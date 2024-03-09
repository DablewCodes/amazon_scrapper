from datetime import date


class Product:
    def __init__(self, title, total_reviews, price, image_url):
        self.title = title
        self.total_reviews = total_reviews
        self.price = price
        self.image_url = image_url
        self.scrape_date = date.today()

    def __str__(self):
        return f"{self.title} has total reviews: {self.total_reviews}, price: {self.price}, and image url: {self.image_url} on date: {self.scrape_date}"
