# ses-send
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

x = SESSend(config_file="/path/to/config")
x.send_email()

```

Will return `True` if the send was successful.
