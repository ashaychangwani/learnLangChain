import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
os.environ['OPENAI_API_KEY'] = apikey

st.title('YoutubeGPT Creator')
prompt = st.text_input('Plugin the report here')

llm = OpenAI(temperature=0.9)

memory = ConversationBufferMemory(input_key = 'topic', memory_key='chat_history')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Write me a Youtube Video title about {topic}',
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template='Write me a Youtube Video script based on the title: {title}',
)


#create title chain
title_chain = LLMChain(llm = llm, prompt = title_template, verbose = True, output_key='title', memory=memory)
script_chain = LLMChain(llm = llm, prompt = script_template, verbose = True, output_key='script', memory=memory)

sequential_chain = SequentialChain(chains = [title_chain, script_chain], input_variables=['topic'], output_variables=['title','script'], verbose = True)


if prompt: 
    response = sequential_chain({'topic': prompt})
    st.write(response['title'])
    st.write(response['script'])
    with st.expander('Show Conversation History'):
        st.info(memory.buffer)