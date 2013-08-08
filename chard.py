# -*- coding: utf-8 -*-
"""
    chard

    mongodb collection introspection. ish.

    one day it'll have like... structure.

    :requires: pymongo
    :copyright: uniphil 2013
    :license: dwtfyw. optionally buy me a coffee.
"""

from collections import OrderedDict


class NiceOD(OrderedDict):
    """A nice ordered dict. aka hashable and prints like a dict."""

    def __repr__(self):
        return dict.__repr__(self)

    def __hash__(self):
        return hash(str(self))


def _doc_to_schema(document, _recursed=False):
    """Sort by key and change values to types"""
    top_sorted = sorted(document.items(), key=lambda t: t[0])
    schema = NiceOD(top_sorted)
    for key, value in schema.items():
        if isinstance(value, dict):
            schema[key] = _doc_to_schema(value, True)
        else:
            schema[key] = type(value)
    return schema


def get_schema(documents):
    """get us a schemas"""
    schemas = {}  # lol the schema here is {hash: {schema: {}, count: int}}

    for doc in documents:
        schema = _doc_to_schema(doc)
        schema_hash = hash(schema)
        try:
            schemas[schema_hash]['count'] += 1
        except KeyError:
            template = {'schema': schema, 'count': 1}
            schemas[schema_hash] = template

    # return the most popular one. better, return the top ones with % matching
    return schemas


def get_nice_schema(collection):
    """stupid proxy for stdlib pprint"""
    from pprint import pprint
    schema = get_schema(collection)
    return pprint(schema)
