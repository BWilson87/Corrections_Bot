# corrections_bot.py

# === IMPORTS ===
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

import os

# === 1) LOAD TEXT FILES ===
loader = DirectoryLoader(
    "data", 
    glob="*.txt",
    loader_cls=TextLoader
)
docs = loader.load()

# === 2) SPLIT INTO CHUNKS ===
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
splits = text_splitter.split_documents(docs)

# === 3) SETUP EMBEDDINGS ===
embeddings = OllamaEmbeddings(
    model="mistral",
    # tip: add longer timeout if you want
    # request_timeout=120
)

# === 4) CREATE / LOAD VECTORSTORE ===
# ✅ Use persistent storage to avoid re-embedding every time!
db_path = "db"

if os.path.exists(db_path):
    print("📁 Reusing existing Chroma DB...")
    vectorstore = Chroma(
        persist_directory=db_path,
        embedding_function=embeddings
    )
else:
    print("🧩 Creating new Chroma DB, please wait...")
    vectorstore = Chroma.from_documents(
        splits,
        embeddings,
        persist_directory=db_path
    )
    vectorstore.persist()
    print("✅ Done embedding and saved to disk!")

# === 5) CONNECT LOCAL LLM ===
llm = Ollama(model="mistral")

# === 6) RETRIEVAL QA CHAIN ===
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# === 7) SIMPLE CHAT LOOP ===
print("\n🗂️ Corrections Legal Bot — Ask me anything! (type 'exit' to quit)\n")

while True:
    query = input("❓ You: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Bye!")
        break

    result = qa_chain({"query": query})
    answer = result["result"]
    sources = result["source_documents"]

    print("\n✅ Answer:\n", answer)
    print("\n📎 Sources:")
    for src in sources:
        print("-", src.metadata["source"])
    print("\n---")