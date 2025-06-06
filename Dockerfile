# Playwright公式のDebianベースイメージを使う
FROM mcr.microsoft.com/playwright:focal

# 作業ディレクトリ作成＆移動
WORKDIR /app

# 必要ファイルをコピー
COPY . .

# Pythonの依存パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# コンテナ起動時に実行するコマンド
CMD ["python", "app.py"]
