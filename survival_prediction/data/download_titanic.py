#!/usr/bin/env python3
"""Download a public Titanic dataset into survival_prediction/data/"""
import os
import requests

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
OUT_DIR = os.path.join(os.path.dirname(__file__))
OUT_PATH = os.path.join(OUT_DIR, 'titanic.csv')

os.makedirs(OUT_DIR, exist_ok=True)
print(f"Downloading dataset from {URL} -> {OUT_PATH}")
resp = requests.get(URL, timeout=30)
resp.raise_for_status()
with open(OUT_PATH, 'wb') as f:
    f.write(resp.content)
print('Done.')
