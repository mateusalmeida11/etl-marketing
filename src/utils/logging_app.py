import datetime
import logging


class LoggerAplication:
    def __init__(self, name):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.storage_logs = []
        self.logger = logging.getLogger(name=name)

    def _log(self, level, message):
        self.logger.log(level=level, message=message)
        dict_log = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": self.logger.name,
            "level": logging.getLevelName(level=level),
            "message": message,
        }
        self.storage_logs.append(dict_log)

    def info(self, message):
        self._log(logging.INFO, message)
