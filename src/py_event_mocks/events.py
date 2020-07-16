#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Events creation module
"""

import json
import logging
from pathlib import Path

from mergedeep import merge, Strategy

logger = logging.getLogger(__name__)

SCRIPT_PATH = Path(__file__).parent.resolve()
EVENTS_JSON_PATH = SCRIPT_PATH / "events"


def create_event(event_type: str, body: dict = None) -> dict:
    """
    Return dict contents based on "event_type".

    Allowed value for "event_type":
        "aws:alexa-skill-event"
        "aws:alexa-smart-home-event"
        "aws:api-gateway-event"
        "aws:cloud-watch-event"
        "aws:cloud-watch-log-event"
        "aws:cognito-user-pool-event"
        "aws:dynamo-stream-event"
        "aws:kinesis"
        "aws:s3"
        "aws:scheduled"
        "aws:sns"
        "aws:sqs"

    :param event_type: Event type specification. i.e. "aws:s3", "aws:sns", ...
    :param body: Additional body which includes return value
    :return: Dict contents based on "event_type"
    """
    json_path = _event_type_to_json_path(event_type)
    with json_path.open() as fh:
        event = json.load(fh)
    merge(event, body or {}, strategy=Strategy.ADDITIVE)
    return event


def _event_type_to_json_path(event_type: str) -> Path:
    """
    Return .json file path for event_type
    :param event_type:
    :return: Path object for event-type JSON file
    """
    event_path_str = event_type.replace(":", "/") + "-template.json"
    return EVENTS_JSON_PATH / event_path_str
