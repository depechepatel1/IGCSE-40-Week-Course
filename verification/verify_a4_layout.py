import os
from playwright.sync_api import sync_playwright

def run():
    file_path = os.path.abspath("Week_01.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Launch page with full viewport to capture everything
        page = browser.new_page(viewport={'width': 1000, 'height': 9000})
        page.goto(f"file://{file_path}")

        # 1. Check there are exactly 7 A4 pages
        pages = page.locator(".a4-page")
        count = pages.count()
        print(f"Found {count} .a4-page elements")
        assert count == 7, f"Expected 7 A4 pages, found {count}"

        # 2. Check Page 1 is Cover Page
        page1 = pages.nth(0)
        classes = page1.get_attribute("class")
        assert "cover-page" in classes, "Page 1 should have class 'cover-page'"
        # Check for title
        title_text = page1.locator("h1").inner_text()
        print(f"Page 1 Title: {title_text}")
        assert "IGCSE / IELTS" in title_text, "Page 1 title incorrect"

        # 3. Check Page 2 is Notes Page
        page2 = pages.nth(1)
        assert page2.locator(".notes-window").count() > 0, "Page 2 should contain a .notes-window"
        text2 = page2.inner_text()
        assert "intentionally left blank" not in text2, "Page 2 should NOT mention 'intentionally left blank'"

        # 4. Check Page 3 is Lesson Plan
        page3 = pages.nth(2)
        text3 = page3.inner_text()
        assert "QTS Aligned Teacher Lesson Plan" in text3, "Page 3 should be the Lesson Plan"

        # 5. Check Page 4 contains Sections 1-3
        page4 = pages.nth(3)
        assert page4.locator("h4", has_text="Section 1. Weekly Grammar Point").count() > 0, "Page 4 should contain Section 1"
        assert page4.locator("h4", has_text="Section 3. Vocabulary Table").count() > 0, "Page 4 should contain Section 3"
        assert page4.locator("h4", has_text="Section 4").count() == 0, "Page 4 should NOT contain Section 4"

        # 6. Check Page 5 contains Sections 4-6
        page5 = pages.nth(4)
        assert page5.locator("h4", has_text="Section 4. Warm-Up Questions").count() > 0, "Page 5 should contain Section 4"
        assert page5.locator("h4", has_text="Section 6. Circuit Prompt & Spider Diagram").count() > 0, "Page 5 should contain Section 6"
        assert page5.locator("h4", has_text="Section 7").count() == 0, "Page 5 should NOT contain Section 7"

        # 7. Check Page 6 contains Sections 7-9
        page6 = pages.nth(5)
        assert page6.locator("h4", has_text="Section 7. Model Answer").count() > 0, "Page 6 should contain Section 7"
        assert page6.locator("h4", has_text="Section 9. Listener Task").count() > 0, "Page 6 should contain Section 9"
        assert page6.locator("h4", has_text="Section 10").count() == 0, "Page 6 should NOT contain Section 10"

        # 8. Check Page 7 contains Sections 10-13
        page7 = pages.nth(6)
        assert page7.locator("h4", has_text="Section 10. Differentiation Stretch").count() > 0, "Page 7 should contain Section 10"
        assert page7.locator("h4", has_text="Section 13. Post-Homework Task").count() > 0, "Page 7 should contain Section 13"

        # 9. Check Dimensions (approximate)
        box = page1.bounding_box()
        print(f"Page dimensions: {box['width']}x{box['height']}")

        # Allow some float tolerance
        assert 790 <= box['width'] <= 800, f"Page width {box['width']} is not close to 210mm (approx 794px)"
        # Use >= 1120 because min-height is 297mm
        assert box['height'] >= 1120, f"Page height {box['height']} is less than 297mm (approx 1123px)"

        # Take a screenshot
        page.screenshot(path="verification/verification_a4.png", full_page=True)
        print("Verification successful and screenshot saved to verification/verification_a4.png")

        browser.close()

if __name__ == "__main__":
    run()