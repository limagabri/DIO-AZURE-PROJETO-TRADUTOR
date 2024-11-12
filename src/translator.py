import requests
from config import API_KEY, OPENAI_ENDPOINT

def translate_article(text, lang):
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Você atua como tradutor de textos"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"traduza: {text} para o idioma {lang} e responda apenas com a tradução no formato markdown"
                    }
                ]
            },
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 900
    }
    
    ENDPOINT = OPENAI_ENDPOINT
    
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")
    
    return response.json()['choices'][0]['message']['content']
