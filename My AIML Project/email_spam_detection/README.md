# SpamGuard AI – Email Spam Detection

A supervised machine-learning project that classifies an email as **Spam** or **Not Spam**.
Built by a team of three: **Frontend**, **Backend/ML**.

The frontend is a **Streamlit** app. It loads the trained model directly — no separate
API server is required to use the app.

```
Streamlit app (streamlit_app/app.py)  ──loads──▶  model.pkl (TF-IDF + SVM)
```

An optional Flask API (`backend/app.py`) is still included if you need a plain REST
endpoint for something else (e.g. another program calling `/predict`), but it is not
needed to run the Streamlit app.

## Project structure

```
email_spam_detection/
├── requirements.txt
├── README.md
├── streamlit_app/
│   └── app.py                # Streamlit frontend — loads backend/model.pkl directly
├── backend/
│   ├── app.py                # Optional Flask API (POST /predict), not needed by Streamlit
│   ├── train_model.py        # Trains + evaluates 3 models, saves the best as model.pkl
│   ├── download_dataset.py   # Downloads the large Enron-Spam dataset (run once)
│   ├── test_api.py           # 21 automated checks for the Flask API (optional)
│   ├── spam_emails.csv       # Team dataset (40 labelled emails)
│   ├── model.pkl             # Trained model (ready to use)
│   ├── metrics.json          # Evaluation results from the last training run
│   └── data/                 # Enron dataset lands here (git-ignored, ~50 MB)
└── ml_exploration/           # Earlier exploration work (kept for reference)
```

## How to run

Requires Python 3.9+.

```bash
# 1. Install dependencies
python -m pip install -r requirements.txt

# 2. Start the app  (model.pkl is already included, so no training needed)
cd streamlit_app
streamlit run app.py
```

This opens the app in your browser automatically (usually **http://localhost:8501**).
Paste an email and click **Check Email**.

### Optional: retrain the model

```bash
cd backend
python download_dataset.py    # once (~15 MB download)
python train_model.py         # under a minute
```

Without the Enron download, `train_model.py` still works but falls back to the 40-email
dataset, which is too small for reliable results.

### Run the tests

```bash
cd backend
python test_api.py
```

(`test_api.py` tests the optional Flask API in `backend/app.py`, not the Streamlit app.)

## Optional: the Flask API

If you want a plain REST endpoint (for example, to call from another program), you can
still run the Flask API instead of, or alongside, Streamlit:

```bash
python -m pip install flask
cd backend
python app.py
```

**`POST /predict`**

Request:
```json
{ "email": "Win a free iPhone now! Click this link to claim your prize." }
```

Response (200):
```json
{
  "prediction": "spam",
  "label": "Spam",
  "confidence": 0.9999,
  "spam_probability": 0.9999
}
```

Invalid input returns HTTP 400 with `{"error": "<reason>"}` (missing field, empty text,
fewer than 5 or more than 20,000 characters, non-text value).

**`GET /health`** → `{"status": "ok", "model": "SVM"}`

## The machine-learning part

| Step | What we do |
|------|-----------|
| Data | 30,444 real emails from **Enron-Spam** (48% spam) + the team's 40 emails |
| Features | TF-IDF on words and word pairs, English stop-words removed, top 100,000 features |
| Models compared | Naive Bayes, Logistic Regression, SVM (LinearSVC, probability-calibrated) |
| Split | 80% train / 20% test (stratified, fixed seed). The test set is never used for training |
| Saved artifact | One `model.pkl` = TF-IDF + classifier in a single scikit-learn Pipeline, so training and prediction always use identical preprocessing |

### Results (6,089 unseen test emails)

| Model | Accuracy | Precision | Recall | F1 | Team's 40 emails* |
|-------|---------:|----------:|-------:|---:|------------------:|
| Naive Bayes | 99.00% | 98.7% | 99.2% | 0.9895 | 97.5% |
| Logistic Regression | 98.88% | 98.2% | 99.5% | 0.9884 | 95.0% |
| **SVM (chosen)** | **99.11%** | **98.9%** | **99.3%** | **0.9907** | 97.5% |

\*A second, independent test: models trained without the team's emails, then scored on them.
The final `model.pkl` is retrained on everything after these scores were measured.

### Why we changed the dataset

The original 40-email dataset produced "87.5% accuracy", but that was measured on only
**8 test emails** (one mistake = 12.5%), so the number was not meaningful. All three models
also scored identically, which is a sign there was too little data to tell them apart.
Training on ~30,000 real emails gives a far more trustworthy evaluation.

## Known limitations (good to mention in the presentation)

- **Training data is from ~2000–2005 (Enron).** Modern phishing (fake Netflix / bank / delivery
  notices) looks different. In our informal check with 30 hand-written modern emails the model
  got 29 right and missed a fake "Netflix subscription expired" message.
- English only.
- Only the first 3,000 characters of an email are used; there is no analysis of links,
  attachments, headers, or sender reputation.
- A classifier gives a probability, not a guarantee. Treat the confidence figure as a guide.

## Ideas for future improvement

- Add recent phishing/spam samples to `spam_emails.csv` and retrain.
- Show the words that pushed the decision toward spam (model explainability).
- Add sender/link-based features.
- Deploy the Streamlit app to Streamlit Community Cloud for a public link.

## Team roles

| Area | Files |
|------|-------|
| Frontend | `streamlit_app/app.py` |
| Backend | `backend/app.py` (optional Flask API), `backend/test_api.py` |
| ML | `backend/train_model.py`, `backend/download_dataset.py`, `backend/spam_emails.csv`, `ml_exploration/` |

## Data credit

Enron-Spam: Metsis, Androutsopoulos & Paliouras (2006), *Spam Filtering with Naive Bayes –
Which Naive Bayes?* CSV version from <https://github.com/MWiechmann/enron_spam_data>.
