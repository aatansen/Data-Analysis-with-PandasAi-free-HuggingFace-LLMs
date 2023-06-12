from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
import matplotlib

#list of free LLMs that support PandasAI (more coming in future):
from pandasai.llm.starcoder import Starcoder
# from pandasai.llm.open_assistant import OpenAssistant
# from pandasai.llm.falcon import Falcon

matplotlib.use('TkAgg')

load_dotenv()

API_KEY = os.getenv('HUGGINGFACEHUB_API_TOKEN')

llm = Starcoder(api_token=API_KEY)
# llm = OpenAssistant(api_token=API_KEY)
# llm = Falcon(api_token=API_KEY)
pandas_ai =PandasAI(llm)


st.title('Analysis CSV file with Ai')

uploaded_file=st.file_uploader('Upload your CSV file', type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    prompt = st.text_input('Enter your prompt')

    if st.button('Generate'):
        if prompt:
            with st.spinner("generating response..."):
                st.write(pandas_ai.run(df,prompt=prompt))
        else:
            st.warning("Please enter your prompt.")
