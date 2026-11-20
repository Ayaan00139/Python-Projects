from sentence_transformers import SentenceTransformer
from PIL import Image
from pathlib import Path
import sys
import numpy as np
import pickle as pi
import pypdf as pdf
import zipfile
image_exts = [".jpg", ".jpeg", ".png", ".webp", ".bmp"]
code_exts = [".txt", ".csv", ".md", ".json", ".py"]
loop=True
model = SentenceTransformer("clip-ViT-B-32")
print("Model ready!")
pdf_vector=[]
database={}
vector=[] # temp data type
multiple=[]

def store_folder(path):

    def extract_zip(file_path):
        with zipfile.ZipFile(file_path, "r") as z:
            contents = z.namelist()

        summary = f"Zip archive {file_path.name} containing: " + ", ".join(contents[:20])
        return model.encode(summary, normalize_embeddings=True)
    
    def read_pdf(i):
        fullpdf=pdf.PdfReader(i)
        for j in range(len(fullpdf.pages)):
            text=fullpdf.pages[j].extract_text()
            if text.strip():
                database[f"{i} (Page {j + 1})"]= model.encode(text[:500],normalize_embeddings=True)

    for i in path.iterdir():
        try:
            print(f"Indexing: {i.name}")
            global pdf_vector
            global vector
            if i.name.startswith(".") or i.name in ["__pycache__", "venv", ".venv", "site-packages","node_modules","Images","Wallpapers","wallpapers"]:
                continue
            if not i.is_file():
                store_folder(i)
                continue
            if str(i) in database:
                continue
            if i.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp", ".bmp"]:
                vector = model.encode(Image.open(i).convert("RGB"), normalize_embeddings=True)
                database[str(i)]=vector

            elif i.suffix.lower() in [".txt", ".csv", ".md", ".json", ".py"]:
                vector = model.encode(i.read_text(encoding="utf-8", errors="ignore")[:500],normalize_embeddings=True)
                database[str(i)]=vector

            elif i.suffix.lower() == ".pdf":
                read_pdf(i)

            elif i.suffix.lower() == ".zip":
                vector = extract_zip(i)
                database[str(i)]=vector
        except:
            continue

def store_database():
    global database
    with open("index.pkl", "wb") as f:   # "w" means write, and "b" means binary
        pi.dump(database, f)

def open_database():
    global database
    with open("index.pkl", "rb") as f:
        database = pi.load(f)
    
def search_folders(query,fil):
    filtered_vectors=[]
    filtered_names=[]
    for name,value in database.items():
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
        else:
            sys.exit("Enter A Filter")

    if len(filtered_names) == 0:
        return "No files found for that category!"
    filtered_vectors=np.array(list(filtered_vectors))
    query_vec = model.encode(query, normalize_embeddings=True)
    scores = filtered_vectors @ query_vec
    sorted_scores=np.argsort(scores)[::-1] # ::-1 to reverse the sort 
    best=sorted_scores[0]
    return f"{filtered_names[best]} is the most Probably the file you are searching for, Match: {scores[best]*100:.1f}"



def main():
    goodinput=input("Would You Like To Store The File Or Search For A File 0 For Store, 1 For Search: ")

    match goodinput:
        case "0":
            if Path("index.pkl").exists():
                open_database()
            name=input('Enter Exact Path Of The Folder You Need To Organise, You Can Add Multiple Folder Path Seprated By " ": ')

            if " " in name.strip():
                mutiple=name.split(" ")
                for j in mutiple:
                    path=Path(j)
                    if not path.exists():
                        sys.exit("Path Does Not Exits")
                    if path.is_file():
                        sys.exit("Path Redirects to a File Not Folder")
                    store_folder(path)

            print("ON IT....")
            path=Path(name)
            if not path.exists():
                sys.exit("Path Does Not Exits")
            if path.is_file():
                sys.exit("Path Redirects to a File Not Folder")
            store_folder(path)
            store_database()
            print(f"Successfully indexed and saved {len(database)} items to index.pkl!")
        
        case "1":
            if not Path("index.pkl").exists():
                sys.exit("No Folders Stored")
            try:
                Filter=int(input("Filter: [0] All  [1] Images  [2] PDFs  [3] Code/Text: "))
            except ValueError:
                sys.exit("Please Enter A Correct Input")
            open_database()
            query=input("Enter The Query You Want To Search The File For: ")
            response=search_folders(query,Filter)
            print(response)
            

if __name__=="__main__":
    main()