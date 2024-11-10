# Usando uma imagem leve do Python
FROM python:3.12-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo requirements.txt para o container
COPY requirements.txt .

# Instalando as dependências listadas no requirements.txt
RUN pip install -r requirements.txt

# Copiando o código-fonte para o container
COPY src/ ./src/

# Expondo a porta que o Streamlit vai usar
EXPOSE 8501

# Comando para rodar o aplicativo usando Streamlit
CMD ["streamlit", "run", "src/app.py", "--server.address", "0.0.0.0"]

