import os
from urllib.parse import urlencode

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from utils.logging_app import setup_logger

logger = setup_logger(name="etl_marketing")


class RequestError(Exception):
    pass


def build_url(base_url, endpoint, params):
    base_url += f"{endpoint}?"
    query_string = urlencode(params)
    base_url += query_string
    return base_url


def request(url, headers):
    retry_strategy = Retry(
        total=5,
        status_forcelist=[408, 429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        backoff_factor=2,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    try:
        response = http.get(url=url, headers=headers, timeout=30)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        raise RequestError(f"Erro na requisicao: {e}") from e


def offset_api(base_url, params, endpoint):
    bearer_token = os.getenv("BEARER_TOKEN_PERFIT")
    if not bearer_token:
        raise EnvironmentError("Token de Autenticacao Ausente")

    headers = {"Authorization": f"Bearer {bearer_token}"}
    url = build_url(base_url=base_url, endpoint=endpoint, params=params)
    raw_data = []

    while url:
        try:
            response = request(url=url, headers=headers)
            response = response.json()

            raw_data.append(response)
            url = response.get("paging", {}).get("next", None)
        except RequestError as e:
            logger.error(f"Erro ao fazer request {url}: {e}")
            raise

        except ValueError as e:
            logger.error(f"Erro no parsing do json: {e}")
            raise

        except Exception as e:
            logger.error(f"Erro inesperado durante processo de paginacao da API: {e}")
            raise

    return raw_data
