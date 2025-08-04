import requests

def get_custom_data(endpoint, query):
    res = requests.post(endpoint, json={"query": query})
    return res.json()
