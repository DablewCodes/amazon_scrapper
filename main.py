from query_reader import get_queries
from data_saver import export_data
from scraper import scrape_query_data


def main():
    print("\n ----------------Starting Scraping---------------- \n")
    queries_list = get_queries()
    for index, query in enumerate(queries_list, start=1):
        query_data = scrape_query_data(query)
        export_data(query, query_data)
        print("\nScraped data for query {}: {}".format(index, query))
        print("---------------------------------------------------------\n\n")


if __name__ == '__main__':
    main()
