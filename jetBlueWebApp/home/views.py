from django.shortcuts import render
from fastai import *
from fastai.vision import *
import json

# Create your views here.
def home(request):
	return render(request,'index.html')

def availabilitybad(request):
	availableData = open('./staticfiles/availability.json').read()
	availableTweets = json.loads(availableData)

	learn = load_learner(".")

	for availableTweet in availableTweets:
		availableTweet["result"]=learn.predict(availableTweet["tweet"])[0]

		if (str(availableTweet["result"])=="neutral" or str(availableTweet["result"])=="positive"):
			availableTweets.remove(availableTweet)

	return render(request,'availabilitybad.html', context={"availableTweets":availableTweets})

def availabilitygood(request):
	availableData = open('./staticfiles/availability.json').read()
	availableTweets = json.loads(availableData)

	learn = load_learner(".")

	for availableTweet in availableTweets:
		availableTweet["result"]=learn.predict(availableTweet["tweet"])[0]

		if (str(availableTweet["result"])=="negative"):
			availableTweets.remove(availableTweet)

	return render(request,'availabilitygood.html', context={"availableTweets":availableTweets})

def costbad(request):
	costData = open('./staticfiles/cost.json').read()
	costTweets = json.loads(costData)

	learn = load_learner(".")

	for costTweet in costTweets:
		costTweet["result"]=learn.predict(costTweet["tweet"])[0]

		if (str(costTweet["result"])=="neutral" or str(costTweet["result"])=="positive"):
			costTweets.remove(costTweet)

	return render(request,'costbad.html', context={"costTweets":costTweets})

def costgood(request):
	costData = open('./staticfiles/cost.json').read()
	costTweets = json.loads(costData)

	learn = load_learner(".")

	for costTweet in costTweets:
		costTweet["result"]=learn.predict(costTweet["tweet"])[0]

		if (str(costTweet["result"])=="negative"):
			costTweets.remove(costTweet)

	return render(request,'costgood.html', context={"costTweets":costTweets})

def legroombad(request):
	legroomData = open('./staticfiles/legroom.json').read()
	legroomTweets = json.loads(legroomData)

	learn = load_learner(".")

	for legroomTweet in legroomTweets:
		legroomTweet["result"]=learn.predict(legroomTweet["tweet"])[0]

		if (str(legroomTweet["result"])=="neutral" or str(legroomTweet["result"])=="positive"):
			legroomTweets.remove(legroomTweet)

	return render(request,'legroombad.html', context={"legroomTweets":legroomTweets})

def legroomgood(request):
	legroomData = open('./staticfiles/legroom.json').read()
	legroomTweets = json.loads(legroomData)

	learn = load_learner(".")

	for legroomTweet in legroomTweets:
		legroomTweet["result"]=learn.predict(legroomTweet["tweet"])[0]

		if (str(legroomTweet["result"])=="negative"):
			legroomTweets.remove(legroomTweet)

	return render(request,'legroomgood.html', context={"legroomTweets":legroomTweets})

def timelinessbad(request):
	timeData = open('./staticfiles/time.json').read()
	timeTweets = json.loads(timeData)

	learn = load_learner(".")

	for timeTweet in timeTweets:
		timeTweet["result"]=learn.predict(timeTweet["tweet"])[0]

		if (str(timeTweet["result"])=="neutral" or str(timeTweet["result"])=="positive"):
			timeTweets.remove(timeTweet)

	return render(request,'timelinessbad.html', context={"timeTweets":timeTweets})

def timelinessgood(request):
	timeData = open('./staticfiles/time.json').read()
	timeTweets = json.loads(timeData)

	learn = load_learner(".")

	for timeTweet in timeTweets:
		timeTweet["result"]=learn.predict(timeTweet["tweet"])[0]

		if (str(timeTweet["result"])=="negative"):
			timeTweets.remove(timeTweet)

	return render(request,'timelinessgood.html', context={"timeTweets":timeTweets})