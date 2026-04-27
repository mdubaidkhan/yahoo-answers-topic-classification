"""
extract_figures.py

Extracts all image outputs from main_notebook.ipynb and saves them
to the assets/ folder. Run this from the repository root.

Usage:
    python scripts/extract_figures.py
"""

import json
import base64
import os

NOTEBOOK_PATH = "main_notebook.ipynb"
OUTPUT_DIR = "assets"

def extract_figures(notebook_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    figure_count = 0

    for cell_index, cell in enumerate(notebook.get("cells", [])):
        outputs = cell.get("outputs", [])
        for output in outputs:
            # Handle display_data and execute_result with image content
            data = output.get("data", {})
            for mime_type, content in data.items():
                if mime_type.startswith("image/"):
                    extension = mime_type.split("/")[-1]
                    if extension == "jpeg":
                        extension = "jpg"
                    figure_count += 1
                    filename = f"figure_{figure_count:02d}_cell_{cell_index}.{extension}"
                    filepath = os.path.join(output_dir, filename)

                    # content may be a list of strings or a single string
                    if isinstance(content, list):
                        image_data = "".join(content)
                    else:
                        image_data = content

                    with open(filepath, "wb") as img_file:
                        img_file.write(base64.b64decode(image_data))

                    print(f"Saved: {filepath}")

    if figure_count == 0:
        print("No image outputs found in the notebook.")
        print("Make sure you have run all cells in Colab before extracting figures.")
    else:
        print(f"\nDone. {figure_count} figure(s) saved to '{output_dir}/'.")

if __name__ == "__main__":
    extract_figures(NOTEBOOK_PATH, OUTPUT_DIR)
