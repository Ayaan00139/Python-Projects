# OmniSearch 🔍
#### Video Demo: <URL HERE>
#### Description:

OmniSearch is a local, file search engine built in Python. Unlike traditional file search tools that rely on exact filename matches, it indexes and searches files based on their content. Users can provide one or multiple directory paths to be indexed, and OmniSearch creates a vector of anything using a **CLIP** model of **OPENAI** of everything inside including images, multi-page PDFs, source code, text files, and zip archives.

### How It Works

OmniSearch uses a OpenAI's CLIP (`clip-ViT-B-32`) multimodal transformer model, integrated with the `sentence-transformers` library. The model projects both images and text into a 512-dimensional vector space:

1. **Images:** Images (`.jpg`, `.png`, `.webp`, `.bmp`) are loaded via Pillow, converted to RGB, and transformed into 512-dimensional vectors.
2. **PDF Documents:** Multi-page PDFs are parsed page-by-page using `pypdf`. Rather than summarizing the entire document into one blurry vector, each page is indexed individually as an independent document stored like this ->(`file.pdf (Page 1)`) with the vector of each page, allowing users to find the exact page relevant to their query.
3. **Zip Archives:** Zip files are extracted in-memory using `zipfile` to get file manifests and table of contents without decompressing them to disk, creating a vector of the archive's internal structure.
4. **Code & Text:** Source code files and plaintext notes are encoded alongside their filenames, filtering out empty files to prevent mis matching of queries.
5. **Vector Similarity:** When a search query is submitted, it is encoded into a 512-dimensional query vector. OmniSearch calculates cosine similarity scores across candidate vectors using NumPy (`scores = matrix @ query_vec`), returning the top 3 ranked matches with a percentage confidence score.

### Key Design Decisions & Challenges

* **Loading:** Loading a neural network into RAM takes several seconds and heavy memory. OmniSearch ensures that the model is loaded inside a Python `@property`/getter function so that the model is only loaded into ram if the input prompt is filled correctly so that the program starts instantly and the user does not feel a delay
* **Type Filters:** When OmniSearch was almost done in making, there was a bug which prioritize texts even if the query was searching for images cause the similarity will obviously match text for text rather then image. To fix this bug and ensure query is almost always correct Category Filtering was introduced (`[0] All`, `[1] Images`, `[2] PDFs`, `[3] Code/Text`, `[4] Zip/Archives`) which isolated vectors to only search for the specific categories using file extensions before ranking.

### Project Files

* **`project.py`**: The application containing the `Search` engine class and the 3 top-level functions (`store_database`, `open_database`, and `filter_data`), along with main function.
* **`test_project.py`**: The tests were executed with `pytest`. It tests database storing (in disk, in file `index.pkl` ), opening, and filtering logic using test data which does not need to load the heavy AI model.
* **`requirements.txt`**: Pinned external dependencies including `sentence-transformers`, `pillow`, `numpy`, `pypdf`, and `pytest`.

### Future Scope

For future iterations, accuracy can be further scaled by upgrading the 512 dimensional model `clip-ViT-B-32` to the 768 dimensional `clip-ViT-L-14` model or even the 1024 dimensional `open_clip` model . Additionally, integrating Meta's FAISS library which uses HNSW graph indexing would enable sub-millisecond searches over millions of files.
