import scrape_mars
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_database"

mongo = PyMongo(app)

@app.route("/")
def index():
    mars_scrape_results = mongo.db.mars_database
    return render_template('index.html', mars_html = mars_scrape_results)



@app.route("/scrape")
def scrape():
    mars_scrape_results = mongo.db.mars_database

    mars_data = scrape_mars.scrape()

    mars_scrape_results.update({}, mars_data, upsert = True)
    
    return "scraping complete"




if __name__ == "__main__":
    app.run(debug=True)