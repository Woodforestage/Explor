FROM mcr.microsoft.com/playwright:focal

# python環境セットアップなど必要ならここに追加
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
