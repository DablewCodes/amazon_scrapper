from query_reader import get_queries
from data_saver import export_data
from scraper import scrape_query_data
import time


def main():
    queries_list = get_queries()
    for query in queries_list:
        query_data = scrape_query_data(query)
        export_data(query, query_data)
        time.sleep(2)


if __name__ == '__main__':
    main()
