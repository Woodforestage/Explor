from flask import Flask
from playwright.sync_api import sync_playwright
import os

app = Flask(__name__)

@app.route("/")
def check_playwright():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
            page = browser.new_page()
            page.goto("https://example.com")
            title = page.title()
            browser.close()
        return f"Playwright started successfully! Page title: {title}"
    except Exception as e:
        return f"Playwright failed to start: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
