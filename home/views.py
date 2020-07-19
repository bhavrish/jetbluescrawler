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

	return render(request, 'data.html', {"tweets":costTweets, 'title':'JetBlue', 'category': 'Cost'})

def legroom(request):
	tweets = JetblueAggregateModel.objects.all()
	legroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom':
			legroomTweets.append(tweet)

	return render(request, 'data.html', {'tweets':legroomTweets, 'title':'JetBlue', 'category': 'Legroom'})

def timeliness(request):
	tweets = JetblueAggregateModel.objects.all()
	timeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness':
			timeTweets.append(tweet)

	return render(request, 'data.html', {"tweets":timeTweets, 'title':'JetBlue', 'category': 'Timeliness'})

def hiddenFees(request):
	tweets = JetblueAggregateModel.objects.all()
	hiddenFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'hidden-fees':
			hiddenFeesTweets.append(tweet)

	return render(request, 'data.html', {"tweets":hiddenFeesTweets, 'title':'JetBlue', 'category': 'Hidden Fees'})

def baggageFees(request):
	tweets = JetblueAggregateModel.objects.all()
	baggageFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'baggage-fees':
			baggageFeesTweets.append(tweet)

	return render(request, 'data.html', {"tweets":baggageFeesTweets, 'title':'JetBlue', 'category': 'Baggage Fees'})

def travelRewards(request):
	tweets = JetblueAggregateModel.objects.all()
	travelRewardsTweets = []

	for tweet in tweets:
		if tweet.category == 'travel-rewards':
			travelRewardsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":travelRewardsTweets, 'title':'JetBlue', 'category': 'Travel'})

def reimbursement(request):
	tweets = JetblueAggregateModel.objects.all()
	reimbursementTweets = []

	for tweet in tweets:
		if tweet.category == 'reimbursement':
			reimbursementTweets.append(tweet)

	return render(request, 'data.html', {"tweets":reimbursementTweets, 'title':'JetBlue', 'category': 'Reimbursement'})

def connections(request):
	tweets = JetblueAggregateModel.objects.all()
	connectionsTweets = []

	for tweet in tweets:
		if tweet.category == 'connections':
			connectionsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":connectionsTweets, 'title':'JetBlue', 'category': 'Connections'})

def foodEntertainment(request):
	tweets = JetblueAggregateModel.objects.all()
	foodEntertainmentTweets = []

	for tweet in tweets:
		if tweet.category == 'food-entertainment':
			foodEntertainmentTweets.append(tweet)

	return render(request, 'data.html', {"tweets":foodEntertainmentTweets, 'title':'JetBlue', 'category': 'Food Entertainment'})

def service(request):
	tweets = JetblueAggregateModel.objects.all()
	serviceTweets = []

	for tweet in tweets:
		if tweet.category == 'service':
			serviceTweets.append(tweet)

	return render(request, 'data.html', {"tweets":serviceTweets, 'title':'JetBlue', 'category': 'Service'})

def familyOptions(request):
	tweets = JetblueAggregateModel.objects.all()
	familyOptionsTweets = []

	for tweet in tweets:
		if tweet.category == 'family-options':
			familyOptionsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":familyOptionsTweets, 'title':'JetBlue', 'category': 'Family Options'})


# ------------------------------------------ American Airlines ------------------------------------------
def americanAvailability(request):
	tweets = AmericanAggregateModel.objects.all()
	availableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability':
			availableTweets.append(tweet)

	return render(request, 'data.html', {'tweets':availableTweets, 'title':'American Airlines', 'category': 'Availability'})

def americanCost(request):
	tweets = AmericanAggregateModel.objects.all()
	costTweets = []

	for tweet in tweets:
		if tweet.category == 'cost':
			costTweets.append(tweet)

	return render(request, 'data.html', {"tweets":costTweets, 'title':'American Airlines', 'category': 'Cost'})

def americanLegroom(request):
	tweets = AmericanAggregateModel.objects.all()
	legroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom':
			legroomTweets.append(tweet)

	return render(request, 'data.html', {'tweets':legroomTweets, 'title':'American Airlines', 'category': 'Legroom'})

def americanTimeliness(request):
	tweets = AmericanAggregateModel.objects.all()
	timeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness':
			timeTweets.append(tweet)

	return render(request, 'data.html', {"tweets":timeTweets, 'title':'American Airlines', 'category': 'Timeliness'})

def americanHiddenFees(request):
	tweets = AmericanAggregateModel.objects.all()
	hiddenFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'hidden-fees':
			hiddenFeesTweets.append(tweet)

	return render(request, 'data.html', {"tweets":hiddenFeesTweets, 'title':'American Airlines', 'category': 'Hidden Fees'})

def americanBaggageFees(request):
	tweets = AmericanAggregateModel.objects.all()
	baggageFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'baggage-fees':
			baggageFeesTweets.append(tweet)

	return render(request, 'data.html', {"tweets":baggageFeesTweets, 'title':'American Airlines', 'category': 'Baggage Fees'})

def americanTravelRewards(request):
	tweets = AmericanAggregateModel.objects.all()
	travelRewardsTweets = []

	for tweet in tweets:
		if tweet.category == 'travel-rewards':
			travelRewardsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":travelRewardsTweets, 'title':'American Airlines', 'category': 'Travel Rewards'})

def americanReimbursement(request):
	tweets = AmericanAggregateModel.objects.all()
	reimbursementTweets = []

	for tweet in tweets:
		if tweet.category == 'reimbursement':
			reimbursementTweets.append(tweet)

	return render(request, 'data.html', {"tweets":reimbursementTweets, 'title':'American Airlines', 'category': 'Reimbursement'})

def americanConnections(request):
	tweets = AmericanAggregateModel.objects.all()
	connectionsTweets = []

	for tweet in tweets:
		if tweet.category == 'connections':
			connectionsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":connectionsTweets, 'title':'American Airlines', 'category': 'Connections'})

def americanFoodEntertainment(request):
	tweets = AmericanAggregateModel.objects.all()
	foodEntertainmentTweets = []

	for tweet in tweets:
		if tweet.category == 'food-entertainment':
			foodEntertainmentTweets.append(tweet)

	return render(request, 'data.html', {"tweets":foodEntertainmentTweets, 'title':'American Airlines', 'category': 'Food Entertainment'})

def americanService(request):
	tweets = AmericanAggregateModel.objects.all()
	serviceTweets = []

	for tweet in tweets:
		if tweet.category == 'service':
			serviceTweets.append(tweet)

	return render(request, 'data.html', {"tweets":serviceTweets, 'title':'American Airlines', 'category': 'Service'})

def americanFamilyOptions(request):
	tweets = AmericanAggregateModel.objects.all()
	familyOptionsTweets = []

	for tweet in tweets:
		if tweet.category == 'family-options':
			familyOptionsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":familyOptionsTweets, 'title':'American Airlines', 'category': 'Family Options'})

# ------------------------------------------ United Airlines ------------------------------------------
def unitedAvailability(request):
	tweets = UnitedAggregateModel.objects.all()
	availableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability':
			availableTweets.append(tweet)

	return render(request, 'data.html', {'tweets':availableTweets, 'title':'United Airlines', 'category': 'Availability'})

def unitedCost(request):
	tweets = UnitedAggregateModel.objects.all()
	costTweets = []

	for tweet in tweets:
		if tweet.category == 'cost':
			costTweets.append(tweet)

	return render(request, 'data.html', {"tweets":costTweets, 'title':'United Airlines', 'category': 'Cost'})

def unitedLegroom(request):
	tweets = UnitedAggregateModel.objects.all()
	legroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom':
			legroomTweets.append(tweet)

	return render(request, 'data.html', {'tweets':legroomTweets, 'title':'United Airlines', 'category': 'Legroom'})

def unitedTimeliness(request):
	tweets = UnitedAggregateModel.objects.all()
	timeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness':
			timeTweets.append(tweet)

	return render(request, 'data.html', {"tweets":timeTweets, 'title':'United Airlines', 'category': 'Timeliness'})

def unitedHiddenFees(request):
	tweets = UnitedAggregateModel.objects.all()
	hiddenFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'hidden-fees':
			hiddenFeesTweets.append(tweet)

	return render(request, 'data.html', {"tweets":hiddenFeesTweets, 'title':'United Airlines', 'category': 'Hidden Ffees'})

def unitedBaggageFees(request):
	tweets = UnitedAggregateModel.objects.all()
	baggageFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'baggage-fees':
			baggageFeesTweets.append(tweet)

	return render(request, 'data.html', {"tweets":baggageFeesTweets, 'title':'United Airlines', 'category': 'Baggage Fees'})

def unitedTravelRewards(request):
	tweets = UnitedAggregateModel.objects.all()
	travelRewardsTweets = []

	for tweet in tweets:
		if tweet.category == 'travel-rewards':
			travelRewardsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":travelRewardsTweets, 'title':'United Airlines', 'category': 'Travel Rewards'})

def unitedReimbursement(request):
	tweets = UnitedAggregateModel.objects.all()
	reimbursementTweets = []

	for tweet in tweets:
		if tweet.category == 'reimbursement':
			reimbursementTweets.append(tweet)

	return render(request, 'data.html', {"tweets":reimbursementTweets, 'title':'United Airlines', 'category': 'Reimbursement'})

def unitedConnections(request):
	tweets = UnitedAggregateModel.objects.all()
	connectionsTweets = []

	for tweet in tweets:
		if tweet.category == 'connections':
			connectionsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":connectionsTweets, 'title':'United Airlines', 'category': 'Connections'})

def unitedFoodEntertainment(request):
	tweets = UnitedAggregateModel.objects.all()
	foodEntertainmentTweets = []

	for tweet in tweets:
		if tweet.category == 'food-entertainment':
			foodEntertainmentTweets.append(tweet)

	return render(request, 'data.html', {"tweets":foodEntertainmentTweets, 'title':'United Airlines', 'category': 'Food Entertainment'})

def unitedService(request):
	tweets = UnitedAggregateModel.objects.all()
	serviceTweets = []

	for tweet in tweets:
		if tweet.category == 'service':
			serviceTweets.append(tweet)

	return render(request, 'data.html', {"tweets":serviceTweets, 'title':'United Airlines', 'category': 'Service'})

def unitedFamilyOptions(request):
	tweets = UnitedAggregateModel.objects.all()
	familyOptionsTweets = []

	for tweet in tweets:
		if tweet.category == 'family-options':
			familyOptionsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":familyOptionsTweets, 'title':'United Airlines', 'category': 'Family Options'})

# ------------------------------------------ Spirit Airlines ------------------------------------------
def spiritAvailability(request):
	tweets = SpiritAggregateModel.objects.all()
	availableTweets = []

	for tweet in tweets:
		if tweet.category == 'availability':
			availableTweets.append(tweet)

	return render(request, 'data.html', {'tweets':availableTweets, 'title':'Spirit Airlines', 'category': 'Availability'})

def spiritCost(request):
	tweets = SpiritAggregateModel.objects.all()
	costTweets = []

	for tweet in tweets:
		if tweet.category == 'cost':
			costTweets.append(tweet)

	return render(request, 'data.html', {"tweets":costTweets, 'title':'Spirit Airlines', 'category': 'Cost'})

def spiritLegroom(request):
	tweets = SpiritAggregateModel.objects.all()
	legroomTweets = []

	for tweet in tweets:
		if tweet.category == 'legroom':
			legroomTweets.append(tweet)

	return render(request, 'data.html', {'tweets':legroomTweets, 'title':'Spirit Airlines', 'category': 'Legroom'})

def spiritTimeliness(request):
	tweets = SpiritAggregateModel.objects.all()
	timeTweets = []

	for tweet in tweets:
		if tweet.category == 'timeliness':
			timeTweets.append(tweet)

	return render(request, 'data.html', {"tweets":timeTweets, 'title':'Spirit Airlines', 'category': 'Timeliness'})

def spiritHiddenFees(request):
	tweets = SpiritAggregateModel.objects.all()
	hiddenFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'hidden-fees':
			hiddenFeesTweets.append(tweet)

	return render(request, 'data.html', {"tweets":hiddenFeesTweets, 'title':'Spirit Airlines', 'category': 'Hidden Fees'})

def spiritBaggageFees(request):
	tweets = SpiritAggregateModel.objects.all()
	baggageFeesTweets = []

	for tweet in tweets:
		if tweet.category == 'baggage-fees':
			baggageFeesTweets.append(tweet)

	return render(request, 'data.html', {"tweets":baggageFeesTweets, 'title':'Spirit Airlines', 'category': 'Baggage Fees'})

def spiritTravelRewards(request):
	tweets = SpiritAggregateModel.objects.all()
	travelRewardsTweets = []

	for tweet in tweets:
		if tweet.category == 'travel-rewards':
			travelRewardsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":travelRewardsTweets, 'title':'Spirit Airlines', 'category': 'Travel Rewards'})

def spiritReimbursement(request):
	tweets = SpiritAggregateModel.objects.all()
	reimbursementTweets = []

	for tweet in tweets:
		if tweet.category == 'reimbursement':
			reimbursementTweets.append(tweet)

	return render(request, 'data.html', {"tweets":reimbursementTweets, 'title':'Spirit Airlines', 'category': 'Reimbursement'})

def spiritConnections(request):
	tweets = SpiritAggregateModel.objects.all()
	connectionsTweets = []

	for tweet in tweets:
		if tweet.category == 'connections':
			connectionsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":connectionsTweets, 'title':'Spirit Airlines', 'category': 'Connections'})

def spiritFoodEntertainment(request):
	tweets = SpiritAggregateModel.objects.all()
	foodEntertainmentTweets = []

	for tweet in tweets:
		if tweet.category == 'food-entertainment':
			foodEntertainmentTweets.append(tweet)

	return render(request, 'data.html', {"tweets":foodEntertainmentTweets, 'title':'Spirit Airlines', 'category': 'Food Entertainment'})

def spiritService(request):
	tweets = SpiritAggregateModel.objects.all()
	serviceTweets = []

	for tweet in tweets:
		if tweet.category == 'service':
			serviceTweets.append(tweet)

	return render(request, 'data.html', {"tweets":serviceTweets, 'title':'Spirit Airlines', 'category': 'Service'})

def spiritFamilyOptions(request):
	tweets = SpiritAggregateModel.objects.all()
	familyOptionsTweets = []

	for tweet in tweets:
		if tweet.category == 'family-options':
			familyOptionsTweets.append(tweet)

	return render(request, 'data.html', {"tweets":familyOptionsTweets, 'title':'Spirit Airlines', 'category': 'Family Options'})
