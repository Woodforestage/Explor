from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
        page = browser.new_page()
        page.goto("https://example.com")
        print(page.title())
        browser.close()

if __name__ == "__main__":
    main()
