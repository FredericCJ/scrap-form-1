import requests
import logging

logging.basicConfig(filename="scrap.log", level=logging.INFO)


def request_handler(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.HTTPError as errh:
        logging.error(errh)
        return None
    except requests.ConnectionError as errc:
        logging.error(errc)
        return None
    except requests.Timeout as errt:
        logging.error(errt)
        return None
    except requests.RequestException as errr:
        logging.error(errr)
        return None


if __name__ == "__main__":
    response = request_handler("https://google.com")
    if response is not None:
        with open("scrapped/index.html", "w+") as f:
            f.write(response.text)
