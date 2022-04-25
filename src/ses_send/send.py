#!/usr/bin/env python3

import yaml

from boto3 import client
from botocore.exceptions import ClientError


class SESSend:
    """
    Wrapper for sending a notification email via AWS SES
    """

    def __init__(self, config_file="config.yaml"):
        """
        Keywords:
            config_file (str): Full path to config
        """

        self.config_file = config_file

    def _read_config(self):
        """
        Reads the yaml config file

        Returns:
            config (dict)
        """

        config = {}

        f = open(self.config_file)

        config_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)

        config["destination"] = {
            "ToAddresses": [config_yaml["email"]["destination_address"]]
        }
        config["message"] = {
            "Body": {
                "Text": {"Data": config_yaml["email"]["message"]},
            },
            "Subject": {"Data": config_yaml["email"]["subject"]},
        }
        config["source"] = config_yaml["email"]["source_address"]
        config["region_name"] = config_yaml["aws"]["region"]

        return config

    def send_email(self):
        """
        Sends the email

        Returns:
            True (bool): If successful
        """

        config = self._read_config()

        ses_client = client("ses", region_name=config["region_name"])
        try:
            ses_client.send_email(
                Destination=config["destination"],
                Message=config["message"],
                Source=config["source"],
            )

        except ClientError as e:
            raise Exception(e.response["Error"]["Message"])

        return True
