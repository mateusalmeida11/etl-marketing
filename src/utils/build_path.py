import datetime

from zoneinfo import ZoneInfo


def build_path_storage(layer_name, source):
    tz = ZoneInfo("America/Sao_Paulo")
    current_date = datetime.datetime.now(tz=tz)
    base_path = f"{layer_name}/{source}/{current_date.year}/{current_date.month}/{current_date.day}"
    return base_path
