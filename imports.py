# imports.py

# General Imports
import PyPDF2
import requests
from bs4 import BeautifulSoup
import openai
import streamlit as st

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

# Local Module Imports (assuming they are in the same directory)
from data_ingestion import ingest_pdf_data, ingest_text_file_data, ingest_data
from indexing import index_data
from retrieval import retrieve_data
from generation import generate_response
from ui import run_interface
import os

# Set OpenAI API Key (replace with your actual API key)

openai.api_key = os.getenv("OPENAI_API_KEY")