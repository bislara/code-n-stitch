#!/usr/bin/env python3

import re
import html
import sys
from typing import List


def get_links(text: str) -> List[str]:
    """Extract all the links in the given text string

    Args:
        text (str): The text provided

    Returns:
        List[str]: List of http links
    """
    return [
        html.unescape("".join(item).strip("."))
        for item in re.findall(r'(http|https)(:\/\/)([^ \'"\s]*)', text)
    ]


if __name__ == "__main__":
    for link in get_links("".join(sys.argv[1:])):
        print(link)
