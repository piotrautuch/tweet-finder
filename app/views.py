from flask import render_template, flash
from app import scraping
from app import app
from .form import TweetKeyword

@app.route('/', methods=['GET','POST'])
def index():
    form = TweetKeyword()
    if form.validate_on_submit():
        return hello_tweet(fase=form.keyword.data)
    return render_template('index.html', error = False, form = form)

# Extracting tweets
def hello_tweet(fase):
    # Setting variables
    uniqueUsers = []    # List of all unique users
    results = []        # Final results
    data = scraping.getTweet(fase)
    # Checking if the data scraping was successful
    if data == None or data == []:
        return render_template('error.html', error = True, keyword = fase)
    # Setting the analysis variable
    analysis = {"Total favourites": 0,
                "Total retweets": 0,
                "Tweet count": len(data),
                "Verified users": 0}
    for status in data:
        # Adding the relevant data to the results
        results.append({'author': status.user.name, 'text': status.full_text,
             'datestamp': status.created_at, 'screen_name': status.user.screen_name,
             'source': status.source, 're_count': status.retweet_count})

        # Adding favourites count if given
        if status.favorite_count:
            results[-1]["favs"] = status.favorite_count
            analysis["Total favourites"] += status.favorite_count

        # Checking if the author is unique in the search query
        if results[-1]['author'] not in uniqueUsers:
            uniqueUsers.append(results[-1]['author'])
        # Checking if the tweet was a retweet
        if "RT" in status.full_text:
            #results[-1]['text'] = "RT " + status.retweeted_status.full_text
            analysis["Total retweets"] += 1

        if status.user.verified:
            analysis["Verified users"] += 1
    # Completing the analysis dictionary
    analysis["Number of unique users"] = len(uniqueUsers)
    analysis["Retweet percentage"] = str("%.2f" % ((analysis["Total retweets"]/len(results)) * 100)) + "%"
    print(analysis)
    return render_template('results.html', data=results, error = False, keyword = fase, analysis = analysis)
