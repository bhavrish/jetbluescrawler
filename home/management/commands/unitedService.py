from django.core.management.base import BaseCommand
from ...models import UnitedAggregateModel, UnitedCondensedModel
from django.utils import timezone 

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain service-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#unitedairlines service"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update UnitedAggregateModel and DeepAI sentiment analysis
        serviceTweets = twint.output.tweets_list
        for serviceTweet in serviceTweets[:]:
            if not UnitedAggregateModel.objects.filter(tweet_id=serviceTweet.id).exists(): # if new tweet
                DEEP_AI_KEY = os.getenv("DEEP_AI_KEY")
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': serviceTweet.tweet},
                            headers={'api-key': DEEP_AI_KEY})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = UnitedAggregateModel.objects.get_or_create(tweet_id=serviceTweet.id, name=str(serviceTweet.username), text=str(serviceTweet.tweet), link=str(serviceTweet.link), date=serviceTweet.datestamp, prediction_level=score, category="service")

        # Update UnitedCondensedModel
        tweets = UnitedAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'service':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = UnitedCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="service")
