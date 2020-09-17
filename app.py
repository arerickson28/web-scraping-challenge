import scrape_mars
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:####/mars_database"

mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars_database
    return render_template('index.html', mars = mars)



@app.route("/scrape")
def scrape():
    mars = mongo.db.mars_database
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert = True)
    return "scraping complete"




if __name__ == "__main__":
    app.run(debug=True)