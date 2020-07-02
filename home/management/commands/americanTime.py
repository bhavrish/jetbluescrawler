from django.core.management.base import BaseCommand
from ...models import AmericanAggregateModel, AmericanCondensedModel
from django.utils import timezone 

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain time-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#americanairlines time"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update AmericanAggregateModel and DeepAI sentiment analysis
        timeTweets = twint.output.tweets_list
        for timeTweet in timeTweets[:]:
            if not AmericanAggregateModel.objects.filter(tweet_id=timeTweet.id).exists(): # if new tweet
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': timeTweet.tweet},
                            headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = AmericanAggregateModel.objects.get_or_create(tweet_id=timeTweet.id, name=str(timeTweet.username), text=str(timeTweet.tweet), link=str(timeTweet.link), date=timeTweet.datestamp, prediction_level=score, category="timeliness")

        # Update AmericanCondensedModel
        tweets = AmericanAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'timeliness':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = AmericanCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="timeliness")