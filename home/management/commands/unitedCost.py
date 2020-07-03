from django.core.management.base import BaseCommand
from ...models import UnitedAggregateModel, UnitedCondensedModel
from django.utils import timezone 

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain cost-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#unitedairlines cost"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update UnitedAggregateModel and DeepAI sentiment analysis
        costTweets = twint.output.tweets_list
        for costTweet in costTweets[:]:
            if not UnitedAggregateModel.objects.filter(tweet_id=costTweet.id).exists(): # if new tweet
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': costTweet.tweet},
                            headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = UnitedAggregateModel.objects.get_or_create(tweet_id=costTweet.id, name=str(costTweet.username), text=str(costTweet.tweet), link=str(costTweet.link), date=costTweet.datestamp, prediction_level=score, category="cost")
        
        # Update UnitedCondensedModel
        tweets = UnitedAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'cost':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = UnitedCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="cost")