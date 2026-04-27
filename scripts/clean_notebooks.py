import json
from pathlib import Path

NOTEBOOK_PATHS = [
    Path("main_notebook.ipynb"),
    Path("checkpoints") / "checkpoint-2.ipynb",
]

if __name__ == "__main__":
    for nb_path in NOTEBOOK_PATHS:
        print(f"Cleaning widgets metadata from: {nb_path}")
        with nb_path.open("r", encoding="utf-8") as f:
            nb = json.load(f)

        nb.get("metadata", {}).pop("widgets", None)

        with nb_path.open("w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
            f.write("\n")

    print("Done.")
