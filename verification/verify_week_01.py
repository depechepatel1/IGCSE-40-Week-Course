from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("file:///app/Week_01.html")

    # Wait for content
    try:
        page.wait_for_selector("text=IGCSE / IELTS Speaking Course", timeout=5000)
    except Exception as e:
        print(f"Error loading page: {e}")
        browser.close()
        return

    # Check locators
    yellow_count = page.locator('mark[style="background-color: yellow;"]').count()
    blue_count = page.locator('span[style="color: blue;"]').count()

    print(f"Yellow marks found: {yellow_count}")
    print(f"Blue spans found: {blue_count}")

    # Screenshot
    page.screenshot(path="verification/verification.png", full_page=True)
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
