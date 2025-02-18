import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from  config import OPENAI_API_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

INDEX_DIR = "content/index"
DATA_DIR = "content/data"


def create_vector_db():
    if not os.path.exists(DATA_DIR):
        """Create a new vector database from documents and persist it."""
        documents = SimpleDirectoryReader(DATA_DIR).load_data()
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        index.storage_context.persist(persist_dir=INDEX_DIR)
        return index
    else:
        return load_vector_db()


def load_vector_db():
    """Load the persisted vector database."""
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
    return load_index_from_storage(storage_context)
