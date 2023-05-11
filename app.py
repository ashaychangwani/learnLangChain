import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
os.environ['OPENAI_API_KEY'] = apikey

st.title('YoutubeGPT Creator')
prompt = st.text_input('Plugin the report here')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Write me a Youtube Video title about {topic}',
)
llm = OpenAI(temperature=0.9)


#create title chain
title_chain = LLMChain(llm = llm, prompt = title_template, verbose = True)


if prompt: 
    response = title_chain.run(topic=prompt)
    st.write(response)
