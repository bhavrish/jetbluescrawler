from django.shortcuts import render
from fastai import *
from fastai.vision import *
import json

# Create your views here.
def home(request):
	return render(request,'index.html')

def availabilitybad(request):
	availableData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/availability.json').read()
	availableTweets = json.loads(availableData)

	learn = load_learner(".")

	for availableTweet in availableTweets:
		availableTweet["result"]=learn.predict(availableTweet["tweet"])[0]

	return render(request,'availabilitybad.html', context={"availableTweets":availableTweets})

def availabilitygood(request):
	availableData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/availability.json').read()
	availableTweets = json.loads(availableData)

	learn = load_learner(".")

	for availableTweet in availableTweets:
		availableTweet["result"]=learn.predict(availableTweet["tweet"])[0]

	return render(request,'availabilitygood.html', context={"availableTweets":availableTweets})

def costbad(request):
	costData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/cost.json').read()
	costTweets = json.loads(costData)

	learn = load_learner(".")

	for costTweet in costTweets:
		costTweet["result"]=learn.predict(costTweet["tweet"])[0]

	return render(request,'costbad.html', context={"costTweets":costTweets})

def costgood(request):
	costData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/cost.json').read()
	costTweets = json.loads(costData)

	learn = load_learner(".")

	for costTweet in costTweets:
		costTweet["result"]=learn.predict(costTweet["tweet"])[0]

	return render(request,'costgood.html', context={"costTweets":costTweets})

def legroombad(request):
	legroomData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/legroom.json').read()
	legroomTweets = json.loads(legroomData)

	learn = load_learner(".")

	for legroomTweet in legroomTweets:
		legroomTweet["result"]=learn.predict(legroomTweet["tweet"])[0]

	return render(request,'legroombad.html', context={"legroomTweets":legroomTweets})

def legroomgood(request):
	legroomData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/legroom.json').read()
	legroomTweets = json.loads(legroomData)

	learn = load_learner(".")

	for legroomTweet in legroomTweets:
		legroomTweet["result"]=learn.predict(legroomTweet["tweet"])[0]

	return render(request,'legroomgood.html', context={"legroomTweets":legroomTweets})

def timelinessbad(request):
	timeData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/time.json').read()
	timeTweets = json.loads(timeData)

	learn = load_learner(".")

	for timeTweet in timeTweets:
		timeTweet["result"]=learn.predict(timeTweet["tweet"])[0]

	return render(request,'timelinessbad.html', context={"timeTweets":timeTweets})

def timelinessgood(request):
	timeData = open('/Users/bhaveshshah/Desktop/jetblue/jetBlueWebApp/staticfiles/time.json').read()
	timeTweets = json.loads(timeData)

	learn = load_learner(".")

	for timeTweet in timeTweets:
		timeTweet["result"]=learn.predict(timeTweet["tweet"])[0]

	return render(request,'timelinessgood.html', context={"timeTweets":timeTweets})