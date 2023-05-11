import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI


os.environ['OPENAI_API_KEY'] = apikey

st.title('YoutubeGPT Creator')