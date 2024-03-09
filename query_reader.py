import json


def get_queries() -> list:
    try:
        with open("user_queries.json", "r") as queries_file:
            queries_str = queries_file.read()

    except FileNotFoundError:
        print("queries.json file wasn't found in the script root directory, exiting")
        exit()

    return list(json.loads(queries_str))
