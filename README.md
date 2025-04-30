# 📘 Named Entity Recognition and TEI Annotation of Hannah Arendt's Texts
This project applies Named Entity Recognition (NER) techniques and XML/TEI annotation to the texts of Hannah Arendt. The goal is to create an annotated and structured corpus useful for research projects in the fields of philosophy and digital humanities.

### 📌 Main objectives
- Extract **PERSON** entities using spaCy + transformers.
- Annotate the text with semantically coherent XML tags.
- Generate a structured list of mentioned people, inspired by the TEI format.

---

### ⚠️ Important Notice: Run on Google Colab

This project is **designed to run on [Google Colab](https://colab.research.google.com/)**, which provides:

- A pre-configured Python environment
- Free access to GPUs for transformer-based models like `en_core_web_trf`
- Built-in support for spaCy and NLP libraries
- Simplified access to files and notebooks without local setup

**👉 Recommended:** Open the `.ipynb` notebook in Colab to avoid compatibility or installation issues.

---

### ⚙️ Optional: Run Locally

If you prefer to run the project locally, follow these steps to set up your environment:

### 1. Install required libraries

pip install -r requirements.txt

### 2. . Download spaCy models

python -m spacy download en_core_web_trf
