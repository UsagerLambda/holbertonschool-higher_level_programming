import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            data = [line for line in reader]

            json_data = json.dumps(data)

        with open("data.json", "w") as jsonfile:
            jsonfile.write(json_data)

        return True

    except FileNotFoundError:
        print("File not found.")
        return False
