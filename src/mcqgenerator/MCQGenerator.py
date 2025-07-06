import os
import json
import traceback
import pandas as pd

from dotenv import load_dotenv
from utils import read_file, get_table_data

from logger import logging

#imporing necessary packages packages from langchain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

#LOAD ENVIREMENT API KEY

load_dotenv()

# ACCEESS THE API KEY

key = os.getenv("OPENAI_API_KEY")

#SET UP THE LLM

llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo",openai_api_key=key)
 # PROMPT TEXT SETUP 
tepmlate=''' 
text:{text}
you are an expert MCQ maker ,given the above text, its your main job to create 
a quiz of {number} of multiple choises questions for {subject} student in {tone} tone.
make sure all question not repeted and sheck all question to be comforming the text as well.
make sure to formate your response like response_json below as a guide.
ensure to make {number} MCQs.
### response_json:
{response_json}
'''

#PUTTING ALL TOGETER WITH P.TEMPLATE

quiz_generation_prompt=PromptTemplate(
    input_variables=["text","number",'subject',"tone","response_json"],
    template=tepmlate
)

#SETUP FIRST CHAIN FOR CREATING QUESTION 

quiz_chain=LLMChain(llm=llm,prompt=quiz_generation_prompt,output_key="quiz",verbose=True)

# GRAMMAR PROMPT TEXT SETUP

TEMPLATE2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""
 #PUTTING ALL TOGETER WITH P.TEMPLATE 2 FOR GRAMMAR CORECTING

quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], 
                                      template=TEMPLATE2)

#SETUP SECOND CHAIN FOR GRAMMAR CORECTION

review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

# COMBINING THE TWO CHAIN FOR MCQ CREATION THEN GRAMAR EVALUATION

generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                        output_variables=["quiz", "review"], verbose=True,)
