import requests
from utils.read_config import read_mf_config
from utils.logger import get_logger
import ast
import os


def lambda_handler(event, context):
    logger = get_logger()
    config = read_mf_config()
    url = config[ "api-url"]
    querystring = config["MutualFundFamily"]
    api_key = os.getenv('MF_API_KEY')
    headers = ast.literal_eval(config["header"].replace("{api_key}",str(api_key)))
    print(headers)
    for mf_family in querystring:
        response = requests.request("GET", url, headers=headers, params=mf_family)
    print(response.text)


lambda_handler(None, None)



