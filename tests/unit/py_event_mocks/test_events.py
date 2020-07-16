#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test__event_type_to_json_path():
    from py_event_mocks import events
    fp = events._event_type_to_json_path("aws:s3")
    assert fp.exists()


def test_create_event():
    import py_event_mocks

    r = py_event_mocks.create_event("aws:s3")
    assert "Records" in r

    r = py_event_mocks.create_event("aws:s3", {"foo": "bar"})
    assert "Records" in r
    assert "foo" in r

    r = py_event_mocks.create_event("aws:s3", {"Records": [{"foo": "bar"}]})
    assert "awsRegion" in r["Records"][0]
    assert "foo" in r["Records"][1]
