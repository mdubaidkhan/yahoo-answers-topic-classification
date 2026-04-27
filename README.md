# Can a Machine Learn What You're Really Asking?
## Yahoo Answers Topic Classification: Scale, Failure Modes, and the Value of More Text

**Course:** Data Mining  
**Dataset:** Yahoo Answers Topic Classification Dataset — 753,677 training samples, 32,265 test samples, 10 topic categories

---

## Start Here: [`main_notebook.ipynb`](./main_notebook.ipynb)

This is the main deliverable. It walks through the complete project story — from motivation and EDA through full-scale experiments and conclusions.

---

## Project Video

[Watch the Project Walkthrough — ADD YOUR LINK HERE]()

---

## Research Questions

This project is organized around three research questions, each derived directly from EDA findings:

| RQ | Question | Technique |
|---|---|---|
| **RQ1** | How well do TF-IDF classifiers scale from 10K to 753K samples? Which category pairs drive the most confusion — and does confusion rank match vocabulary overlap rank? | TF-IDF + Naive Bayes, Logistic Regression, LinearSVC |
| **RQ2** | Does adding question body and best answer improve accuracy — and is the improvement equal across categories, or predicted by each category's missingness rate? | Input ablation (Config A/B/C) + McNemar's test |
| **RQ3** | Does an unsupervised method recover the human topic labels from the raw text, or are Yahoo Answers categories human-imposed distinctions on a continuous semantic space? | BERTopic (SBERT + UMAP + HDBSCAN) |

---

## Results Summary

| Research Question | Key Finding | Metric |
|---|---|---|
| RQ1: Classifier performance at scale | LinearSVC best overall; confusion concentrated in Edu&Ref vs Sci&Math as predicted by vocabulary overlap; TF-IDF representation reaches a ceiling by 753K samples | Macro-F1 = 0.733 (vs. 0.687 probe at 10K) |
| RQ2: Value of more text | Config C > B > A confirmed; A to B gain (+0.051) far exceeds B to C (+0.009); gain is heterogeneous and directly predicted by per-category missingness — Biz&Fin gained least (+0.032), Fam&Rel gained most (+0.113) | McNemar p ≈ 4.1×10⁻¹²⁴ |
| RQ3: BERTopic latent structure | Near-total collapse to 1 topic (99.5% of documents); ARI and NMI indistinguishable from random — Yahoo Answers categories are human-imposed distinctions on a continuous semantic space, not natural clusters | ARI = 0.000, NMI = 0.007 |

**Central conclusion:** The hardest categories to classify are hard for structural reasons that persist across every method — supervised or unsupervised, 10K or 753K training examples. Education & Reference, Business & Finance, and Society & Culture share vocabulary with neighbors, have the most missing body text, and occupy no distinct region of the semantic embedding space.

---

## Dataset

**Name:** Yahoo Answers Topic Classification Dataset  
**Source:** https://www.kaggle.com/datasets/yacharki/yahoo-answers-10-categories-for-nlp-csv

Each record contains four fields:

| Field | Description |
|---|---|
| `question_title` | Title of the question (always present) |
| `question_content` | Body of the question (empty in ~46% of posts) |
| `best_answer` | Community-selected best answer |
| `class_index` | One of 10 topic categories (1–10 in raw file, remapped to 0–9) |

**The 10 categories:**  
Society & Culture, Science & Mathematics, Health, Education & Reference, Computers & Internet, Sports, Business & Finance, Entertainment & Music, Family & Relationships, Politics & Government

**Size after cleaning** (rows with any empty text field dropped):
- Training set: 753,677 samples (down from 1,399,999 — 46.2% removed)
- Test set: 32,265 samples

The dataset files are too large to commit to this repo (~500 MB). Download `train.csv` and `test.csv` from the Kaggle link above and upload them directly to your Colab session. See [`data/README_data.md`](./data/README_data.md) for full instructions.

---

## How to Reproduce

This project was built entirely in Google Colab.

1. Open `main_notebook.ipynb` in [Google Colab](https://colab.research.google.com/)
2. Download `train.csv` and `test.csv` from Kaggle and upload them to your Colab session via Files > Upload
3. Run all cells top to bottom — the first cell installs all required packages
4. For the BERTopic section (Section 8), a GPU runtime is recommended: Runtime > Change runtime type > T4 GPU

To install dependencies locally:
```bash
pip install -r requirements.txt
```

---

## Scripts

The `scripts/` folder contains utilities for local setup, data access, and repo verification.

| Script | Description |
|---|---|
| [`scripts/setup.sh`](./scripts/setup.sh) | Creates a `.venv` virtual environment and installs all dependencies from `requirements.txt` |
| [`scripts/download_data.sh`](./scripts/download_data.sh) | Prints step-by-step instructions for downloading the dataset from Kaggle or Google Drive |
| [`scripts/extract_figures.py`](./scripts/extract_figures.py) | Extracts all image outputs from `main_notebook.ipynb` and saves them to `assets/` |
| [`scripts/verify_setup.py`](./scripts/verify_setup.py) | Checks that all expected repo files exist and all key packages are installed |

Quick usage:

```bash
# Set up local Python environment
bash scripts/setup.sh

# Get dataset download instructions
bash scripts/download_data.sh

# Extract notebook figures to assets/
python scripts/extract_figures.py

# Verify repo structure and dependencies
python scripts/verify_setup.py
```

---

## Key Dependencies

| Package | Version | Used For |
|---|---|---|
| Python | 3.x (see requirements.txt) | Runtime |
| pandas | 2.x | Data loading and cleaning |
| numpy | 1.x / 2.x | Numerical operations |
| scikit-learn | 1.x | TF-IDF, classifiers, metrics |
| matplotlib | 3.x | All visualizations |
| seaborn | 0.13.x | Heatmaps and EDA plots |
| scipy | 1.x | McNemar's test (chi2) |
| bertopic | latest | RQ3 topic modeling |
| sentence-transformers | latest | SBERT embeddings (all-MiniLM-L6-v2) |
| umap-learn | latest | Dimensionality reduction |
| hdbscan | latest | Density-based clustering |

Full list of every package and version from the Colab session: [`requirements.txt`](./requirements.txt)

---

## Checkpoint Notebooks

| Notebook | Contents |
|---|---|
| [`checkpoints/checkpoint_1.ipynb`](./checkpoints/checkpoint_1.ipynb) | Three candidate datasets evaluated and compared (Yahoo Answers, Goodreads, MovieLens 20M); Yahoo Answers selected; initial EDA — token distributions, class balance, missingness audit |
| [`checkpoints/checkpoint_2.ipynb`](./checkpoints/checkpoint_2.ipynb) | Additional EDA run to discover interesting questions; research questions formalized from EDA findings; hypotheses stated; pilot classifier and sanity tests run |

---

## Repo Structure

```
yahoo-answers-topic-classification/
│
├── main_notebook.ipynb          # Main deliverable — start here
├── README.md
├── requirements.txt             # Full dependency list (exported from Colab)
├── .gitignore
│
├── checkpoints/
│   ├── checkpoint_1.ipynb       # CP1: Dataset selection and initial EDA
│   └── checkpoint_2.ipynb       # CP2: Research questions and pilot experiments
│
├── data/
│   └── README_data.md           # Instructions for downloading the dataset
│
└── scripts/
    ├── setup.sh                 # Create virtual environment and install dependencies
    ├── download_data.sh         # Dataset download instructions
    ├── extract_figures.py       # Extract notebook image outputs to assets/
    └── verify_setup.py          # Validate repo structure and dependencies
```

---

## References

1. Zhang, X., Zhao, J., & LeCun, Y. (2015). Character-level convolutional networks for text classification. *NeurIPS 28*.
2. Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. *arXiv:2203.05794*.
3. Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. *EMNLP 2019*. arXiv:1908.10084.
4. McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform Manifold Approximation and Projection. *JOSS*. arXiv:1802.03426.