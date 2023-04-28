"""
Read environment variables from .env file, if it exists, in an error free manner.
"""
import os
from pathlib import Path
from dotenv import load_dotenv


def read_env(env_file =  '.ENV'):
    values = {
        'OPENAI_API_KEY': None,
        'MAX_TOKENS': 3000,
    }
    # try to load the .env file
    try:
        load_dotenv(dotenv_path= Path('.') / env_file)
        values['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
        values['MAX_TOKENS'] = int(os.getenv('MAX_TOKENS'))
    except:
        print("Error loading .env file")
    return values
    