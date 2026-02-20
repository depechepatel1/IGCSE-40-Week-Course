import os

def test_week_01_exists():
    assert os.path.exists("Week_01.html"), "Week_01.html should exist"

def test_week_01_content():
    with open("Week_01.html", "r", encoding="utf-8") as f:
        content = f.read()

        # Check title and week
        assert "Week 1: Leisure & Free Time" in content

        # Check structure classes
        assert "floating-window" in content
        assert "cover-page" in content

        # Check specific content
        assert "couch‿potato" in content

        # Check Section 11 Update
        assert "Section 11. What did you learn today?" in content
        assert "Reflection:" in content

if __name__ == "__main__":
    test_week_01_exists()
    test_week_01_content()
    print("All tests passed!")
