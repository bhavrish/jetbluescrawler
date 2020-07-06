from django.core.management.base import BaseCommand
from ...models import JetblueAggregateModel, JetblueCondensedModel
from django.utils import timezone

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain availability-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#jetblue available"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update JetblueAggregateModel and DeepAI sentiment analysis
        availableTweets = twint.output.tweets_list
        for availableTweet in availableTweets[:]:
            if not JetblueAggregateModel.objects.filter(tweet_id=availableTweet.id).exists(): # if new tweet
                DEEP_AI_KEY = os.getenv("DEEP_AI_KEY")
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': availableTweet.tweet},
                            headers={'api-key': 'DEEP_AI_KEY'})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = JetblueAggregateModel.objects.get_or_create(tweet_id=availableTweet.id, name=str(availableTweet.username), text=str(availableTweet.tweet), link=str(availableTweet.link), date=availableTweet.datestamp, prediction_level=score, category="availability")

        # Update JetblueCondensedModel
        tweets = JetblueAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'availability':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = JetblueCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="availability")