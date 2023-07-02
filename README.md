## Data Analysis with PandasAi free HuggingFace LLMs

### Python version used in this project

- `3.9.13`

### Create Virtual Environment

```bash
pip install virtualenv
```

```bash
python -m venv env
```

```bash
.\env\Scripts\activate
```

### Install Requirement

```bash
pip install -r requirements.txt
```

### API:

- edit `.env.example` file to `.env` and fillup `HUGGINGFACEHUB_API_TOKEN`
- Get the API Token from [HuggingFace API](https://huggingface.co/settings/tokens)

### Run the app

```bash
streamlit run app.py
```

### Limitation

- `matplotlib.use('TkAgg')` working with `pandasai==0.5.0` but buggy.
- Free LLMs give wrong/weird answer sometimes

### References

- [PandasAi](https://github.com/gventuri/pandas-ai)
- [HuggingFace](https://huggingface.co/)
- [Streamlit pandasai prompt driven data analysis using OpenAi API](https://bugbytes.io/posts/streamlit-pandasai-prompt-driven-data-analysis/)