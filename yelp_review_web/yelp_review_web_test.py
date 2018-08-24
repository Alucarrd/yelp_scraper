
from services.yelp_review_service import Yelp_Review_Service
from helper.util import Util
import pytest

"""Unit test file"""

@pytest.fixture
def my_util_object():
    util = Util()
    return util

@pytest.fixture
def my_service_object():
    my_service = Yelp_Review_Service()
    return my_service



def test_make_searchable_name_standard(my_util_object):
    """unit test for make_searchable_name that cleans up punctuations and lower case the string"""
    original_name = "Juliana’s Pizza,"
    converted_name = "julianas pizza"
    assert my_util_object.make_searchable_name(original_name) == converted_name

def test_make_searchable_name_empty(my_util_object):
    """unit test for make_searchable_name when None object's passed in"""
    original_name = None
    converted_name = ""
    assert my_util_object.make_searchable_name(original_name) == converted_name

def test_get_avg_score_empty_list(my_util_object):
    """unit test for get_avg_score when an empty list is passed in"""
    my_empty_list_of_scores = []
    assert my_util_object.get_avg_score(my_empty_list_of_scores) == 0.0

def test_get_avg_score_scores_list(my_util_object):
    """unit test for get_avg_score when a list of scores (float) is passed in"""
    my_list_of_scores = [5.0, 4.0, 3.0, 2.0]
    assert my_util_object.get_avg_score(my_list_of_scores) == 3.5

def test_get_search_result(my_service_object):
    """unit test to test a valid search that should return one result assume there are scrapped data"""
    pizza_name = "Juliana’s Pizza"
    review_count = 1
    review_list, review_score = my_service_object.get_search_result(pizza_name, review_count)
    assert len(review_list) == 1


