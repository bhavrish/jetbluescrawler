from django.shortcuts import render
from .models import AvailabilityBadModel, AvailabilityGoodModel, CostBadModel, CostGoodModel, LegroomBadModel, LegroomGoodModel, TimelinessBadModel, TimelinessGoodModel
import datetime
import json
import twint
import requests

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

	for availableTweet in availableTweets[:]:
		r = requests.post("https://api.deepai.org/api/sentiment-analysis",
    				data={'text': availableTweet["tweet"]},
    				headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
		resultJSON = r.json()
		resultOutput = resultJSON['output']
		score = 0
		for x in resultOutput:
			if x == "Negative":
				score-=1
			elif x == "Positive":
				score+=1
			
		if score >= 0: # if positive or neutral, remove tweet
			availableTweets.remove(availableTweet)
		else: # if negative, keep it
			availableTweet["result"]="negative"
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

	for availableTweet in availableTweets[:]:
		r = requests.post("https://api.deepai.org/api/sentiment-analysis",
    				data={'text': availableTweet["tweet"]},
    				headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
		resultJSON = r.json()
		resultOutput = resultJSON['output']
		score = 0
		for x in resultOutput:
			if x == "Negative":
				score-=1
			elif x == "Positive":
				score+=1
			
		if score >= 0: # if positive or neutral, keep tweet
			availableTweet["result"]="positive"
			oldDate = str(availableTweet["date"])
			oldDateList = oldDate.split("/")
			newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
			newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

			availabilityGoodObject=AvailabilityGoodModel(name=str(availableTweet["username"]),text=str(availableTweet["tweet"]),date=newDate,prediction_level=str(availableTweet["result"]))
			availabilityGoodObject.save()
		else: # if negative, remove it
			availableTweets.remove(availableTweet)

	return render(request,'availabilitygood.html', context={"availableTweets":availableTweets})

def costbad(request):
	costData = open('./staticfiles/cost.json').read()
	costTweets = json.loads(costData)

	for costTweet in costTweets[:]:
		r = requests.post("https://api.deepai.org/api/sentiment-analysis",
    				data={'text': costTweet["tweet"]},
    				headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
		resultJSON = r.json()
		resultOutput = resultJSON['output']
		score = 0
		for x in resultOutput:
			if x == "Negative":
				score-=1
			elif x == "Positive":
				score+=1
			
		if score >= 0: # if positive or neutral, remove tweet
			costTweets.remove(costTweet)
		else: # if negative, keep it
			costTweet["result"]="negative"
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

	for costTweet in costTweets[:]:
		r = requests.post("https://api.deepai.org/api/sentiment-analysis",
    				data={'text': costTweet["tweet"]},
    				headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
		resultJSON = r.json()
		resultOutput = resultJSON['output']
		score = 0
		for x in resultOutput:
			if x == "Negative":
				score-=1
			elif x == "Positive":
				score+=1
		
		if score >= 0: # if positive or neutral, keep tweet
			costTweet["result"]="positive"
			oldDate = str(costTweet["date"])
			oldDateList = oldDate.split("/")
			newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
			newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

			costGoodObject=CostGoodModel(name=str(costTweet["username"]),text=str(costTweet["tweet"]),date=newDate,prediction_level=str(costTweet["result"]))
			costGoodObject.save()
		else: # if negative, remove it
			costTweets.remove(costTweet)

	return render(request,'costgood.html', context={"costTweets":costTweets})

def legroombad(request):
	legroomData = open('./staticfiles/legroom.json').read()
	legroomTweets = json.loads(legroomData)

	for legroomTweet in legroomTweets[:]:
		r = requests.post("https://api.deepai.org/api/sentiment-analysis",
    				data={'text': legroomTweet["tweet"]},
    				headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
		resultJSON = r.json()
		resultOutput = resultJSON['output']
		score = 0
		for x in resultOutput:
			if x == "Negative":
				score-=1
			elif x == "Positive":
				score+=1
			
		if score >= 0: # if positive or neutral, remove tweet
			legroomTweets.remove(legroomTweet)
		else: # if negative, keep it
			legroomTweet["result"]="negative"
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

	for legroomTweet in legroomTweets[:]:
		r = requests.post("https://api.deepai.org/api/sentiment-analysis",
    				data={'text': legroomTweet["tweet"]},
    				headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
		resultJSON = r.json()
		resultOutput = resultJSON['output']
		score = 0
		for x in resultOutput:
			if x == "Negative":
				score-=1
			elif x == "Positive":
				score+=1
		
		if score >= 0: # if positive or neutral, keep tweet
			legroomTweet["result"]="positive"
			oldDate = str(legroomTweet["date"])
			oldDateList = oldDate.split("/")
			newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
			newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

			legroomGoodObject=LegroomGoodModel(name=str(legroomTweet["username"]),text=str(legroomTweet["tweet"]),date=newDate,prediction_level=str(legroomTweet["result"]))
			legroomGoodObject.save()
		else: # if negative, remove it
			legroomTweets.remove(legroomTweet)

	return render(request,'legroomgood.html', context={"legroomTweets":legroomTweets})

def timelinessbad(request):
	timeData = open('./staticfiles/time.json').read()
	timeTweets = json.loads(timeData)

	for timeTweet in timeTweets[:]:
		r = requests.post("https://api.deepai.org/api/sentiment-analysis",
    				data={'text': timeTweet["tweet"]},
    				headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
		resultJSON = r.json()
		resultOutput = resultJSON['output']
		score = 0
		for x in resultOutput:
			if x == "Negative":
				score-=1
			elif x == "Positive":
				score+=1
			
		if score >= 0: # if positive or neutral, remove tweet
			timeTweets.remove(timeTweet)
		else: # if negative, keep it
			timeTweet["result"]="negative"
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

	for timeTweet in timeTweets[:]:
		r = requests.post("https://api.deepai.org/api/sentiment-analysis",
    				data={'text': timeTweet["tweet"]},
    				headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
		resultJSON = r.json()
		resultOutput = resultJSON['output']
		score = 0
		for x in resultOutput:
			if x == "Negative":
				score-=1
			elif x == "Positive":
				score+=1
		
		if score >= 0: # if positive or neutral, keep tweet
			timeTweet["result"]="positive"
			oldDate = str(timeTweet["date"])
			oldDateList = oldDate.split("/")
			newDateStr = "20" + oldDateList[2] + "-" + oldDateList[0] + "-" + oldDateList[1]
			newDate=datetime.datetime.strptime(newDateStr, "%Y-%m-%d").date()

			timelinessGoodObject=TimelinessGoodModel(name=str(timeTweet["username"]),text=str(timeTweet["tweet"]),date=newDate,prediction_level=str(timeTweet["result"]))
			timelinessGoodObject.save()
		else: # if negative, remove it
			timeTweets.remove(timeTweet)

	return render(request,'timelinessgood.html', context={"timeTweets":timeTweets})
