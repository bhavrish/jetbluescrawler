from django.core.management.base import BaseCommand
from ...models import UnitedAggregateModel, UnitedCondensedModel
from django.utils import timezone 

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain baggage-fees-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#unitedairlines baggage fees"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update UnitedAggregateModel and DeepAI sentiment analysis
        baggageFeesTweets = twint.output.tweets_list
        for baggageFeesTweet in baggageFeesTweets[:]:
            if not UnitedAggregateModel.objects.filter(tweet_id=baggageFeesTweet.id).exists(): # if new tweet
                DEEP_AI_KEY = os.getenv("DEEP_AI_KEY")
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': baggageFeesTweet.tweet},
                            headers={'api-key': DEEP_AI_KEY})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = UnitedAggregateModel.objects.get_or_create(tweet_id=baggageFeesTweet.id, name=str(baggageFeesTweet.username), text=str(baggageFeesTweet.tweet), link=str(baggageFeesTweet.link), date=baggageFeesTweet.datestamp, prediction_level=score, category="baggage-fees")

        # Update UnitedCondensedModel
        tweets = UnitedAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'baggage-fees':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = UnitedCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="baggage-fees")
