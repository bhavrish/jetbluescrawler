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
		modelObjects = airline['modelObjects']

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
def availability(request):
	tweets = JetblueAggregateModel.objects.all()
	availableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability':
			availableTweets.append(tweet)

	return render(request, 'data.html', {'tweets':availableTweets, 'title':'JetBlue', 'category': 'Availability'})

def cost(request):
	tweets = JetblueAggregateModel.objects.all()
	costTweets = []

	for tweet in tweets:
		if tweet.category == 'cost':
			costTweets.append(tweet)

	return render(request, 'cost.html', {"costTweets":costTweets, 'title':'JetBlue'})

def legroom(request):
	tweets = JetblueAggregateModel.objects.all()
	legroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom':
			legroomTweets.append(tweet)

	return render(request, 'legroom.html', {'legroomTweets':legroomTweets, 'title':'JetBlue'})

def timeliness(request):
	tweets = JetblueAggregateModel.objects.all()
	timeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness':
			timeTweets.append(tweet)

	return render(request, 'timeliness.html', {"timeTweets":timeTweets, 'title':'JetBlue'})

def hiddenFees(request):
	tweets = JetblueAggregateModel.objects.all()
	hiddenFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'hidden-fees':
			hiddenFeesTweets.append(tweet)

	return render(request, 'hiddenFees.html', {"hiddenFeesTweets":hiddenFeesTweets, 'title':'JetBlue'})

def baggageFees(request):
	tweets = JetblueAggregateModel.objects.all()
	baggageFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'baggage-fees':
			baggageFeesTweets.append(tweet)

	return render(request, 'baggageFees.html', {"baggageFeesTweets":baggageFeesTweets, 'title':'JetBlue'})

def travelRewards(request):
	tweets = JetblueAggregateModel.objects.all()
	travelRewardsTweets = []

	for tweet in tweets:
		if tweet.category == 'travel-rewards':
			travelRewardsTweets.append(tweet)

	return render(request, 'travelRewards.html', {"travelRewardsTweets":travelRewardsTweets, 'title':'JetBlue'})

def reimbursement(request):
	tweets = JetblueAggregateModel.objects.all()
	reimbursementTweets = []

	for tweet in tweets:
		if tweet.category == 'reimbursement':
			reimbursementTweets.append(tweet)

	return render(request, 'reimbursement.html', {"reimbursementTweets":reimbursementTweets, 'title':'JetBlue'})

def connections(request):
	tweets = JetblueAggregateModel.objects.all()
	connectionsTweets = []

	for tweet in tweets:
		if tweet.category == 'connections':
			connectionsTweets.append(tweet)

	return render(request, 'connections.html', {"connectionsTweets":connectionsTweets, 'title':'JetBlue'})

def foodEntertainment(request):
	tweets = JetblueAggregateModel.objects.all()
	foodEntertainmentTweets = []

	for tweet in tweets:
		if tweet.category == 'food-entertainment':
			foodEntertainmentTweets.append(tweet)

	return render(request, 'foodEntertainment.html', {"foodEntertainmentTweets":foodEntertainmentTweets, 'title':'JetBlue'})

def service(request):
	tweets = JetblueAggregateModel.objects.all()
	serviceTweets = []

	for tweet in tweets:
		if tweet.category == 'service':
			serviceTweets.append(tweet)

	return render(request, 'service.html', {"serviceTweets":serviceTweets, 'title':'JetBlue'})

def familyOptions(request):
	tweets = JetblueAggregateModel.objects.all()
	familyOptionsTweets = []

	for tweet in tweets:
		if tweet.category == 'family-options':
			familyOptionsTweets.append(tweet)

	return render(request, 'familyOptions.html', {"familyOptionsTweets":familyOptionsTweets, 'title':'JetBlue'})


# ------------------------------------------ American Airlines ------------------------------------------
def americanAvailability(request):
	tweets = AmericanAggregateModel.objects.all()
	availableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability':
			availableTweets.append(tweet)

	return render(request, 'availability.html', {'availableTweets':availableTweets, 'title':'American Airlines'})

def americanCost(request):
	tweets = AmericanAggregateModel.objects.all()
	costTweets = []

	for tweet in tweets:
		if tweet.category == 'cost':
			costTweets.append(tweet)

	return render(request, 'cost.html', {"costTweets":costTweets, 'title':'American Airlines'})

def americanLegroom(request):
	tweets = AmericanAggregateModel.objects.all()
	legroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom':
			legroomTweets.append(tweet)

	return render(request, 'legroom.html', {'legroomTweets':legroomTweets, 'title':'American Airlines'})

def americanTimeliness(request):
	tweets = AmericanAggregateModel.objects.all()
	timeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness':
			timeTweets.append(tweet)

	return render(request, 'timeliness.html', {"timeTweets":timeTweets, 'title':'American Airlines'})

def americanHiddenFees(request):
	tweets = AmericanAggregateModel.objects.all()
	hiddenFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'hidden-fees':
			hiddenFeesTweets.append(tweet)

	return render(request, 'hiddenFees.html', {"hiddenFeesTweets":hiddenFeesTweets, 'title':'American Airlines'})

def americanBaggageFees(request):
	tweets = AmericanAggregateModel.objects.all()
	baggageFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'baggage-fees':
			baggageFeesTweets.append(tweet)

	return render(request, 'baggageFees.html', {"baggageFeesTweets":baggageFeesTweets, 'title':'American Airlines'})

def americanTravelRewards(request):
	tweets = AmericanAggregateModel.objects.all()
	travelRewardsTweets = []

	for tweet in tweets:
		if tweet.category == 'travel-rewards':
			travelRewardsTweets.append(tweet)

	return render(request, 'travelRewards.html', {"travelRewardsTweets":travelRewardsTweets, 'title':'American Airlines'})

def americanReimbursement(request):
	tweets = AmericanAggregateModel.objects.all()
	reimbursementTweets = []

	for tweet in tweets:
		if tweet.category == 'reimbursement':
			reimbursementTweets.append(tweet)

	return render(request, 'reimbursement.html', {"reimbursementTweets":reimbursementTweets, 'title':'American Airlines'})

def americanConnections(request):
	tweets = AmericanAggregateModel.objects.all()
	connectionsTweets = []

	for tweet in tweets:
		if tweet.category == 'connections':
			connectionsTweets.append(tweet)

	return render(request, 'connections.html', {"connectionsTweets":connectionsTweets, 'title':'American Airlines'})

def americanFoodEntertainment(request):
	tweets = AmericanAggregateModel.objects.all()
	foodEntertainmentTweets = []

	for tweet in tweets:
		if tweet.category == 'food-entertainment':
			foodEntertainmentTweets.append(tweet)

	return render(request, 'foodEntertainment.html', {"foodEntertainmentTweets":foodEntertainmentTweets, 'title':'American Airlines'})

def americanService(request):
	tweets = AmericanAggregateModel.objects.all()
	serviceTweets = []

	for tweet in tweets:
		if tweet.category == 'service':
			serviceTweets.append(tweet)

	return render(request, 'service.html', {"serviceTweets":serviceTweets, 'title':'American Airlines'})

def americanFamilyOptions(request):
	tweets = AmericanAggregateModel.objects.all()
	familyOptionsTweets = []

	for tweet in tweets:
		if tweet.category == 'family-options':
			familyOptionsTweets.append(tweet)

	return render(request, 'familyOptions.html', {"familyOptionsTweets":familyOptionsTweets, 'title':'American Airlines'})

# ------------------------------------------ United Airlines ------------------------------------------
def unitedAvailability(request):
	tweets = UnitedAggregateModel.objects.all()
	availableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability':
			availableTweets.append(tweet)

	return render(request, 'availability.html', {'availableTweets':availableTweets, 'title':'United Airlines'})

def unitedCost(request):
	tweets = UnitedAggregateModel.objects.all()
	costTweets = []

	for tweet in tweets:
		if tweet.category == 'cost':
			costTweets.append(tweet)

	return render(request, 'cost.html', {"costTweets":costTweets, 'title':'United Airlines'})

def unitedLegroom(request):
	tweets = UnitedAggregateModel.objects.all()
	legroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom':
			legroomTweets.append(tweet)

	return render(request, 'legroom.html', {'legroomTweets':legroomTweets, 'title':'United Airlines'})

def unitedTimeliness(request):
	tweets = UnitedAggregateModel.objects.all()
	timeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness':
			timeTweets.append(tweet)

	return render(request, 'timeliness.html', {"timeTweets":timeTweets, 'title':'United Airlines'})

def unitedHiddenFees(request):
	tweets = UnitedAggregateModel.objects.all()
	hiddenFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'hidden-fees':
			hiddenFeesTweets.append(tweet)

	return render(request, 'hiddenFees.html', {"hiddenFeesTweets":hiddenFeesTweets, 'title':'United Airlines'})

def unitedBaggageFees(request):
	tweets = UnitedAggregateModel.objects.all()
	baggageFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'baggage-fees':
			baggageFeesTweets.append(tweet)

	return render(request, 'baggageFees.html', {"baggageFeesTweets":baggageFeesTweets, 'title':'United Airlines'})

def unitedTravelRewards(request):
	tweets = UnitedAggregateModel.objects.all()
	travelRewardsTweets = []

	for tweet in tweets:
		if tweet.category == 'travel-rewards':
			travelRewardsTweets.append(tweet)

	return render(request, 'travelRewards.html', {"travelRewardsTweets":travelRewardsTweets, 'title':'United Airlines'})

def unitedReimbursement(request):
	tweets = UnitedAggregateModel.objects.all()
	reimbursementTweets = []

	for tweet in tweets:
		if tweet.category == 'reimbursement':
			reimbursementTweets.append(tweet)

	return render(request, 'reimbursement.html', {"reimbursementTweets":reimbursementTweets, 'title':'United Airlines'})

def unitedConnections(request):
	tweets = UnitedAggregateModel.objects.all()
	connectionsTweets = []

	for tweet in tweets:
		if tweet.category == 'connections':
			connectionsTweets.append(tweet)

	return render(request, 'connections.html', {"connectionsTweets":connectionsTweets, 'title':'United Airlines'})

def unitedFoodEntertainment(request):
	tweets = UnitedAggregateModel.objects.all()
	foodEntertainmentTweets = []

	for tweet in tweets:
		if tweet.category == 'food-entertainment':
			foodEntertainmentTweets.append(tweet)

	return render(request, 'foodEntertainment.html', {"foodEntertainmentTweets":foodEntertainmentTweets, 'title':'United Airlines'})

def unitedService(request):
	tweets = UnitedAggregateModel.objects.all()
	serviceTweets = []

	for tweet in tweets:
		if tweet.category == 'service':
			serviceTweets.append(tweet)

	return render(request, 'service.html', {"serviceTweets":serviceTweets, 'title':'United Airlines'})

def unitedFamilyOptions(request):
	tweets = UnitedAggregateModel.objects.all()
	familyOptionsTweets = []

	for tweet in tweets:
		if tweet.category == 'family-options':
			familyOptionsTweets.append(tweet)

	return render(request, 'familyOptions.html', {"familyOptionsTweets":familyOptionsTweets, 'title':'United Airlines'})

# ------------------------------------------ Spirit Airlines ------------------------------------------
def spiritAvailability(request):
	tweets = SpiritAggregateModel.objects.all()
	availableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability':
			availableTweets.append(tweet)

	return render(request, 'availability.html', {'availableTweets':availableTweets, 'title':'Spirit Airlines'})

def spiritCost(request):
	tweets = SpiritAggregateModel.objects.all()
	costTweets = []

	for tweet in tweets:
		if tweet.category == 'cost':
			costTweets.append(tweet)

	return render(request, 'cost.html', {"costTweets":costTweets, 'title':'Spirit Airlines'})

def spiritLegroom(request):
	tweets = SpiritAggregateModel.objects.all()
	legroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom':
			legroomTweets.append(tweet)

	return render(request, 'legroom.html', {'legroomTweets':legroomTweets, 'title':'Spirit Airlines'})

def spiritTimeliness(request):
	tweets = SpiritAggregateModel.objects.all()
	timeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness':
			timeTweets.append(tweet)

	return render(request, 'timeliness.html', {"timeTweets":timeTweets, 'title':'Spirit Airlines'})

def spiritHiddenFees(request):
	tweets = SpiritAggregateModel.objects.all()
	hiddenFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'hidden-fees':
			hiddenFeesTweets.append(tweet)

	return render(request, 'hiddenFees.html', {"hiddenFeesTweets":hiddenFeesTweets, 'title':'Spirit Airlines'})

def spiritBaggageFees(request):
	tweets = SpiritAggregateModel.objects.all()
	baggageFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'baggage-fees':
			baggageFeesTweets.append(tweet)

	return render(request, 'baggageFees.html', {"baggageFeesTweets":baggageFeesTweets, 'title':'Spirit Airlines'})

def spiritTravelRewards(request):
	tweets = SpiritAggregateModel.objects.all()
	travelRewardsTweets = []

	for tweet in tweets:
		if tweet.category == 'travel-rewards':
			travelRewardsTweets.append(tweet)

	return render(request, 'travelRewards.html', {"travelRewardsTweets":travelRewardsTweets, 'title':'Spirit Airlines'})

def spiritReimbursement(request):
	tweets = SpiritAggregateModel.objects.all()
	reimbursementTweets = []

	for tweet in tweets:
		if tweet.category == 'reimbursement':
			reimbursementTweets.append(tweet)

	return render(request, 'reimbursement.html', {"reimbursementTweets":reimbursementTweets, 'title':'Spirit Airlines'})

def spiritConnections(request):
	tweets = SpiritAggregateModel.objects.all()
	connectionsTweets = []

	for tweet in tweets:
		if tweet.category == 'connections':
			connectionsTweets.append(tweet)

	return render(request, 'connections.html', {"connectionsTweets":connectionsTweets, 'title':'Spirit Airlines'})

def spiritFoodEntertainment(request):
	tweets = SpiritAggregateModel.objects.all()
	foodEntertainmentTweets = []

	for tweet in tweets:
		if tweet.category == 'food-entertainment':
			foodEntertainmentTweets.append(tweet)

	return render(request, 'foodEntertainment.html', {"foodEntertainmentTweets":foodEntertainmentTweets, 'title':'Spirit Airlines'})

def spiritService(request):
	tweets = SpiritAggregateModel.objects.all()
	serviceTweets = []

	for tweet in tweets:
		if tweet.category == 'service':
			serviceTweets.append(tweet)

	return render(request, 'service.html', {"serviceTweets":serviceTweets, 'title':'Spirit Airlines'})

def spiritFamilyOptions(request):
	tweets = SpiritAggregateModel.objects.all()
	familyOptionsTweets = []

	for tweet in tweets:
		if tweet.category == 'family-options':
			familyOptionsTweets.append(tweet)

	return render(request, 'familyOptions.html', {"familyOptionsTweets":familyOptionsTweets, 'title':'Spirit Airlines'})
