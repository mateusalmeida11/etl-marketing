import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


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
