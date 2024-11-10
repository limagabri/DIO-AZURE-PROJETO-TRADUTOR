import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_KEY")
TRANSLATOR_API_KEY = os.getenv("TRANSLATOR_API_KEY")
TRANSLATOR_ENDPOINT = os.getenv("TRANSLATOR_ENDPOINT")
TRANSLATOR_LOCATION = os.getenv("TRANSLATOR_LOCATION")
