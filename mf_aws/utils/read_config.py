import json
from utils.logger import get_logger


def read_mf_config():
    logger = get_logger()
    try:
        with open("/var/task/mf_config.json") as mf_config_file:
            mf_config = json.load(mf_config_file)
        return mf_config
    except Exception as e:
        logger.exception(f"read_mf_config() failed with exception - {e}")
