import ast
import os
from datetime import datetime
from uuid import uuid4

import awswrangler as wr
import pandas as pd
import requests

from logger import get_logger
from read_config import read_mf_config


def handler(event, context):
    logger = get_logger()
    today = datetime.date()
    event_id = datetime.now().strftime('%Y%M%D%H%M%S-') + str(uuid4())
    try:
        config = read_mf_config()
        url = config["api-url"]
        querystring = config["MutualFundFamily"]
        api_key = os.getenv('MF_API_KEY')
        s3_bucket = config["s3-bucket"]
        headers = ast.literal_eval(
            config["header"].replace("{api_key}", str(api_key)))
        for mf_family in querystring:
            logger.info(f"started data ingestion for {mf_family} , event_id - {event_id}")
            response = requests.get(url, headers=headers, params=mf_family)
            mf_family = mf_family.replace(" ", "-")
            mf_df = pd.DataFrame(response.json())
            wr.s3.to_parquet(
                df=mf_df,
                path=f"s3://{s3_bucket}/{mf_family}/{today}/{event_id}/mf_data.parquet"
            )
            logger.info(f"completed data ingestion for {mf_family} , event_id - {event_id}")
    except Exception as e:
        logger.exception(f"event_id - {event_id}. handler() failed with exception - {e}")
