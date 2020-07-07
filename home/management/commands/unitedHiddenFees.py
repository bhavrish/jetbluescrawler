from django.core.management.base import BaseCommand
from ...models import UnitedAggregateModel, UnitedCondensedModel
from django.utils import timezone 

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain hidden-fees-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#unitedairlines hidden fees"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update UnitedAggregateModel and DeepAI sentiment analysis
        hiddenFeesTweets = twint.output.tweets_list
        for hiddenFeesTweet in hiddenFeesTweets[:]:
            if not UnitedAggregateModel.objects.filter(tweet_id=hiddenFeesTweet.id).exists(): # if new tweet
                DEEP_AI_KEY = os.getenv("DEEP_AI_KEY")
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': hiddenFeesTweet.tweet},
                            headers={'api-key': DEEP_AI_KEY})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = UnitedAggregateModel.objects.get_or_create(tweet_id=hiddenFeesTweet.id, name=str(hiddenFeesTweet.username), text=str(hiddenFeesTweet.tweet), link=str(hiddenFeesTweet.link), date=hiddenFeesTweet.datestamp, prediction_level=score, category="hidden-fees")

        # Update UnitedCondensedModel
        tweets = UnitedAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'hidden-fees':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = UnitedCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="hidden-fees")
