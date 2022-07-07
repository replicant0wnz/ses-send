# ses-send
![](https://github.com/replicant0wnz/ses-send/actions/workflows/release.yml/badge.svg)
[![Releases](https://img.shields.io/github/v/release/replicant0wnz/ses-send)](https://github.com/replicant0wnz/ses-send/releases)
[![Latest commit](https://img.shields.io/github/last-commit/replicant0wnz/ses-send)](https://github.com/replicant0wnz/ses-send/commits/main)
[![LICENSE](https://img.shields.io/github/license/replicant0wnz/ses-send)](https://github.com/replicant0wnz/ses-send/blob/main/LICENSE)

Simple wrapper to send emails via [AWS SES](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)

## Description

`ses-send` is a wrapper for the boto3 SES client. It allows the user to describe the email in a `yaml` configuration file instead of having to map it manually.

## Requirements

Module requirements are `boto3` and `yaml`. You must also have an SES identity already configured. 

## Installation

```bash
pip install ses-send
```

## Configuration example

```yaml
email:
  destination_address: youremail@gmail.com
  source_address: automation@yourdomain.com
  subject: Automation notification 
  message: This is a notification
aws:
  region: us-east-1
```

## Usage

```python3

from ses_send import SESSend

# You can omit the config_file keyword if you have config.yaml in the current path
x = SESSend(config_file="/path/to/config")
x.send_email()

```

Will return `True` if the send was successful.
