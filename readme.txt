Please follow the steps to setup and run the project:

1. Install the python3 modules in the requirements.txt via pip
2. Setup MongoDB connection as both yelp review scrapper and flask web app uses this MongoDB as backend.
    a. Install MongoDB if you haven't done it.
    b. Create a database called "yelp"
    c. Create a collection called "yelp_review"
    d. Check and make sure the connection information located in the following path is setup correctly both flask web app and scrapper spider.
        i. flask web app: ./yelp_review_web/config/app_config.py
        ii. scrapper spider: ./yelp_review_scraper/yelp_review_crawler/yelp_review_crawler/settings.py
    e. Once MongoDB's up and running restore the MongoDB dump the running the following:
        mongodb_root/bin/mongorestore --collection collectionName --db myDB PathToDump/
3. To kick off the scraper, go to the following folder then run the following command:
    a. go to the folder: project_root/yelp_review_scraper/yelp_review_crawler/yelp_review_crawler/spiders
    b. type the following command (yelp_review is the name of the spider): scrapy crawl yelp_review
    c. The spider will perform upsert to mongodb collection
    d. For the sake of POC, I have hardcoded so the spider won't crawl longer than 10 pages of review list. To change this, go to the path below:
        i. go to: project_root/yelp_review_scraper/yelp_review_crawler/yelp_review_crawler/spiders
        ii. edit yelp_review.py -> change from PAGE_CUT_OFF = 10 to the desired page number.

4. To launch the flask web.
    a. go to the following in command prompt: projec_root/yelp_review_web
    b. command to launch flask web app: python app.py

5. Interacting with the flask web app.
    a. Input the pizza restaurant name and the number of reviews (from 1 to 100) to return.
    