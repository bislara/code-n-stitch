from typing import Optional
import unittest

from links import get_links

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


class LinkTests(unittest.TestCase):
    def test_get_links(self):
        text = read_file('text.txt')
        self.assertEqual(
            ["http://www.example.org/bag.aspx", "http://example.com/bat.html"],
            get_links(text),
        )

    def test_get_links_code(self):
        text = read_file('code.js')
        self.assertEqual(
            [
                "https://stackoverflow.com/a/57804949",
                "http://www.google.com",
                "http://www.mylink.com",
                "http://www.yourlink.com",
                "http://www.test.com",
                "http://www.facebook.com",
            ],
            get_links(text),
        )


if __name__ == "__main__":
    unittest.main()
