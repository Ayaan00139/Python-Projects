from PIL import Image
from pathlib import Path
import sys
import numpy as np
import pickle as pi
import pypdf as pdf
import zipfile
import os

class Search:
    def __init__(self):
        self.loop=True
        self._model=None
        self.database={}
        self.vector=[]
    
    @property
    def model(self):
        if self._model is None:
            print("Loading AI model into RAM...")
            from sentence_transformers import SentenceTransformer
            self._model = SentenceTransformer("clip-ViT-B-32")
            print("Model ready!")
        return self._model

    def store_folder(self,path):
        model=self.model

        def extract_zip(file_path):
            model=self.model
            with zipfile.ZipFile(file_path, "r") as z:
                contents = z.namelist()

            summary = f"Zip archive {file_path.name} containing: " + ", ".join(contents[:40])
            return model.encode(summary, normalize_embeddings=True)
        
        def read_pdf(i):
            model=self.model
            fullpdf=pdf.PdfReader(i)
            for j in range(len(fullpdf.pages)):
                text=fullpdf.pages[j].extract_text()
                if text.strip():
                    self.database[f"{i} (Page {j + 1})"]= model.encode(f"{i.name}{text[:1000]}",normalize_embeddings=True)

        for i in path.iterdir():
            try:
                print(f"Indexing: {i.name}")
                if i.name.startswith(".") or i.name in ["__pycache__", "venv", ".venv", "site-packages","node_modules","Images","Wallpapers","wallpaper"]:
                    continue
                if not i.is_file():
                    self.store_folder(i)
                    continue
                if str(i) in self.database:
                    continue
                if i.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp", ".bmp"]:
                    vector = self.model.encode(Image.open(i).convert("RGB"), normalize_embeddings=True)
                    self.database[str(i)]=vector

                elif i.suffix.lower() in [".txt", ".csv", ".md", ".json", ".py"]:
                    text=i.read_text(encoding="utf-8", errors="ignore")
                    if not text.strip():
                        continue
                    vector = model.encode(f"{i.name}: {text[:1000]}",normalize_embeddings=True)
                    self.database[str(i)]=vector

                elif i.suffix.lower() == ".pdf":
                    read_pdf(i)

                elif i.suffix.lower() == ".zip":
                    vector = extract_zip(i)
                    self.database[str(i)]=vector
            except Exception:
                continue
    
    def store_database(self):
        with open("index.pkl", "wb") as f:   # "w" means write, and "b" means binary
            pi.dump(self.database, f)

    def open_database(self):
        with open("index.pkl", "rb") as f:
            self.database = pi.load(f)
        
    def search_folders(self,query,fil):
        model=self.model
        filtered_vectors=[]
        filtered_names=[]
        for name,value in self.database.items():
            if fil==0:
                filtered_names.append(name)
                filtered_vectors.append(value)
            elif fil==1:
                if any((name.lower()).endswith(ext) for ext in image_exts):
                    filtered_names.append(name)
                    filtered_vectors.append(value)
            elif fil == 2:
                if ".pdf" in (name.lower()):
                    filtered_names.append(name)
                    filtered_vectors.append(value)

            elif fil == 3:
                if any((name.lower()).endswith(ext) for ext in code_exts):
                    filtered_names.append(name)
                    filtered_vectors.append(value)
            elif fil == 4:
                if name.lower().endswith(".zip"):
                    filtered_names.append(name)
                    filtered_vectors.append(value)
            else:
                sys.exit("Enter A Filter")

        if len(filtered_names) == 0:
            return "No files found for that category!"
        filtered_vectors=np.array(list(filtered_vectors))
        query_vec = model.encode(query, normalize_embeddings=True)
        scores = filtered_vectors @ query_vec
        sorted_scores=np.argsort(scores)[::-1] # ::-1 to reverse the sort 
        if len(sorted_scores)>=3:
            return f"Top 3 Results: \n {filtered_names[sorted_scores[0]]} Match: {scores[sorted_scores[0]]*100:.1f} \n  {filtered_names[sorted_scores[1]]} Match: {scores[sorted_scores[1]]*100:.1f}  \n {filtered_names[sorted_scores[2]]} Match: {scores[sorted_scores[2]]*100:.1f} "
        else:
            return f"Results: {filtered_names[sorted_scores[0]]} Match: {scores[sorted_scores[0]]*100:.1f}"

        

os.environ["HF_HUB_VERBOSITY"] = "error"
image_exts = [".jpg", ".jpeg", ".png", ".webp", ".bmp"]
code_exts = [".txt", ".csv", ".md", ".json", ".py"]

def main():
    engine=Search()
    while True:
        goodinput=input("[0] Store  [1] Search  [q] Quit: ")
        match goodinput:
            case "0":
                if Path("index.pkl").exists():
                    engine.open_database()
                name=input('Enter Exact Path Of The Folder You Need To Organise, You Can Add Multiple Folder Path Seprated By " ": ')
                engine.model
                if " " in name.strip():
                    mutiple=name.split(" ")
                    for j in mutiple:
                        path=Path(j)
                        if not path.exists():
                            sys.exit("Path Does Not Exits")
                        if path.is_file():
                            sys.exit("Path Redirects to a File Not Folder")
                        engine.store_folder(path)
                else:
                    print("ON IT....")
                    path=Path(name)
                    if not path.exists():
                        sys.exit("Path Does Not Exits")
                    if path.is_file():
                        sys.exit("Path Redirects to a File Not Folder")
                    engine.store_folder(path)
                engine.store_database()
                print(f"Successfully indexed and saved {len(engine.database)} items to index.pkl!")
            
            case "1":
                if not Path("index.pkl").exists():
                    sys.exit("No Folders Stored")
                try:
                    Filter=int(input("Filter: [0] All  [1] Images  [2] PDFs  [3] Code/Text [4] Zip/Archives: "))
                except ValueError:
                    sys.exit("Please Enter A Correct Input")
                engine.model
                engine.open_database()
                query=input("Enter The Query You Want To Search The File For: ")
                response=engine.search_folders(query,Filter)
                print(response)
            case "q":
                print("Program Exited")
                break
            case _:
                sys.exit("Wrong Input")

if __name__=="__main__":
    main()