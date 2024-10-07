"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""

import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/drug-use-by-age/drug-use-by-age.csv",
    file_path="/Users/chensi/Desktop/MIDS/Fall 2024/IDS 706/drug-use-by-age.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
