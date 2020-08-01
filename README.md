# py-event-mocks

Python implementation of [serverless / event-mocks](https://github.com/serverless/event-mocks)

A small library that includes details mocks of AWS Lambda event sources, same with original event-mocks.
Useful for use when unit testing your Lambda functions.
Supported Event Sources are:
- [x] API Gateway
- [x] SNS
- [x] SQS
- [x] DynamoDB
- [x] S3
- [x] Scheduled
- [x] Websocket
- [x] Alexa Skill
- [x] Alexa Smart Home
- [x] CloudWatch
- [x] CloudWatch Log
- [x] Cognito Pool
- [x] IoT
- [x] AWS Batch

The library simply uses default event source mock templates and merge it with any overwrite you provide. [Check out the JSON template files](src/py_event_mocks/events/aws) to learn more about the data structure of each event source.

## Set up

```bash
pip install py-event-mocks
```

## Usage

```python3
from py_event_mocks import create_event

event = create_event("aws:s3")

# event would be
#   {
#     "Records": [
#       {
#         "eventVersion": "2.0",
#         "eventSource": "aws:s3",
#         "awsRegion": "us-east-1",
#     ...
#   }
```

Allowed event_type (first parameter) is as follows:

- "aws:alexa-skill-event"
- "aws:alexa-smart-home-event"
- "aws:api-gateway-event"
- "aws:cloud-watch-event"
- "aws:cloud-watch-log-event"
- "aws:cognito-user-pool-event"
- "aws:dynamo-stream-event"
- "aws:kinesis"
- "aws:s3"
- "aws:scheduled"
- "aws:sns"
- "aws:sqs"

You can overwrite default template with "body" parameter.

```python3
event = create_event(
    event_type="aws:s3",
    body={
      "Records": [{
        "eventName": "ObjectCreated:Put",
        "s3": {
          "bucket": {
            "name": "my-bucket-name"
          },
          "object": {
            "key": "object-key"
          }
        }
      }]
    }
)
```
