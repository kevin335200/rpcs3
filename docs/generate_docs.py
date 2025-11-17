#!/usr/bin/env python3
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

class CppFileAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.content = self._read_file()
        self.filename = Path(file_path).name

    def _read_file(self) -> str:
        try:
            with open(self.file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    def extract_includes(self) -> List[str]:
        """Extract all #include statements"""
        includes = re.findall(r'#include\s+[<"]([^>"]+)[>"]', self.content)
        return includes

    def extract_namespaces(self) -> List[str]:
        """Extract namespace declarations"""
        namespaces = re.findall(r'namespace\s+(\w+)', self.content)
        return list(set(namespaces))

    def extract_classes_and_structs(self) -> List[Tuple[str, str]]:
        """Extract class and struct declarations with brief description"""
        # Find class/struct definitions
        pattern = r'(?:class|struct)\s+(\w+)'
        matches = re.findall(pattern, self.content)
        return [(match, self._get_context(match)) for match in set(matches)]

    def extract_functions(self) -> List[str]:
        """Extract function declarations"""
        # Simple pattern for common function signatures
        pattern = r'(?:void|int|bool|auto|static|inline|virtual|override|const|u32|u64|s32|f32|f64|std::\w+)\s+(\w+)\s*\('
        matches = re.findall(pattern, self.content)
        # Filter out common false positives
        filtered = [m for m in set(matches) if not m[0].isupper() and len(m) > 2]
        return filtered[:20]  # Return top 20 functions

    def extract_enums(self) -> List[str]:
        """Extract enum declarations"""
        pattern = r'enum\s+(?:class\s+)?(\w+)'
        matches = re.findall(pattern, self.content)
        return list(set(matches))

    def _get_context(self, identifier: str) -> str:
        """Get surrounding context for an identifier"""
        idx = self.content.find(identifier)
        if idx == -1:
            return ""
        start = max(0, idx - 100)
        end = min(len(self.content), idx + 100)
        context = self.content[start:end].strip()
        # Remove newlines for readability
        context = ' '.join(context.split())
        return context[:150]

    def get_line_count(self) -> int:
        """Get total line count"""
        return len(self.content.split('\n'))

    def extract_brief_description(self) -> str:
        """Try to extract a brief description from comments"""
        # Look for file-level comments
        lines = self.content.split('\n')
        for i, line in enumerate(lines[:30]):  # Check first 30 lines
            if '//' in line or '/*' in line:
                comment = line.split('//')[1].strip() if '//' in line else ''
                if comment:
                    return comment[:100]
        return "C++ Source/Header File"

    def generate_markdown(self) -> str:
        """Generate markdown documentation"""
        md = []

        # Header
        md.append(f"# {self.filename}")
        md.append("")

        # Basic Info
        md.append("## File Information")
        md.append(f"- **Location**: `{self.file_path}`")
        md.append(f"- **Type**: {'Header File' if self.filename.endswith('.h') else 'Source File'}")
        md.append(f"- **Lines**: {self.get_line_count()}")
        md.append("")

        # Description
        desc = self.extract_brief_description()
        md.append("## Description")
        md.append(desc)
        md.append("")

        # Includes
        includes = self.extract_includes()
        if includes:
            md.append("## Includes")
            for inc in includes[:15]:  # Show first 15
                md.append(f"- `{inc}`")
            if len(includes) > 15:
                md.append(f"- ... and {len(includes) - 15} more")
            md.append("")

        # Namespaces
        namespaces = self.extract_namespaces()
        if namespaces:
            md.append("## Namespaces")
            for ns in namespaces:
                md.append(f"- `{ns}`")
            md.append("")

        # Classes and Structs
        classes = self.extract_classes_and_structs()
        if classes:
            md.append("## Classes & Structures")
            for cls_name, context in classes[:15]:
                md.append(f"### {cls_name}")
                if context:
                    md.append(f"```cpp")
                    md.append(context[:80])
                    md.append("```")
                md.append("")
            md.append("")

        # Enums
        enums = self.extract_enums()
        if enums:
            md.append("## Enumerations")
            for enum in enums[:10]:
                md.append(f"- `{enum}`")
            md.append("")

        # Functions
        functions = self.extract_functions()
        if functions:
            md.append("## Key Functions")
            for func in functions[:15]:
                md.append(f"- `{func}()`")
            md.append("")

        return "\n".join(md)


def generate_all_docs():
    """Generate documentation for all C++ files"""

    input_dir = "/home/user/rpcs3/rpcs3/Input"
    np_dir = "/home/user/rpcs3/rpcs3/Emu/NP"
    output_input_dir = "/home/user/rpcs3/docs/cpp-files/Input"
    output_np_dir = "/home/user/rpcs3/docs/cpp-files/Emu/NP"

    # Process Input files
    print("Processing Input files...")
    process_directory(input_dir, output_input_dir)

    # Process NP files
    print("Processing NP files...")
    process_directory(np_dir, output_np_dir)

    print("Documentation generation complete!")


def process_directory(source_dir: str, output_dir: str):
    """Process all C++ files in a directory"""
    cpp_files = list(Path(source_dir).glob("*.cpp")) + list(Path(source_dir).glob("*.h"))

    for cpp_file in sorted(cpp_files):
        try:
            analyzer = CppFileAnalyzer(str(cpp_file))
            markdown = analyzer.generate_markdown()

            # Output filename
            output_file = Path(output_dir) / f"{cpp_file.stem}.md"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)

            print(f"  Generated: {output_file.name}")
        except Exception as e:
            print(f"  Error processing {cpp_file.name}: {e}")


if __name__ == "__main__":
    generate_all_docs()
