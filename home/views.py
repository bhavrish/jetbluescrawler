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

def availabilitybad(request):
	availableTweets = []
	for line in open('./AvailabilityTweets/tweets.json', 'r'):
		availableTweets.append(json.loads(line))

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
			newDate=datetime.datetime.strptime(str(availableTweet["date"]), "%Y-%m-%d").date()

			availabilityBadObject=AvailabilityBadModel(name=str(availableTweet["username"]),text=str(availableTweet["tweet"]),date=newDate,prediction_level=str(availableTweet["result"]))
			availabilityBadObject.save()

	return render(request,'availabilitybad.html', context={"availableTweets":availableTweets})

def availabilitygood(request):
	availableTweets = []
	for line in open('./AvailabilityTweets/tweets.json', 'r'):
		availableTweets.append(json.loads(line))

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
			newDate=datetime.datetime.strptime(str(availableTweet["date"]), "%Y-%m-%d").date()

			availabilityGoodObject=AvailabilityGoodModel(name=str(availableTweet["username"]),text=str(availableTweet["tweet"]),date=newDate,prediction_level=str(availableTweet["result"]))
			availabilityGoodObject.save()
		else: # if negative, remove it
			availableTweets.remove(availableTweet)

	return render(request,'availabilitygood.html', context={"availableTweets":availableTweets})

def costbad(request):
	costTweets = []
	for line in open('./CostTweets/tweets.json', 'r'):
		costTweets.append(json.loads(line))

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
			newDate=datetime.datetime.strptime(str(costTweet["date"]), "%Y-%m-%d").date()

			costBadObject=CostBadModel(name=str(costTweet["username"]),text=str(costTweet["tweet"]),date=newDate,prediction_level=str(costTweet["result"]))
			costBadObject.save()

	return render(request,'costbad.html', context={"costTweets":costTweets})

def costgood(request):
	costTweets = []
	for line in open('./CostTweets/tweets.json', 'r'):
		costTweets.append(json.loads(line))

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
			newDate=datetime.datetime.strptime(str(costTweet["date"]), "%Y-%m-%d").date()

			costGoodObject=CostGoodModel(name=str(costTweet["username"]),text=str(costTweet["tweet"]),date=newDate,prediction_level=str(costTweet["result"]))
			costGoodObject.save()
		else: # if negative, remove it
			costTweets.remove(costTweet)

	return render(request,'costgood.html', context={"costTweets":costTweets})

def legroombad(request):
	legroomTweets = []
	for line in open('./LegroomTweets/tweets.json', 'r'):
		legroomTweets.append(json.loads(line))

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
			newDate=datetime.datetime.strptime(str(legroomTweet["date"]), "%Y-%m-%d").date()

			legroomBadObject=LegroomBadModel(name=str(legroomTweet["username"]),text=str(legroomTweet["tweet"]),date=newDate,prediction_level=str(legroomTweet["result"]))
			legroomBadObject.save()

	return render(request,'legroombad.html', context={"legroomTweets":legroomTweets})

def legroomgood(request):
	legroomTweets = []
	for line in open('./LegroomTweets/tweets.json', 'r'):
		legroomTweets.append(json.loads(line))

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
			newDate=datetime.datetime.strptime(str(legroomTweet["date"]), "%Y-%m-%d").date()

			legroomGoodObject=LegroomGoodModel(name=str(legroomTweet["username"]),text=str(legroomTweet["tweet"]),date=newDate,prediction_level=str(legroomTweet["result"]))
			legroomGoodObject.save()
		else: # if negative, remove it
			legroomTweets.remove(legroomTweet)

	return render(request,'legroomgood.html', context={"legroomTweets":legroomTweets})

def timelinessbad(request):
	timeTweets = []
	for line in open('./TimeTweets/tweets.json', 'r'):
		timeTweets.append(json.loads(line))

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
			newDate=datetime.datetime.strptime(str(timeTweet["date"]), "%Y-%m-%d").date()

			timelinessBadObject=TimelinessBadModel(name=str(timeTweet["username"]),text=str(timeTweet["tweet"]),date=newDate,prediction_level=str(timeTweet["result"]))
			timelinessBadObject.save()

	return render(request,'timelinessbad.html', context={"timeTweets":timeTweets})

def timelinessgood(request):
	timeTweets = []
	for line in open('./TimeTweets/tweets.json', 'r'):
		timeTweets.append(json.loads(line))

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
			newDate=datetime.datetime.strptime(str(timeTweet["date"]), "%Y-%m-%d").date()

			timelinessGoodObject=TimelinessGoodModel(name=str(timeTweet["username"]),text=str(timeTweet["tweet"]),date=newDate,prediction_level=str(timeTweet["result"]))
			timelinessGoodObject.save()
		else: # if negative, remove it
			timeTweets.remove(timeTweet)

	return render(request,'timelinessgood.html', context={"timeTweets":timeTweets})

def cardio(request):
	return render(request, 'cardio.html')
