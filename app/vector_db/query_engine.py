# Description: This file contains the query engine for the vector database. It is responsible for querying the vector database and returning the response.

import os
from dotenv import load_dotenv
from llama_index.response.pprint_utils import pprint_response
from llama_index import VectorStoreIndex,SimpleDirectoryReader
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index import     VectorStoreIndex
from llama_index import   SimpleDirectoryReader
from llama_index import StorageContext
from llama_index import load_index_from_storage
from vector_db.vector_db_functions import load_vector_db

def get_query_engine():
    """Initialize and return the query engine."""
    index = load_vector_db()
    
    retriever = VectorIndexRetriever(index=index, similarity_top_k=4)
    postprocessor = SimilarityPostprocessor(similarity_cutoff=0.80)
    
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        node_postprocessors=[postprocessor]
    )
    return query_engine


def query_vector_db(query: str):
    """Query the vector database and return the response."""
    query_engine = get_query_engine()
    response = query_engine.query(query)
    return str(response)
