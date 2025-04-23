from .utils import (
    logging,
    load_csv_to_dict_list,
    convert,
    write_to_file,
)
from .config import OUTPUT_DIR
import requests
import os

def main(websites: list[dict]):
    for website in websites:
        response = requests.get(website["Websites"])
        website["html"] = response.text
        website["markdown"] = convert(website["html"])

        while True:
            i = 1
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            output_dir = os.path.join(OUTPUT_DIR, f"cwe-{website['CWE']}")
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f"document-{i}.md")
            if os.path.exists(output_file):
                i += 1
            else:
                write_to_file(output_file, website["markdown"])
                break

if __name__ == "__main__":
    data_path = "inputs/websites.csv"
    data = load_csv_to_dict_list(data_path)
    websites = [website for website in data if website.get("Websites")]
    main(websites)