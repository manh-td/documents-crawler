import logging
import os
import csv
from .config import (
    PRODUCT,
    LOGS_DIR,
)
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
import json

log_file_path = os.path.join(LOGS_DIR, 'logs.log')
logging.basicConfig(
    force=True,
    level=logging.INFO if PRODUCT else logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
    ] if PRODUCT else [
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

def load_csv_to_dict_list(file_path):
    """
    Load a CSV file into a list of dictionaries.

    :param file_path: Path to the CSV file.
    :return: List of dictionaries where each dictionary represents a row in the CSV.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            return [row for row in reader]
    except Exception as e:
        logging.error(f"Failed to load CSV file: {e}")
        return []

def convert(html_content: str) -> str:
    logging.debug(f"Converting HTML to markdown ...")
    """Convert HTML content to markdown."""
    if html_content is None or html_content == '':
        return ''
    
    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    for element in soup.find_all(['picture', 'header', 'footer', 'nav', 'script', 'style', 'button']):
        element.decompose()

    # Convert to markdown
    markdown_content = MarkdownConverter().convert_soup(soup)
    logging.debug(f"Converted markdown content")
    return markdown_content

def write_list_of_dicts_to_jsonl(file_path, data):
    """
    Write a list of dictionaries to a JSONL (JSON Lines) file.

    :param file_path: Path to the JSONL file.
    :param data: List of dictionaries to write.
    """
    logging.debug(f"Writing list of dictionaries to JSONL file: {file_path}")
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            for item in data:
                file.write(json.dumps(item) + '\n')
        logging.info(f"Data successfully written to {file_path}")
    except Exception as e:
        logging.error(f"Failed to write to JSONL file {file_path}: {e}")