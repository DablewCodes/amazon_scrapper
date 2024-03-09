from query_reader import get_queries
from data_saver import export_data
from scraper import scrape_query_data
import time


def main():
    queries_list = get_queries()
    for index, query in enumerate(queries_list):
        query_data = scrape_query_data(query)
        export_data(query, query_data)
        print("Scraped data for query {}: {}".format(index+1, query))
        time.sleep(1)


if __name__ == '__main__':
    main()
