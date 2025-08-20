import uuid

from src.utils.aws_s3 import S3
from src.utils.build_path import build_path_storage
from src.utils.get_request_api import offset_api


def lambda_handler(event, context):
    s3 = S3()
    unique_id = uuid.uuid4()
    unique_id_string = str(unique_id)
    layer_name = "bronze"
    source = "email"
    endpoint = "campaigns"

    params = {"offset": 0, "limit": 100, "sortby": "created", "sortdir": "asc"}

    url_base = "https://api.myperfit.com/v2/bepopu/"

    data = offset_api(base_url=url_base, params=params, endpoint=endpoint)

    path_storage = build_path_storage(layer_name=layer_name, source=source)

    file_name = f"campanhas_email_{unique_id_string}.json"

    s3.upload_file(data=data, folder=path_storage, file_name=file_name)

    return {
        "statusCode": 200,
        "message": f"Processo de etl da fonte: {source} camada: {layer_name} endpoint: {endpoint}",
    }
