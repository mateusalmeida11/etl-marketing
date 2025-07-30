import os
from urllib.parse import urlencode

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def build_url(base_url, endpoint, params):
    base_url += endpoint
    query_string = urlencode(params)
    base_url += query_string
    return base_url


def request(url, headers):
    retry_strategy = Retry(
        total=5,
        status_forcelist=[408, 429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        backoff_factor=120,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)
    response = http.get(url=url, headers=headers)
    return response


def offset_api(base_url, params, endpoint):
    bearer_token = os.getenv("BEARER_TOKEN_PERFIT")
    headers = {"Authorization": f"Bearer {bearer_token}"}
    url = build_url(base_url=base_url, endpoint=endpoint, params=params)
    raw_data = []
    while url:
        try:
            response = request(url=url, headers=headers)
            response = response.json()
            raw_data.append(response)
            url = response["paging"]["next"]
        except Exception:
            url = None

    return raw_data
