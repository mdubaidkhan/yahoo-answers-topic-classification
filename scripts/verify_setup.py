"""
verify_setup.py

Checks that the repository structure is correct and that
all key dependencies are installed. Run this from the repository root.

Usage:
    python scripts/verify_setup.py
"""

import importlib
import os
import sys

# Expected files and folders at the repo root
EXPECTED_STRUCTURE = [
    "main_notebook.ipynb",
    "README.md",
    "requirements.txt",
    ".gitignore",
    "checkpoints/checkpoint_1.ipynb",
    "checkpoints/checkpoint_2.ipynb",
    "data/README_data.md",
    "scripts/setup.sh",
    "scripts/download_data.sh",
    "scripts/extract_figures.py",
    "scripts/verify_setup.py",
]

# Key packages used in main_notebook.ipynb
REQUIRED_PACKAGES = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "sklearn",
    "scipy",
    "bertopic",
    "sentence_transformers",
    "umap",
    "hdbscan",
]

def check_structure():
    print("Checking repository structure...")
    all_present = True
    for path in EXPECTED_STRUCTURE:
        exists = os.path.exists(path)
        status = "OK" if exists else "MISSING"
        print(f"  [{status}] {path}")
        if not exists:
            all_present = False
    return all_present

def check_packages():
    print("\nChecking key dependencies...")
    all_installed = True
    for package in REQUIRED_PACKAGES:
        try:
            mod = importlib.import_module(package)
            version = getattr(mod, "__version__", "unknown version")
            print(f"  [OK]      {package} ({version})")
        except ImportError:
            print(f"  [MISSING] {package}")
            all_installed = False
    return all_installed

def main():
    structure_ok = check_structure()
    packages_ok = check_packages()

    print("")
    if structure_ok and packages_ok:
        print("All checks passed. Repository is ready.")
    else:
        if not structure_ok:
            print("Some expected files are missing. Check the repo structure.")
        if not packages_ok:
            print("Some packages are missing. Run: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
