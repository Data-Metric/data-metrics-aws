import requests
from read_config import read_mf_config
from logger import get_logger
import ast
import os


def handler(event, context):
    logger = get_logger()
    config = read_mf_config()
    url = config[ "api-url"]
    querystring = config["MutualFundFamily"]
    api_key = os.getenv('MF_API_KEY')
    headers = ast.literal_eval(config["header"].replace("{api_key}",str("054e8d7ecemsh51cc24b302f1999p135cf6jsn6ec3f7992da3")))
    print(headers)
    for mf_family in querystring:
        response = requests.request("GET", url, headers=headers, params=mf_family)
    print(response.text)



