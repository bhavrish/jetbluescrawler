from django.shortcuts import render
from .models import JetblueAggregateModel, JetblueCondensedModel, AmericanAggregateModel, AmericanCondensedModel, UnitedAggregateModel, UnitedCondensedModel, SpiritAggregateModel, SpiritCondensedModel
import requests

# Create your views here.
def home(request):
	# JetBlue ------------------------------------------------------------------------------------
	jetBlueTweets = JetblueCondensedModel.objects.all()
	jetblueAvailabilityTweets = []
	jetblueCostTweets = []
	jetblueLegroomTweets = []
	jetblueTimeTweets = []
	jetblueOverallTweetsDict = {}
	
	jetBlueAvailabilitySum = 0
	jetBlueCostSum = 0
	jetBlueLegroomSum = 0
	jetBlueTimeSum = 0

	jetBlueAvailabilityItems = 0
	jetBlueCostItems = 0
	jetBlueLegroomItems = 0
	jetBlueTimeItems = 0
	for tweet in jetBlueTweets:
		if tweet.category == 'availability':
			jetblueAvailabilityTweets.append(tweet)
			jetBlueAvailabilitySum += tweet.average_prediction
			jetBlueAvailabilityItems += 1

		elif tweet.category == 'cost':
			jetblueCostTweets.append(tweet)
			jetBlueCostSum += tweet.average_prediction
			jetBlueCostItems += 1

		elif tweet.category == 'legroom':
			jetblueLegroomTweets.append(tweet)
			jetBlueLegroomSum += tweet.average_prediction
			jetBlueLegroomItems += 1

		elif tweet.category == 'timeliness':
			jetblueTimeTweets.append(tweet)
			jetBlueTimeSum += tweet.average_prediction
			jetBlueTimeItems += 1

		if tweet.date in jetblueOverallTweetsDict:
  			jetblueOverallTweetsDict[tweet.date] += tweet.average_prediction
		else:
			jetblueOverallTweetsDict[tweet.date] = tweet.average_prediction

	jetBlueAvailabilityScore = 0
	if not jetBlueAvailabilityItems == 0:
		jetBlueAvailabilityScore = jetBlueAvailabilitySum / jetBlueAvailabilityItems

	jetBlueCostScore = 0
	if not jetBlueCostItems == 0:	
		jetBlueCostScore = jetBlueCostSum / jetBlueCostItems

	jetBlueLegroomScore = 0
	if not jetBlueLegroomItems == 0:
		jetBlueLegroomScore = jetBlueLegroomSum / jetBlueLegroomItems

	jetBlueTimeScore = 0
	if not jetBlueTimeItems == 0:
		jetBlueTimeScore = jetBlueTimeSum / jetBlueTimeItems
	
	jetBlueOverallScore = (jetBlueAvailabilityScore + jetBlueCostScore + jetBlueLegroomScore + jetBlueTimeScore)/4
	
	jetBlueInfoDict = {
		'jetBlueAvailabilityScore': jetBlueAvailabilityScore,
		'jetBlueCostScore': jetBlueCostScore,
		'jetBlueLegroomScore': jetBlueLegroomScore,
		'jetBlueTimeScore': jetBlueTimeScore,
		'jetBlueOverallScore': jetBlueOverallScore,
		'jetblueOverallTweetsDict': jetblueOverallTweetsDict,
		'jetblueAvailabilityTweets': jetblueAvailabilityTweets,
		'jetblueCostTweets': jetblueCostTweets,
		'jetblueLegroomTweets': jetblueLegroomTweets,
		'jetblueTimeTweets': jetblueTimeTweets
	}

	# American Airlines ------------------------------------------------------------------------------------
	americanTweets = AmericanCondensedModel.objects.all()
	americanAvailabilityTweets = []
	americanCostTweets = []
	americanLegroomTweets = []
	americanTimeTweets = []
	americanOverallTweetsDict = {}
	
	americanAvailabilitySum = 0
	americanCostSum = 0
	americanLegroomSum = 0
	americanTimeSum = 0

	americanAvailabilityItems = 0
	americanCostItems = 0
	americanLegroomItems = 0
	americanTimeItems = 0
	for tweet in americanTweets:
		if tweet.category == 'availability':
			americanAvailabilityTweets.append(tweet)
			americanAvailabilitySum += tweet.average_prediction
			americanAvailabilityItems += 1

		elif tweet.category == 'cost':
			americanCostTweets.append(tweet)
			americanCostSum += tweet.average_prediction
			americanCostItems += 1

		elif tweet.category == 'legroom':
			americanLegroomTweets.append(tweet)
			americanLegroomSum += tweet.average_prediction
			americanLegroomItems += 1

		elif tweet.category == 'timeliness':
			americanTimeTweets.append(tweet)
			americanTimeSum += tweet.average_prediction
			americanTimeItems += 1

		if tweet.date in americanOverallTweetsDict:
  			americanOverallTweetsDict[tweet.date] += tweet.average_prediction
		else:
			americanOverallTweetsDict[tweet.date] = tweet.average_prediction

	americanAvailabilityScore = 0
	if not americanAvailabilityItems == 0:
		americanAvailabilityScore = americanAvailabilitySum / americanAvailabilityItems

	americanCostScore = 0
	if not americanCostItems == 0:	
		americanCostScore = americanCostSum / americanCostItems

	americanLegroomScore = 0
	if not americanLegroomItems == 0:
		americanLegroomScore = americanLegroomSum / americanLegroomItems

	americanTimeScore = 0
	if not americanTimeItems == 0:
		americanTimeScore = americanTimeSum / americanTimeItems
	
	americanOverallScore = (americanAvailabilityScore + americanCostScore + americanLegroomScore + americanTimeScore)/4
	
	americanInfoDict = {
		'americanAvailabilityScore': americanAvailabilityScore,
		'americanCostScore': americanCostScore,
		'americanLegroomScore': americanLegroomScore,
		'americanTimeScore': americanTimeScore,
		'americanOverallScore': americanOverallScore,
		'americanOverallTweetsDict': americanOverallTweetsDict,
		'americanAvailabilityTweets': americanAvailabilityTweets,
		'americanCostTweets': americanCostTweets,
		'americanLegroomTweets': americanLegroomTweets,
		'americanTimeTweets': americanTimeTweets
	}

	# United Airlines ------------------------------------------------------------------------------------
	unitedTweets = UnitedCondensedModel.objects.all()
	unitedAvailabilityTweets = []
	unitedCostTweets = []
	unitedLegroomTweets = []
	unitedTimeTweets = []
	unitedOverallTweetsDict = {}
	
	unitedAvailabilitySum = 0
	unitedCostSum = 0
	unitedLegroomSum = 0
	unitedTimeSum = 0

	unitedAvailabilityItems = 0
	unitedCostItems = 0
	unitedLegroomItems = 0
	unitedTimeItems = 0
	for tweet in unitedTweets:
		if tweet.category == 'availability':
			unitedAvailabilityTweets.append(tweet)
			unitedAvailabilitySum += tweet.average_prediction
			unitedAvailabilityItems += 1

		elif tweet.category == 'cost':
			unitedCostTweets.append(tweet)
			unitedCostSum += tweet.average_prediction
			unitedCostItems += 1

		elif tweet.category == 'legroom':
			unitedLegroomTweets.append(tweet)
			unitedLegroomSum += tweet.average_prediction
			unitedLegroomItems += 1

		elif tweet.category == 'timeliness':
			unitedTimeTweets.append(tweet)
			unitedTimeSum += tweet.average_prediction
			unitedTimeItems += 1

		if tweet.date in unitedOverallTweetsDict:
  			unitedOverallTweetsDict[tweet.date] += tweet.average_prediction
		else:
			unitedOverallTweetsDict[tweet.date] = tweet.average_prediction

	unitedAvailabilityScore = 0
	if not unitedAvailabilityItems == 0:
		unitedAvailabilityScore = unitedAvailabilitySum / unitedAvailabilityItems

	unitedCostScore = 0
	if not unitedCostItems == 0:	
		unitedCostScore = unitedCostSum / unitedCostItems

	unitedLegroomScore = 0
	if not unitedLegroomItems == 0:
		unitedLegroomScore = unitedLegroomSum / unitedLegroomItems

	unitedTimeScore = 0
	if not unitedTimeItems == 0:
		unitedTimeScore = unitedTimeSum / unitedTimeItems
	
	unitedOverallScore = (unitedAvailabilityScore + unitedCostScore + unitedLegroomScore + unitedTimeScore)/4
	
	unitedInfoDict = {
		'unitedAvailabilityScore': unitedAvailabilityScore,
		'unitedCostScore': unitedCostScore,
		'unitedLegroomScore': unitedLegroomScore,
		'unitedTimeScore': unitedTimeScore,
		'unitedOverallScore': unitedOverallScore,
		'unitedOverallTweetsDict': unitedOverallTweetsDict,
		'unitedAvailabilityTweets': unitedAvailabilityTweets,
		'unitedCostTweets': unitedCostTweets,
		'unitedLegroomTweets': unitedLegroomTweets,
		'unitedTimeTweets': unitedTimeTweets
	}

	# Spirit Airlines ------------------------------------------------------------------------------------
	spiritTweets = SpiritCondensedModel.objects.all()
	spiritAvailabilityTweets = []
	spiritCostTweets = []
	spiritLegroomTweets = []
	spiritTimeTweets = []
	spiritOverallTweetsDict = {}
	
	spiritAvailabilitySum = 0
	spiritCostSum = 0
	spiritLegroomSum = 0
	spiritTimeSum = 0

	spiritAvailabilityItems = 0
	spiritCostItems = 0
	spiritLegroomItems = 0
	spiritTimeItems = 0
	for tweet in spiritTweets:
		if tweet.category == 'availability':
			spiritAvailabilityTweets.append(tweet)
			spiritAvailabilitySum += tweet.average_prediction
			spiritAvailabilityItems += 1

		elif tweet.category == 'cost':
			spiritCostTweets.append(tweet)
			spiritCostSum += tweet.average_prediction
			spiritCostItems += 1

		elif tweet.category == 'legroom':
			spiritLegroomTweets.append(tweet)
			spiritLegroomSum += tweet.average_prediction
			spiritLegroomItems += 1

		elif tweet.category == 'timeliness':
			spiritTimeTweets.append(tweet)
			spiritTimeSum += tweet.average_prediction
			spiritTimeItems += 1

		if tweet.date in spiritOverallTweetsDict:
  			spiritOverallTweetsDict[tweet.date] += tweet.average_prediction
		else:
			spiritOverallTweetsDict[tweet.date] = tweet.average_prediction

	spiritAvailabilityScore = 0
	if not spiritAvailabilityItems == 0:
		spiritAvailabilityScore = spiritAvailabilitySum / spiritAvailabilityItems

	spiritCostScore = 0
	if not spiritCostItems == 0:	
		spiritCostScore = spiritCostSum / spiritCostItems

	spiritLegroomScore = 0
	if not spiritLegroomItems == 0:
		spiritLegroomScore = spiritLegroomSum / spiritLegroomItems

	spiritTimeScore = 0
	if not spiritTimeItems == 0:
		spiritTimeScore = spiritTimeSum / spiritTimeItems
	
	spiritOverallScore = (spiritAvailabilityScore + spiritCostScore + spiritLegroomScore + spiritTimeScore)/4
	
	spiritInfoDict = {
		'spiritAvailabilityScore': spiritAvailabilityScore,
		'spiritCostScore': spiritCostScore,
		'spiritLegroomScore': spiritLegroomScore,
		'spiritTimeScore': spiritTimeScore,
		'spiritOverallScore': spiritOverallScore,
		'spiritOverallTweetsDict': spiritOverallTweetsDict,
		'spiritAvailabilityTweets': spiritAvailabilityTweets,
		'spiritCostTweets': spiritCostTweets,
		'spiritLegroomTweets': spiritLegroomTweets,
		'spiritTimeTweets': spiritTimeTweets
	}

	airlineInfoList = [jetBlueInfoDict, americanInfoDict, unitedInfoDict, spiritInfoDict]
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
