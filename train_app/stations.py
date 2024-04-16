import json

# Open the JSON file
import json


def extract_values(data):
    if isinstance(data, dict):
        for value in data.values():
            yield from extract_values(value)
    elif isinstance(data, list):
        for item in data:
            yield from extract_values(item)
    else:
        yield data


def f():
    with open('stations.json') as file:
        contents = file.read()

    data = json.loads(contents)

    values = list(extract_values(data))

    print(values)


f()
