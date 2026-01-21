# Craete a virtual environment
conda create -n bankbot python=3.10 -y
conda activate bankbot

# Create directory 
bash template.sh

# Install dependencies
pip install -r requirements.txt

# Actual run by me 

```
pip install -U langchain-community pypdf
pip install -U langchain-text-splitters langchain-community pypdf pinecone-client
pip install -U langchain-community sentence-transformers
pip install -U langchain-core
pip uninstall pinecone-client -y
pip install -U pinecone   
python store_index.py


pip install "langchain==0.3.7" "langchain-core<1.0.0" "langchain-community==0.3.7"
pip install "langchain-pinecone==0.2.13"

pip install --upgrade "langchain==0.3.7" \
            "langchain-community==0.3.7" \
            "langchain-core==0.3.83" \
            "langsmith==0.6.4" \
            "langchain-text-splitters==0.3.8"



pip uninstall -y langchain langchain-community langchain-classic langchain-text-splitters langsmit
pip install \
    "langchain>=0.3.9" \
    "langchain-community>=0.3.9" \
    "langchain-text-splitters>=0.3.0" \
    "langsmith==0.6.4" \
    "langchain-pinecone==0.2.13"

```

pip install -U langchain-huggingface
from langchain_huggingface import HuggingFaceEmbeddings
pip install "langchain-community>=0.3.7"

pip uninstall -y langchain langchain-community langchain-text-splitters langsmith langchain-pinecone
pip install "langchain==0.3.7" "langchain-community==0.3.7" "langchain-text-splitters==0.3.0" "langsmith<0.2.0" "langchain-pinecone==0.2.13"
from langchain_huggingface import HuggingFaceEmbeddings



# How to run 

conda activate bankbot
python store_index.py
python app.py

click on 
http://192.168.1.12:8080


