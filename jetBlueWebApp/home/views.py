from django.shortcuts import render
from fastai import *
from fastai.vision import *
from .models import AvailabilityBadModel, AvailabilityGoodModel, CostBadModel, CostGoodModel, LegroomBadModel, LegroomGoodModel, TimelinessBadModel, TimelinessGoodModel
import datetime
import json
import twint

# Create your views here.
def home(request):
	return render(request,'index.html')

def react(request):
        return render(request, 'react.html')

def pullRealtimeAvailTweets():
	c = twint.Config()
	c.Search = "#jetblue #availability"
	c.Limit = 5
	c.Store_object = True
	twint.run.Search(c)
	availableTweets = twint.output.tweets_list
	return availableTweets

def availabilitybad(request):
	#availableTweets=pullRealtimeAvailTweets()

	availableData = open('./staticfiles/availability.json').read()
	availableTweets = json.loads(availableData)

	learn = load_learner(".")

	for availableTweet in availableTweets:
		availableTweet["result"]=learn.predict(availableTweet["tweet"])[0]

		if (str(availableTweet["result"])=="neutral" or str(availableTweet["result"])=="positive"):
			availableTweets.remove(availableTweet)

		oldDate = str(availableTweet["date"])
		oldDateList = oldDate.split("/")
		newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
		newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

		availabilityBadObject=AvailabilityBadModel(name=str(availableTweet["username"]),text=str(availableTweet["tweet"]),date=newDate,prediction_level=str(availableTweet["result"]))
		availabilityBadObject.save()

	return render(request,'availabilitybad.html', context={"availableTweets":availableTweets})

def availabilitygood(request):
	availableData = open('./staticfiles/availability.json').read()
	availableTweets = json.loads(availableData)

	learn = load_learner(".")

	for availableTweet in availableTweets:
		availableTweet["result"]=learn.predict(availableTweet["tweet"])[0]

		if (str(availableTweet["result"])=="negative"):
			availableTweets.remove(availableTweet)

		oldDate = str(availableTweet["date"])
		oldDateList = oldDate.split("/")
		newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
		newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

		availabilityGoodObject=AvailabilityGoodModel(name=str(availableTweet["username"]),text=str(availableTweet["tweet"]),date=newDate,prediction_level=str(availableTweet["result"]))
		availabilityGoodObject.save()

	return render(request,'availabilitygood.html', context={"availableTweets":availableTweets})

def costbad(request):
	costData = open('./staticfiles/cost.json').read()
	costTweets = json.loads(costData)

	learn = load_learner(".")

	for costTweet in costTweets:
		costTweet["result"]=learn.predict(costTweet["tweet"])[0]

		if (str(costTweet["result"])=="neutral" or str(costTweet["result"])=="positive"):
			costTweets.remove(costTweet)

		oldDate = str(costTweet["date"])
		oldDateList = oldDate.split("/")
		newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
		newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

		costBadObject=CostBadModel(name=str(costTweet["username"]),text=str(costTweet["tweet"]),date=newDate,prediction_level=str(costTweet["result"]))
		costBadObject.save()

	return render(request,'costbad.html', context={"costTweets":costTweets})

def costgood(request):
	costData = open('./staticfiles/cost.json').read()
	costTweets = json.loads(costData)

	learn = load_learner(".")

	for costTweet in costTweets:
		costTweet["result"]=learn.predict(costTweet["tweet"])[0]

		if (str(costTweet["result"])=="negative"):
			costTweets.remove(costTweet)

		oldDate = str(costTweet["date"])
		oldDateList = oldDate.split("/")
		newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
		newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

		costGoodObject=CostGoodModel(name=str(costTweet["username"]),text=str(costTweet["tweet"]),date=newDate,prediction_level=str(costTweet["result"]))
		costGoodObject.save()

	return render(request,'costgood.html', context={"costTweets":costTweets})

def legroombad(request):
	legroomData = open('./staticfiles/legroom.json').read()
	legroomTweets = json.loads(legroomData)

	learn = load_learner(".")

	for legroomTweet in legroomTweets:
		legroomTweet["result"]=learn.predict(legroomTweet["tweet"])[0]

		if (str(legroomTweet["result"])=="neutral" or str(legroomTweet["result"])=="positive"):
			legroomTweets.remove(legroomTweet)

		oldDate = str(legroomTweet["date"])
		oldDateList = oldDate.split("/")
		newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
		newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

		legroomBadObject=LegroomBadModel(name=str(legroomTweet["username"]),text=str(legroomTweet["tweet"]),date=newDate,prediction_level=str(legroomTweet["result"]))
		legroomBadObject.save()

	return render(request,'legroombad.html', context={"legroomTweets":legroomTweets})

def legroomgood(request):
	legroomData = open('./staticfiles/legroom.json').read()
	legroomTweets = json.loads(legroomData)

	learn = load_learner(".")

	for legroomTweet in legroomTweets:
		legroomTweet["result"]=learn.predict(legroomTweet["tweet"])[0]

		if (str(legroomTweet["result"])=="negative"):
			legroomTweets.remove(legroomTweet)

		oldDate = str(legroomTweet["date"])
		oldDateList = oldDate.split("/")
		newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
		newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

		legroomGoodObject=LegroomGoodModel(name=str(legroomTweet["username"]),text=str(legroomTweet["tweet"]),date=newDate,prediction_level=str(legroomTweet["result"]))
		legroomGoodObject.save()

	return render(request,'legroomgood.html', context={"legroomTweets":legroomTweets})

def timelinessbad(request):
	timeData = open('./staticfiles/time.json').read()
	timeTweets = json.loads(timeData)

	learn = load_learner(".")

	for timeTweet in timeTweets:
		timeTweet["result"]=learn.predict(timeTweet["tweet"])[0]

		if (str(timeTweet["result"])=="neutral" or str(timeTweet["result"])=="positive"):
			timeTweets.remove(timeTweet)

		oldDate = str(timeTweet["date"])
		oldDateList = oldDate.split("/")
		newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
		newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

		timelinessBadObject=TimelinessBadModel(name=str(timeTweet["username"]),text=str(timeTweet["tweet"]),date=newDate,prediction_level=str(timeTweet["result"]))
		timelinessBadObject.save()

	return render(request,'timelinessbad.html', context={"timeTweets":timeTweets})

def timelinessgood(request):
	timeData = open('./staticfiles/time.json').read()
	timeTweets = json.loads(timeData)

	learn = load_learner(".")

	for timeTweet in timeTweets:
		timeTweet["result"]=learn.predict(timeTweet["tweet"])[0]

		if (str(timeTweet["result"])=="negative"):
			timeTweets.remove(timeTweet)

		oldDate = str(timeTweet["date"])
		oldDateList = oldDate.split("/")
		newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
		newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

		timelinessGoodObject=TimelinessGoodModel(name=str(timeTweet["username"]),text=str(timeTweet["tweet"]),date=newDate,prediction_level=str(timeTweet["result"]))
		timelinessGoodObject.save()

	return render(request,'timelinessgood.html', context={"timeTweets":timeTweets})
