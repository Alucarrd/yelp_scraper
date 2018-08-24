import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config.app_config import MONGODB_SERVER, MONGODB_PORT, MONGODB_DB
from helper.util import Util

class Yelp_Review_Service():
	"""
	This is the main service class to serve scraped review data from mongoDB.

	"""
	_client = None
	_collection = None


	def __init__(self):
		"""constructor that initializes object properties"""
		self.__db = None
		self.__client = None
		self.__util = Util()

	def set_database(self):
		"""This method opens connection to mongodb and set the database"""
		self.__client = MongoClient(MONGODB_SERVER, MONGODB_PORT, maxPoolSize=50)
		self.__db = self.__client[MONGODB_DB]

	def check_connection(self):
		"""
		This is the check connection method that will throw exception when there's
		problem connecting to mongodb instance
		"""
		try:
			# The ismaster command is cheap and does not require auth.
			self.set_database()
			self.__client.admin.command('ismaster')
			return True
		except ConnectionFailure:
			return False

	def get_search_result(self, pizza_name, num_reviews):
		"""
		The get_search_result method will take in search name, transform the name into searchable name, and send through the mongodb find query.
		The result set will be sorted by review time and the size will be limited to passed in value.

		Args:
			pizza_name: passed in search name for the pizza restaurant
			num_reviews: the review size to return from mongoDB
		Returns:
			This method returns a tuple of two lists.
				1. list of reviews
				2. list of review scores
		"""
		if self.check_connection():

			query = {
				'searchable_name' : self.__util.make_searchable_name(pizza_name)
			}
			sort_field = 'review_date_unix'
			rows = list(self.__db.yelp_review.find(query).sort(sort_field, pymongo.DESCENDING).limit(num_reviews))
			score_list = [row.get("reviewer_rating") for row in rows]
			return rows, list(score_list)
		else:
			return [], []






	
