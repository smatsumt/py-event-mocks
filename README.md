# py-event-mocks

Python implementation of [serverless / event-mocks](https://github.com/serverless/event-mocks)

## Set up

```bash
pip install py-event-mocks
```

## Usage

```python3
from py_event_mocks import create_event

event = create_event("aws:s3")
# return 
#   {
#     "Records": [
#       {
#         "eventVersion": "2.0",
#         "eventSource": "aws:s3",
#         "awsRegion": "us-east-1",
#     ...
#   }

event = create_event(
    "aws:s3",
    {
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
