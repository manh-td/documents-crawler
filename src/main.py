from .utils import (
    logging,
    load_csv_to_dict_list,
    convert,
    write_list_of_dicts_to_jsonl
)
from .config import OUTPUT_DIR
import requests
import os

def main(websites: list[dict]) -> list[dict]:
    for website in websites:
        response = requests.get(website["Websites"])
        website["markdown"] = convert(response.text)
    return websites

if __name__ == "__main__":
    data_path = "inputs/websites.csv"
    data = load_csv_to_dict_list(data_path)
    websites = [website for website in data if website.get("Websites")]
    websites = main(websites)
    write_list_of_dicts_to_jsonl(
        os.path.join(OUTPUT_DIR, "websites.jsonl"),
        websites
    )