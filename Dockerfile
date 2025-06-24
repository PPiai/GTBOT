# Estágio 1: Definir a imagem base oficial do Python.
# Usamos a versão 'slim' por ser menor que a padrão, ideal para produção.
# Certifique-se de que a versão (ex: 3.9) é compatível com seu projeto.
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner.
# Todos os comandos seguintes serão executados a partir daqui.
WORKDIR /app

# Copia apenas o arquivo de dependências primeiro.
# Isso aproveita o cache do Docker: se o requirements.txt não mudar,
# o passo de instalação não será executado novamente, acelerando builds futuros.
COPY requirements.txt .

# Instala as dependências do Python.
# A flag --no-cache-dir reduz o tamanho final da imagem.
RUN pip install --no-cache-dir -r requirements.txt

# Agora, copia todos os outros arquivos do seu projeto para o diretório de trabalho (/app).
# Supondo que seu 'app.py' está dentro de uma pasta 'app'.
COPY . .

# Expõe a porta que o Streamlit usa.
# Isso informa ao Docker que o contêiner escuta nesta porta.
EXPOSE 8501

# O comando para iniciar a aplicação quando o contêiner é executado.
# Este comando é otimizado para rodar em um servidor/contêiner.
CMD [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]
