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
    content = f.read()
    response_json = json.loads(content)



st.title("MCQ GENERATOR APPLICATION WITH LANGCHAIN")

with st.form("user input"):
    file=st.file_uploader("upload file")
    number=st.number_input("nuber of question",min_value=3,max_value=25)
    tone=st.text_input("select the deficulty of mcqor parametre",placeholder="SIMPLE",max_chars=25 )
    subject=st.text_input("select the subject",placeholder="history/math......",max_chars=25 )
    button=st.form_submit_button("create mcq")
    if button and file is not None and number and tone and subject:
        with st.spinner("generating...."):
            try:
                
                text=read_file(file)
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                                {"text":text,
                                "number":number,
                                "subject":subject,
                                "tone":tone,
                                "response_json":json.dumps(response_json)
                                }
                            )
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("error")
            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total Cost: {cb.total_cost}")

                if isinstance(response, dict):
                    # Extract the quiz data from the response
                    quiz = response.get("quiz", None)
                    
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)
                            st.text_area(label="Review",value=response["review"])
                        else:
                            st.error("error in the table data")
                    else:
                        st.write(response) 