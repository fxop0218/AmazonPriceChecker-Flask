import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

AMZN_NF_TITLE = "Amazon.com Page Not Found in title"


# Check if the url exists
# If the url doesn't exist the page return error != 200
def check_existence(url):
    result = requests.get(url)
    if result.status_code != 404:
        session = HTMLSession()
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            title = soup.find(id="productTitle").text
            print(title)
        except Exception as attr:
            return False

        if title is None or len(title) == 0:
            return False
        return True
    else:
        return False


def scrap_product(url):
    if check_existence(url):
        print("Correct link")
        session = HTMLSession()
        product_dict = dict()
        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            product_dict["title"] = soup.find(id="productTitle").text.strip()
            product_dict["price"] = soup.find(class_="a-price-whole").text
            product_dict["price"] = product_dict["price"] + soup.find(class_="a-price-fraction").text
            strs = soup.find(class_="a-icon-alt").text
            product_dict["strs"] = strs.replace("de 5 estrellas", "")  # Delete the first part of the stars text
            product_dict["url"] = url
            session.close()
            return product_dict
        except AttributeError as attrError:
            return None

    else:
        # If the link doesn't work, return None
        return None
