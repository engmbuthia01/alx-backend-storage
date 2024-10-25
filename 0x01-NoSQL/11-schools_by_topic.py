#!/usr/bin/env python3
"""
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of dictionaries representing the matching schools.
    """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    finds by topic
    """
    return mongo_collection.find({"topics": topic})
