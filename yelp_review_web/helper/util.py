import re

class Util():
	"""
	This class contains helper methods for the flask web app
	"""
	def make_searchable_name(self, input_name):
		"""This method will transform the passed in string by dropping
		 the punctuation via regular expression and lower case the result.
		 This approach is being applied via the scrapper as well as the flask web app at search time.

		 Args:
		 	input_name: typically pizza restaurant name

		Return:
			The return value is the string that's lower cased and with all punctuation removed.

		"""
		if input_name:
			return re.sub(r'[^\w\s]','',input_name.lower())
		else:
			return ""

	def get_avg_score(self, list_scores):
		"""
		This function takes a list of review scores and calculate the average review score.

		Args:
			list_scores: list of scores in float

		Return:
			calculated average score
		"""
		if len(list_scores) > 0:
			return round(sum(list_scores)/len(list_scores), 1)
		else:
			return 0
