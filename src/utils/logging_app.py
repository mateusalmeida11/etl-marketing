import logging


class LoggerAplication:
    def __init__(self, name):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.storage_logs = []
        self.logger = logging.getLogger(name=name)
