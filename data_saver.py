import json


def export_data(query: str, query_data: list) -> None:
    try:
        query_data_file = open("output_data/{}.json".format(query), "x")
    except FileExistsError:
        query_data_file = open("output_data/{}.json".format(query), "w")

    json_string = json.dumps([data_item.__dict__ for data_item in query_data])
    query_data_file.write(json_string)
    query_data_file.close()
