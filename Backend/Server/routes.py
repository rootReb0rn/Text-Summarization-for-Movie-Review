from flask import render_template, url_for, flash, redirect, request, jsonify, config
from Server import app,db
from Server.model import Review
from Server.text_preprocessing import expand_contractions,remove_special_characters,strip_html_tags
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

db.create_all()

def InsertReview(movie,review):
    if review != None:
        print("Database\t: Processing")
        insert_review = Review(movie=movie,review=review)
        db.session.add(insert_review)
        db.session.commit()
        print("Database\t: Completed")

def Summarization(review):
    if review != None:
        print("Text PreProcessing\t: Processing")
        # Text PreProcessing
        review = review.lower()
        review = strip_html_tags(review)
        review = expand_contractions(review)
        review = remove_special_characters(review)
        tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
        model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
        tokens = tokenizer(review, truncation=True, padding="longest", return_tensors="pt")
        summary = model.generate(**tokens)
        get_summary = tokenizer.decode(summary[0])
        print("Text PreProcessing\t: Completed")
        return get_summary

def DisplayReview(movie):
    return Review.query.filter_by(movie=movie).all()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/movie1', methods=['POST', 'GET'])
def movie1():
    if request.method == "POST":
        movie = request.form['movie-name']
        review = request.form['my-review']
        get_summary_review = Summarization(review=review)
        InsertReview(movie=movie,review=get_summary_review)
        print(movie)
        print(review)
    display_review = DisplayReview(movie="1")
    return render_template("movie1.html",display_review=display_review)

@app.route('/movie2', methods=['POST', 'GET'])
def movie2():
    if request.method == "POST":
        movie = request.form['movie-name']
        review = request.form['my-review']
        get_summary_review = Summarization(review=review)
        InsertReview(movie=movie,review=get_summary_review)
        print(movie)
        print(review)
    display_review = DisplayReview(movie="2")

    return render_template("movie2.html",display_review=display_review)

@app.route('/movie3', methods=['POST', 'GET'])
def movie3():
    if request.method == "POST":
        movie = request.form['movie-name']
        review = request.form['my-review']
        get_summary_review = Summarization(review=review)
        InsertReview(movie=movie,review=get_summary_review)
        print(movie)
        print(review)
    display_review = DisplayReview(movie="3")
    return render_template("movie3.html",display_review=display_review)

@app.route('/movie4', methods=['POST', 'GET'])
def movie4():
    if request.method == "POST":
        movie = request.form['movie-name']
        review = request.form['my-review']
        get_summary_review = Summarization(review=review)
        InsertReview(movie=movie,review=get_summary_review)
        print(movie)
        print(review)
    display_review = DisplayReview(movie="4")
    return render_template("movie4.html",display_review=display_review)

@app.route('/movie5', methods=['POST', 'GET'])
def movie5():
    if request.method == "POST":
        movie = request.form['movie-name']
        review = request.form['my-review']
        get_summary_review = Summarization(review=review)
        InsertReview(movie=movie,review=get_summary_review)
        print(movie)
        print(review)
        display_review = DisplayReview(movie="5")
    return render_template("movie5.html",display_review=display_review)