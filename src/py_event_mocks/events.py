#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Events
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

    :param event_type:
    :param body:
    :return:
    """
    json_path = _event_type_to_json_path(event_type)
    with json_path.open() as fh:
        event = json.load(fh)
    merge(event, body or {}, strategy=Strategy.ADDITIVE)
    return event


def _event_type_to_json_path(event_type: str) -> Path:
    """

    :param event_type:
    :return:
    """
    event_path_str = event_type.replace(":", "/") + "-template.json"
    return EVENTS_JSON_PATH / event_path_str
