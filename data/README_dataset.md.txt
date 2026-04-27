# Yahoo Answers Dataset Download Instructions

This project uses the **Yahoo Answers Topic Classification** dataset, which is too large to commit directly to GitHub.

## Source Links

- Dataset repo: https://github.com/LC-John/Yahoo-Answers-Topic-Classification-Dataset
- Google Drive folder: https://drive.google.com/drive/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M?resourcekey=0-TLwzfR2O-D2aPitmn5o9VQ

## File to Download

Download this archive from the Drive folder:

- `yahoo_answers_csv.tar.gz`

## How to Extract

Run from your terminal:

```bash
tar -xzf yahoo_answers_csv.tar.gz
```

This will produce `train.csv` and `test.csv`.

## Where to Place the Files

This project loads data directly in Google Colab. After extracting the archive, upload `train.csv` and `test.csv` to your Colab session via the sidebar file browser (Files > Upload). The notebook expects both files in the Colab working directory — not in a `data/` subfolder.

## Notes

- Do **not** commit raw dataset files to GitHub.
- Keep only instructions and lightweight metadata in `data/`.