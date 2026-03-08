import csv


def save_to_csv(data, file):

    keys = data[0].keys()

    with open(file, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=keys)

        writer.writeheader()

        writer.writerows(data)