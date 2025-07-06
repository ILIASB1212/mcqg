import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from utils import read_file,get_table_data
import  logging

from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import streamlit as st
from MCQGenerator import generate_evaluate_chain



with open(r"C:\Windows\System32\mcqg\responce.json","r") as f:
    response_json=json.loads(f)