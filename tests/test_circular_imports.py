import importlib
import os
import unittest
from pathlib import Path


class TestCircularImports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project_root = Path(__file__).parent / "royalflush"

    def test_imports(self):
        """
        Test that all modules can be imported without triggering circular dependencies.
        """
        python_files = [
            p for p in self.project_root.rglob("*.py") if "__init__.py" not in p.name and "test_" not in p.name
        ]

        for file_path in python_files:
            relative_path = file_path.relative_to(self.project_root).with_suffix("")
            module_name = ".".join(relative_path.parts)

            with self.subTest(module=module_name):
                try:
                    importlib.import_module(module_name)
                except Exception as e:
                    self.fail(f"Failed to import {module_name}: {e}")


if __name__ == "__main__":
    unittest.main()
