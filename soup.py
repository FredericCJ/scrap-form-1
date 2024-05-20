import requests
from bs4 import BeautifulSoup
from scrap import request_handler


def filter_soup(text):
    soup = BeautifulSoup(response.text, "html.parser")
    through_dom(soup)


def through_dom(element: BeautifulSoup, level=0):
    """return html opening tags in order

    Args:
        element (_type_): _description_
        level (int, optional): _description_. Defaults to 0.
    """
    if element.name:
        print(f"{' ' * level}<{element.name}>")

    if hasattr(element, "children"):
        for child in element.children:
            through_dom(child, level + 1)


if __name__ == "__main__":
    url = "http://books.toscrape.com/"
    response = request_handler(url)
    if response is not None:
        filter_soup(response.text)
