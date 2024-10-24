#!/usr/bin/env python3
"""
    Inserts a new document in the collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: key-value pairs representing the document fields.

    Returns:
        The new document's _id.
    """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert one document based on kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
