from flask import Flask, render_template, request
from services.yelp_review_service import Yelp_Review_Service
from helper.util import Util
"""Flask Web App File"""

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# define the route

@app.route("/", methods=['GET', 'POST'])
def home():
    """
    Home page method for the pizza aggregator app.

    """
    # template file needs to be under "templates" folder.
    is_post = False
    review_list = []
    avg_score = 0
    name = ""
    count = ""
    pizza_info = {}
    review_size = 0
    if request.method == 'POST':
        my_util = Util()
        is_post = True

        my_review_service = Yelp_Review_Service()
        name = request.form['name']
        count = int(request.form['count'])
        review_list, my_score_list = my_review_service.get_search_result(name, count)

        if len(review_list) > 0:
            pizza_info = {
                'pizza_name': review_list[0].get('pizza_name'),
                'pizza_phone': review_list[0].get('pizza_phone'),
                'pizza_address': review_list[0].get('pizza_address'),
            }

        avg_score = my_util.get_avg_score(my_score_list)
        review_size = len(review_list)

    return render_template("home.html", review_size=review_size, pizza_info=pizza_info, review_list=review_list,
                           is_post=is_post, avg_score=avg_score, name=name, count=count)


if __name__ == "__main__":
    app.run(debug=True)

