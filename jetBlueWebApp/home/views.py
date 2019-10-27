from django.shortcuts import render
from fastai import *
from fastai.vision import *
import json

# Create your views here.
def home(request):
	timeData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/time.json').read()
	costData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/cost.json').read()
	legroomData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/legroom.json').read()
	availableData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/availability.json').read()
	timeTweets = json.loads(timeData)
	costTweets = json.loads(costData)
	legroomTweets = json.loads(legroomData)
	availableTweets = json.loads(availableData)

	learn = load_learner(".")

	for timeTweet in timeTweets:
		timeTweet["result"]=learn.predict(timeTweet["tweet"])[0]
	for costTweet in costTweets:
		costTweet["result"]=learn.predict(costTweet["tweet"])[0]
	for legroomTweet in legroomTweets:
		legroomTweet["result"]=learn.predict(legroomTweet["tweet"])[0]
	for availableTweet in availableTweets:
		availableTweet["result"]=learn.predict(availableTweet["tweet"])[0]

	return render(request,'index.html', context={"timeTweets":timeTweets, "costTweets":costTweets, "legroomTweets":legroomTweets, "availableTweets":availableTweets})
