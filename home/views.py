from django.shortcuts import render
from .models import JetblueAggregateModel, JetblueCondensedModel, AmericanAggregateModel, AmericanCondensedModel, UnitedAggregateModel, UnitedCondensedModel, SpiritAggregateModel, SpiritCondensedModel
import requests

from datetime import datetime

# Home endpoint
def home(request):
	airlineInfoList = [
	{'modelObjects': JetblueCondensedModel.objects.all(), 'name': "JETBLUE", 'imageURL': 'https://images.unsplash.com/photo-1576128343868-ba0ea33570a6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&q=80&crop=edges&ar=96:69'},
	{'modelObjects': AmericanCondensedModel.objects.all(), 'name': "AMERICAN", 'imageURL': 'https://images.unsplash.com/photo-1532973497172-04b34d604825?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1341&q=80&ar=96:69'},
	{'modelObjects': UnitedCondensedModel.objects.all(), 'name': "UNITED", 'imageURL': 'https://images.unsplash.com/photo-1473862170180-84427c485aca?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80&ar=96:69'},
	{'modelObjects': SpiritCondensedModel.objects.all(), 'name': "SPIRIT", 'imageURL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Spirit_Airlines_Airbus_A321-231_N677NK_approaching_Newark_Airport.jpg/1280px-Spirit_Airlines_Airbus_A321-231_N677NK_approaching_Newark_Airport.jpg'}
	]

	for airline in airlineInfoList:
		modelObjects = ['modelObjects']

		OverallDict = {}
		AvailabilityDict = {}
		CostDict = {}
		LegroomDict = {}
		TimeDict = {}
		BaggageFeesDict = {}
		HiddenFeesDict = {}
		ConnectionsDict = {}
		FamilyOptionsDict = {}
		FoodEntertainmentDict = {}
		ReimbursementDict = {}
		ServiceDict = {}
		TravelRewardsDict = {}
		
		# iterate over condensed objects and filter each object into respective category dictionary
		for modelObject in modelObjects:
			modelObject.date = modelObject.date.strftime("%m/%d/%Y")
			if modelObject.category == 'availability':
				AvailabilityDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'cost':
				CostDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'legroom':
				LegroomDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'timeliness':
				TimeDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'baggage-fees':
				BaggageFeesDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'hidden-fees':
				HiddenFeesDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'connections':
				ConnectionsDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'family-options':
				FamilyOptionsDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'food-entertainment':
				FoodEntertainmentDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'reimbursement':
				ReimbursementDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'service':
				ServiceDict[modelObject.date] = modelObject.average_prediction
			elif modelObject.category == 'travel-rewards':
				TravelRewardsDict[modelObject.date] = modelObject.average_prediction
			
			if modelObject.date in OverallDict:
				OverallDict[modelObject.date] += modelObject.average_prediction
			else:
				OverallDict[modelObject.date] = modelObject.average_prediction

		# update category scores and overall scores
		AvailabilitySum = 0
		AvailabilityScore = 0
		for date in AvailabilityDict:
			AvailabilitySum += AvailabilityDict[date]
		if not len(AvailabilityDict) == 0:
			AvailabilityScore = AvailabilitySum / (len(AvailabilityDict))

		CostSum = 0
		CostScore = 0
		for date in CostDict:
			CostSum += CostDict[date]
		if not len(CostDict) == 0:	
			CostScore = CostSum / (len(CostDict))

		LegroomSum = 0
		LegroomScore = 0
		for date in LegroomDict:
			LegroomSum += LegroomDict[date]
		if not len(LegroomDict) == 0:
			LegroomScore = LegroomSum / (len(LegroomDict))

		TimeSum = 0
		TimeScore = 0
		for date in TimeDict:
			TimeSum += TimeDict[date]
		if not len(TimeDict) == 0:
			TimeScore = TimeSum / (len(TimeDict))
		
		BaggageFeesSum = 0
		BaggageFeesScore = 0
		for date in BaggageFeesDict:
			BaggageFeesSum += BaggageFeesDict[date]
		if not len(BaggageFeesDict) == 0:
			BaggageFeesScore = BaggageFeesSum / (len(BaggageFeesDict))

		HiddenFeesSum = 0
		HiddenFeesScore = 0
		for date in HiddenFeesDict:
			HiddenFeesSum += HiddenFeesDict[date]
		if not len(HiddenFeesDict) == 0:
			HiddenFeesScore = HiddenFeesSum / (len(HiddenFeesDict))

		ConnectionsSum = 0
		ConnectionsScore = 0
		for date in ConnectionsDict:
			ConnectionsSum += ConnectionsDict[date]
		if not len(ConnectionsDict) == 0:
			ConnectionsScore = ConnectionsSum / (len(ConnectionsDict))

		FamilyOptionsSum = 0
		FamilyOptionsScore = 0
		for date in FamilyOptionsDict:
			FamilyOptionsSum += FamilyOptionsDict[date]
		if not len(FamilyOptionsDict) == 0:
			FamilyOptionsScore = FamilyOptionsSum / (len(FamilyOptionsDict))

		FoodEntertainmentSum = 0
		FoodEntertainmentScore = 0
		for date in FoodEntertainmentDict:
			FoodEntertainmentSum += FoodEntertainmentDict[date]
		if not len(FoodEntertainmentDict) == 0:
			FoodEntertainmentScore = FoodEntertainmentSum / (len(FoodEntertainmentDict))

		ReimbursementSum = 0
		ReimbursementScore = 0
		for date in ReimbursementDict:
			ReimbursementSum += ReimbursementDict[date]
		if not len(ReimbursementDict) == 0:
			ReimbursementScore = ReimbursementSum / (len(ReimbursementDict))

		ServiceSum = 0
		ServiceScore = 0
		for date in ServiceDict:
			ServiceSum += ServiceDict[date]
		if not len(ServiceDict) == 0:
			ServiceScore = ServiceSum / (len(ServiceDict))

		TravelRewardsSum = 0
		TravelRewardsScore = 0
		for date in TravelRewardsDict:
			TravelRewardsSum += TravelRewardsDict[date]
		if not len(TravelRewardsDict) == 0:
			TravelRewardsScore = TravelRewardsSum / (len(TravelRewardsDict))

		OverallScore = (AvailabilityScore + CostScore + LegroomScore + TimeScore + BaggageFeesScore + HiddenFeesScore + ConnectionsScore + FamilyOptionsScore + FoodEntertainmentScore + ReimbursementScore + ServiceScore + TravelRewardsScore)/12
		
		airline['OverallScore'] = OverallScore
		airline['AvailabilityScore'] = AvailabilityScore
		airline['CostScore'] = CostScore
		airline['LegroomScore'] = LegroomScore
		airline['TimeScore'] = TimeScore
		airline['BaggageFeesScore'] = BaggageFeesScore
		airline['HiddenFeesScore'] = HiddenFeesScore
		airline['ConnectionsScore'] = ConnectionsScore
		airline['FamilyOptionsScore'] = FamilyOptionsScore
		airline['FoodEntertainmentScore'] = FoodEntertainmentScore
		airline['ReimbursementScore'] = ReimbursementScore
		airline['ServiceScore'] = ServiceScore
		airline['TravelRewardsScore'] = TravelRewardsScore

		airline['OverallTweetsDict'] = OverallDict
		airline['AvailabilityDict'] = AvailabilityDict
		airline['CostDict'] = CostDict
		airline['LegroomDict'] = LegroomDict
		airline['TimeDict'] = TimeDict
		airline['BaggageFeesDict'] = BaggageFeesDict
		airline['HiddenFeesDict'] = HiddenFeesDict
		airline['ConnectionsDict'] = ConnectionsDict
		airline['FamilyOptionsDict'] = FamilyOptionsDict
		airline['FoodEntertainmentDict'] = FoodEntertainmentDict
		airline['ReimbursementDict'] = ReimbursementDict
		airline['ServiceDict'] = ServiceDict
		airline['TravelRewardsDict'] = TravelRewardsDict


	return render(request,'index.html', {'airlineInfoList':airlineInfoList})

def react(request):
        return render(request, 'react.html')


# ------------------------------------------ JetBlue ------------------------------------------
def availabilitybad(request):
	tweets = JetblueAggregateModel.objects.all()
	negativeAvailableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability' and tweet.prediction_level < 0:
			negativeAvailableTweets.append(tweet)

	return render(request, 'availabilitybad.html', {'availableTweets':negativeAvailableTweets, 'title':'JetBlue'})
	
def availabilitygood(request):
	tweets = JetblueAggregateModel.objects.all()
	positiveAvailableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability' and tweet.prediction_level >= 0:
			positiveAvailableTweets.append(tweet)

	return render(request, 'availabilitygood.html', {'availableTweets':positiveAvailableTweets, 'title':'JetBlue'})

def costbad(request):
	tweets = JetblueAggregateModel.objects.all()
	negativeCostTweets = []

	for tweet in tweets:
		if tweet.category == 'cost' and tweet.prediction_level < 0:
			negativeCostTweets.append(tweet)

	return render(request, 'costbad.html', {"costTweets":negativeCostTweets, 'title':'JetBlue'})

def costgood(request):
	tweets = JetblueAggregateModel.objects.all()
	positiveCostTweets = []

	for tweet in tweets:
		if tweet.category == 'cost' and tweet.prediction_level >= 0:
			positiveCostTweets.append(tweet)

	return render(request, 'costgood.html', {"costTweets":positiveCostTweets, 'title':'JetBlue'})

def legroombad(request):
	tweets = JetblueAggregateModel.objects.all()
	negativeLegroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom' and tweet.prediction_level < 0:
			negativeLegroomTweets.append(tweet)

	return render(request, 'legroombad.html', {'legroomTweets':negativeLegroomTweets, 'title':'JetBlue'})

def legroomgood(request):
	tweets = JetblueAggregateModel.objects.all()
	positiveLegroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom' and tweet.prediction_level >= 0:
			positiveLegroomTweets.append(tweet)

	return render(request, 'legroomgood.html', {'legroomTweets':positiveLegroomTweets, 'title':'JetBlue'})

def timelinessbad(request):
	tweets = JetblueAggregateModel.objects.all()
	negativeTimeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness' and tweet.prediction_level < 0:
			negativeTimeTweets.append(tweet)

	return render(request, 'timelinessbad.html', {"timeTweets":negativeTimeTweets, 'title':'JetBlue'})

def timelinessgood(request):
	tweets = JetblueAggregateModel.objects.all()
	positiveTimeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness' and tweet.prediction_level >= 0:
			positiveTimeTweets.append(tweet)

	return render(request, 'timelinessgood.html', {"timeTweets":positiveTimeTweets, 'title':'JetBlue'})


# ------------------------------------------ American Airlines ------------------------------------------
def americanavailabilitybad(request):
	tweets = AmericanAggregateModel.objects.all()
	negativeAvailableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability' and tweet.prediction_level < 0:
			negativeAvailableTweets.append(tweet)

	return render(request, 'availabilitybad.html', {'availableTweets':negativeAvailableTweets, 'title':'American Airlines'})
	
def americanavailabilitygood(request):
	tweets = AmericanAggregateModel.objects.all()
	positiveAvailableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability' and tweet.prediction_level >= 0:
			positiveAvailableTweets.append(tweet)

	return render(request, 'availabilitygood.html', {'availableTweets':positiveAvailableTweets, 'title':'American Airlines'})

def americancostbad(request):
	tweets = AmericanAggregateModel.objects.all()
	negativeCostTweets = []

	for tweet in tweets:
		if tweet.category == 'cost' and tweet.prediction_level < 0:
			negativeCostTweets.append(tweet)

	return render(request, 'costbad.html', {"costTweets":negativeCostTweets, 'title':'American Airlines'})

def americancostgood(request):
	tweets = AmericanAggregateModel.objects.all()
	positiveCostTweets = []

	for tweet in tweets:
		if tweet.category == 'cost' and tweet.prediction_level >= 0:
			positiveCostTweets.append(tweet)

	return render(request, 'costgood.html', {"costTweets":positiveCostTweets, 'title':'American Airlines'})

def americanlegroombad(request):
	tweets = AmericanAggregateModel.objects.all()
	negativeLegroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom' and tweet.prediction_level < 0:
			negativeLegroomTweets.append(tweet)

	return render(request, 'legroombad.html', {'legroomTweets':negativeLegroomTweets, 'title':'American Airlines'})

def americanlegroomgood(request):
	tweets = AmericanAggregateModel.objects.all()
	positiveLegroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom' and tweet.prediction_level >= 0:
			positiveLegroomTweets.append(tweet)

	return render(request, 'legroomgood.html', {'legroomTweets':positiveLegroomTweets, 'title':'American Airlines'})

def americantimelinessbad(request):
	tweets = AmericanAggregateModel.objects.all()
	negativeTimeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness' and tweet.prediction_level < 0:
			negativeTimeTweets.append(tweet)

	return render(request, 'timelinessbad.html', {"timeTweets":negativeTimeTweets, 'title':'American Airlines'})

def americantimelinessgood(request):
	tweets = AmericanAggregateModel.objects.all()
	positiveTimeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness' and tweet.prediction_level >= 0:
			positiveTimeTweets.append(tweet)

	return render(request, 'timelinessgood.html', {"timeTweets":positiveTimeTweets, 'title':'American Airlines'})

# ------------------------------------------ United Airlines ------------------------------------------
def unitedavailabilitybad(request):
	tweets = UnitedAggregateModel.objects.all()
	negativeAvailableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability' and tweet.prediction_level < 0:
			negativeAvailableTweets.append(tweet)

	return render(request, 'availabilitybad.html', {'availableTweets':negativeAvailableTweets, 'title':'United Airlines'})
	
def unitedavailabilitygood(request):
	tweets = UnitedAggregateModel.objects.all()
	positiveAvailableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability' and tweet.prediction_level >= 0:
			positiveAvailableTweets.append(tweet)

	return render(request, 'availabilitygood.html', {'availableTweets':positiveAvailableTweets, 'title':'United Airlines'})

def unitedcostbad(request):
	tweets = UnitedAggregateModel.objects.all()
	negativeCostTweets = []

	for tweet in tweets:
		if tweet.category == 'cost' and tweet.prediction_level < 0:
			negativeCostTweets.append(tweet)

	return render(request, 'costbad.html', {"costTweets":negativeCostTweets, 'title':'United Airlines'})

def unitedcostgood(request):
	tweets = UnitedAggregateModel.objects.all()
	positiveCostTweets = []

	for tweet in tweets:
		if tweet.category == 'cost' and tweet.prediction_level >= 0:
			positiveCostTweets.append(tweet)

	return render(request, 'costgood.html', {"costTweets":positiveCostTweets, 'title':'United Airlines'})

def unitedlegroombad(request):
	tweets = UnitedAggregateModel.objects.all()
	negativeLegroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom' and tweet.prediction_level < 0:
			negativeLegroomTweets.append(tweet)

	return render(request, 'legroombad.html', {'legroomTweets':negativeLegroomTweets, 'title':'United Airlines'})

def unitedlegroomgood(request):
	tweets = UnitedAggregateModel.objects.all()
	positiveLegroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom' and tweet.prediction_level >= 0:
			positiveLegroomTweets.append(tweet)

	return render(request, 'legroomgood.html', {'legroomTweets':positiveLegroomTweets, 'title':'United Airlines'})

def unitedtimelinessbad(request):
	tweets = UnitedAggregateModel.objects.all()
	negativeTimeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness' and tweet.prediction_level < 0:
			negativeTimeTweets.append(tweet)

	return render(request, 'timelinessbad.html', {"timeTweets":negativeTimeTweets, 'title':'United Airlines'})

def unitedtimelinessgood(request):
	tweets = UnitedAggregateModel.objects.all()
	positiveTimeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness' and tweet.prediction_level >= 0:
			positiveTimeTweets.append(tweet)

	return render(request, 'timelinessgood.html', {"timeTweets":positiveTimeTweets, 'title':'United Airlines'})

# ------------------------------------------ Spirit Airlines ------------------------------------------
def spiritavailabilitybad(request):
	tweets = SpiritAggregateModel.objects.all()
	negativeAvailableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability' and tweet.prediction_level < 0:
			negativeAvailableTweets.append(tweet)

	return render(request, 'availabilitybad.html', {'availableTweets':negativeAvailableTweets, 'title':'Spirit Airlines'})
	
def spiritavailabilitygood(request):
	tweets = SpiritAggregateModel.objects.all()
	positiveAvailableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability' and tweet.prediction_level >= 0:
			positiveAvailableTweets.append(tweet)

	return render(request, 'availabilitygood.html', {'availableTweets':positiveAvailableTweets, 'title':'Spirit Airlines'})

def spiritcostbad(request):
	tweets = SpiritAggregateModel.objects.all()
	negativeCostTweets = []

	for tweet in tweets:
		if tweet.category == 'cost' and tweet.prediction_level < 0:
			negativeCostTweets.append(tweet)

	return render(request, 'costbad.html', {"costTweets":negativeCostTweets, 'title':'Spirit Airlines'})

def spiritcostgood(request):
	tweets = SpiritAggregateModel.objects.all()
	positiveCostTweets = []

	for tweet in tweets:
		if tweet.category == 'cost' and tweet.prediction_level >= 0:
			positiveCostTweets.append(tweet)

	return render(request, 'costgood.html', {"costTweets":positiveCostTweets, 'title':'Spirit Airlines'})

def spiritlegroombad(request):
	tweets = SpiritAggregateModel.objects.all()
	negativeLegroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom' and tweet.prediction_level < 0:
			negativeLegroomTweets.append(tweet)

	return render(request, 'legroombad.html', {'legroomTweets':negativeLegroomTweets, 'title':'Spirit Airlines'})

def spiritlegroomgood(request):
	tweets = SpiritAggregateModel.objects.all()
	positiveLegroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom' and tweet.prediction_level >= 0:
			positiveLegroomTweets.append(tweet)

	return render(request, 'legroomgood.html', {'legroomTweets':positiveLegroomTweets, 'title':'Spirit Airlines'})

def spirittimelinessbad(request):
	tweets = SpiritAggregateModel.objects.all()
	negativeTimeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness' and tweet.prediction_level < 0:
			negativeTimeTweets.append(tweet)

	return render(request, 'timelinessbad.html', {"timeTweets":negativeTimeTweets, 'title':'Spirit Airlines'})

def spirittimelinessgood(request):
	tweets = SpiritAggregateModel.objects.all()
	positiveTimeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness' and tweet.prediction_level >= 0:
			positiveTimeTweets.append(tweet)

	return render(request, 'timelinessgood.html', {"timeTweets":positiveTimeTweets, 'title':'Spirit Airlines'})
