# README #

## Online Tweet Finder ##
This is possibly my first major programming project.
It's a very basic tweet finder. A user types in a keyword. Using tweepy, the
application connects to the Twitter API and prints out the most recent tweets that
include the keyword.

## How to use it ##
1. Download the project files.
2. In the main folder, create a tweetapi.txt file.
3. In it, copy and paste your Twitter API credentials in the following order:
  - consumer key
  - consumer secret
  - access token
  - access token secret
4. Open the terminal and change the directory to the project folder.
5. Open the app using gunicorn ("gunicorn run:app") or just run the run.py file.

## To-do list ##
Possible aspects that could be implemented:
* Creating a stream and updating the results page with each newly posted tweet that includes the keyword.
* Emphasis on the data-science side of it - analysis of sources, hashtags, words associated with the keyword, etc.
* Comparing statistics for multiple search queries.
* Better CSS.

## Dependencies ##
This app uses the following packages:
* chardet
* click
* Flask
* Flask-WTF
* certifi
* gunicorn
* idna
* itsdangerous
* Jinja2
* MarkupSafe
* oauthlib
* pip
* requests
* requests-oauthlib
* setuptools
* six
* tweepy
* urllib3
* Werkzeug
* wheel
* WTForms
