# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.conf import settings


class MongoDBPipeline(object):
    """MongoDB Pipeline class for scrapy to insert crawled yelp reviews into mongodb to support the pizza review aggregator flask app. """
    def __init__(self):
        """Initialize connection"""
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']

        )
        db = connection[settings["MONGODB_DB"]]
        self.collection = db[settings["MONGODB_COLLECTION"]]

    def process_item(self, item, spider):
        """The process item method will take a crawled dictionary item and upsert them into mongodb collection"""
        item_dict = dict(item)
        self.collection.update({
            'pizza_name' : item_dict.get('pizza_name'),
            'reviewer_name' : item_dict.get('reviewer_name'),
            'review_date' : item_dict.get('review_date'),
            'reviewer_rating' : item_dict.get('reviewer_rating')

        },
            item_dict,
            True

        )

        return item
