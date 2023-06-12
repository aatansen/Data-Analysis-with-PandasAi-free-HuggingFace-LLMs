## Data Analysis with PandasAi free HuggingFace LLMs

### Python version used in this project

- `3.9.13`

### Create Virtual Environment

- `pip install virtualenv`
- `python -m venv env`
- `.\env\Scripts\activate`

### Install Requirement

- `pip install -r requirements.txt`

### API:

- edit `.env.example` file to `.env` and fillup `HUGGINGFACEHUB_API_TOKEN`
- Get the API Token from [HuggingFace API](https://huggingface.co/settings/tokens)

### Run the app

- `streamlit run app.py`

### Limitation

- Plot not working on the Streamlit UI
- Free llms give wrong/weird answer sometimes

### References

- [Streamlit pandasai prompt driven data analysis using OpenAi API](https://bugbytes.io/posts/streamlit-pandasai-prompt-driven-data-analysis/)