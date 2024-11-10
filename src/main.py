from scraper import extract_text
from translator import translate_article

# URL de exemplo
url = "https://dev.to/eric_dequ/steve-jobs-the-visionary-who-blended-spirituality-and-technology-3ppi"

# Extrai o texto da URL
text = extract_text(url)

if text:
    # Traduz o artigo para o português
    artigo = translate_article(text, "português")
    print(artigo)
