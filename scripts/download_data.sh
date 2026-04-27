#!/bin/bash
# download_data.sh
# Instructions for obtaining the Yahoo Answers dataset.
# Automatic download is not available as the dataset requires
# a Kaggle account. Follow the steps below.

echo ""
echo "Yahoo Answers Topic Classification Dataset"
echo "------------------------------------------"
echo ""
echo "This dataset cannot be downloaded automatically."
echo "Please follow these steps:"
echo ""
echo "  1. Go to: https://www.kaggle.com/datasets/yacharki/yahoo-answers-10-categories-for-nlp-csv"
echo "  2. Sign in to your Kaggle account (free)."
echo "  3. Click the Download button to get the archive."
echo "  4. Extract train.csv and test.csv from the archive."
echo "  5. Upload both files to your Google Colab session via Files > Upload."
echo ""
echo "The notebook expects train.csv and test.csv in the Colab working directory."
echo ""
echo "Alternatively, download the tar.gz archive from Google Drive:"
echo "  https://drive.google.com/drive/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M"
echo ""
echo "Then extract with:"
echo "  tar -xzf yahoo_answers_csv.tar.gz"
echo ""
