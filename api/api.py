
import requests
import json
import config
import praw
from flask import Flask
from functools import reduce
from weather_helpers import extract_weather_data
from traffic_helpers import extract_travel_time
from calendar_event_helpers import extract_calendar_data

app = Flask(__name__)

ORLANDO_COORD_STR = '28.5383,-81.3792'
WEATHER_QUERY_PARAMS = '?exclude=minutely,daily,alerts,flags'
TRAFFIC_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
TRAFFIC_SOURCE = '28.5383,-81.3792'
TRAFFIC_DEST = '28.597240,-81.203796'

@app.route("/api/weather")
def weather():
    r = requests.get('https://api.darksky.net/forecast/{}/{}{}'.format(config.darksky_key, ORLANDO_COORD_STR, WEATHER_QUERY_PARAMS))
    return json.dumps(extract_weather_data(r.json()))

@app.route("/api/news")
def news():
    return "This will return data fetched via News API"

@app.route("/api/reddit")
def reddit():
    # Using authorized mode!
    reddit = praw.Reddit(client_id=config.client_id,client_secret=config.secret_client,user_agent=config.usr_agent,username=config.usr_name, password=config.reddit_ps)
    ucfReddit = reddit.subreddit('UCF')
    showerThoughts = reddit.subreddit('Showerthoughts')

    # Grab 5 stories from showerThoughts
    for submission in showerThoughts.hot(limit=5):
        redditTitles.append(submission.title)

    # Grab 5 stories from UCF 	
    for submission in showerThoughts.hot(limit=5):
        redditTitles.append(submission.title)

    # Return json dumped version of this dictionary
    json_string = json.dumps(redditTitles)
    return json_string
    
@app.route("/api/quote")
def quote():
    r = requests.get('http://quotes.rest/qod.json?category=inspire&maxlength=300') 
    data = r.json()
    daQuote = data['contents']['quotes'][0]['quote']
    return json.dumps(daQuote)
    
@app.route("/api/traffic")
def traffic():
    r = requests.get('{}origins={}&destinations={}&key={}'.format(TRAFFIC_URL, TRAFFIC_SOURCE, TRAFFIC_DEST, config.maps_key)) 
    return json.dumps(extract_travel_time(r.json()))

@app.route("/api/calendar")
def calendar():
    pass
    #r = requests.get(https://webcourses.ucf.edu/feeds/calendars/user_QlbM3tYdBowXoTbbzfgUiy7cYb39WTcBzkEDCWUU.ics)

    # TODO: Error checking
    #return json.dumps(extract_calendar_data(r))
