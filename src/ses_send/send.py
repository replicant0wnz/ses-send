#!/usr/bin/env python3

import yaml

from boto3 import client

class SESSend:
    """
    Wrapper for sending a notification email via AWS SES
    """

    def __init__(self, config_file="config.yaml"):

        self.config_file = config_file

    def _read_config(self):
        """
        Reads the yaml config file

        Keywords:
            config_file (string): Full path to config

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

        """
        config = self._read_config()

        ses_client = client("ses", region_name=config["region_name"])
        ses_client.send_email(
            Destination = config["destination"],
            Message = config["message"],
            Source = config["source"],
        )
