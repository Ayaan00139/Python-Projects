# OmniSearch 🔍

A local, offline semantic search engine built in Python. Search your images, PDFs, code, text, and zip files by meaning rather than exact filenames.

---

## ⚡ Features

* **Multi-Modal:** Search images, PDFs, code, and text using natural language.
* **Page-Level PDF Search:** Pinpoints the exact page inside multi-page PDFs.
* **Zip Inspection:** Reads the contents of `.zip` files without extracting them.
* **Fast & Offline:** Runs 100% locally using OpenAI's CLIP (`clip-ViT-B-32`) and NumPy matrix math.
* **Type Filtering:** Filter searches by All, Images, PDFs, Code, or Archives.

---

## 📦 Setup

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

Run the script:

```bash
python omnisearch.py
```

1. **Store (`0`):** Enter one or more folder paths to index your files.
2. **Search (`1`):** Choose your filter (e.g. `1` for Images) and type your search query!
3. **Quit (`q`):** Exit the program.
