from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from product import Product


def get_user_agents():
    with open("user_agents.txt", "r") as user_agents_file:
        return user_agents_file.read().split("\n")


def get_driver():
    options = Options()
    # set the user-agent
    user_agents = get_user_agents()
    options.add_argument(f"user-agent={user_agents[random.randint(1, 500)]}")
    options.add_argument(f"Accept-Language={'da, en-gb, en'}")
    options.add_argument(f"Accept-Encoding={'gzip, deflate, br'}")
    options.add_argument(
        f"Accept={'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}")
    options.add_argument(f"Referer={'https://www.google.com/'}")
    options.add_argument("--headless=new")

    # initialize the Chrome WebDriver with the specified options
    return webdriver.Chrome(options=options)


def scrape_query_data(query: str) -> list:
    query_data_list = []

    BASE_URL = "https://www.amazon.com/s?k={}"

    driver = get_driver()
    driver.set_page_load_timeout(30)

    try:
        driver.get(BASE_URL.format(query))
    except TimeoutException:
        print("Driver took too long to load the webpage, Check your internet connection and try again")
        quit()

    query_page_html = driver.page_source

    driver.close()

    soup = BeautifulSoup(query_page_html, features="lxml")

    # Loop to account for number of product cards on the page
    for i in range(2, 25):

        product_div = soup.find("div", {"data-component-type": "s-search-result", "data-index": i})

        if product_div is None:
            continue

        title_div = product_div.findNext("div", {"data-cy": "title-recipe"})
        title_text = title_div.text

        lines_to_remove = ["Featured from Amazon brands", "Sponsored",
                           "You’re seeing this ad based on the product’s relevance to your search query.",
                           "You’re seeing this ad based on the product’s relevance to your search query",
                           "Leave ad feedback"]
        for line in lines_to_remove:
            title_text = title_text.replace(line, "")
        product_title = title_text.strip()

        reviews_div = product_div.findNext("span", {"data-component-type": "s-client-side-analytics"})
        if reviews_div is not None:
            product_total_reviews = reviews_div.findNext("span").text
        else:
            product_total_reviews = "Reviews Unavailable"

        price_div = product_div.findNext("div", {"data-cy": "price-recipe"})
        if price_div.text.lower() == "Click to see price".lower():
            product_price = "Price concealed"
        else:
            try:
                product_price = price_div.text.split("$")[1].strip()
            except IndexError:
                product_price = price_div.text.strip()

        image_src = product_div.find_all_next("img")
        product_img = str(image_src[0]["src"]).strip()

        product = Product(product_title, product_total_reviews, product_price, product_img)

        query_data_list.append(product)

    return query_data_list
