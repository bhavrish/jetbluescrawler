from django.core.management.base import BaseCommand
from ...models import AmericanAggregateModel, AmericanCondensedModel
from django.utils import timezone 

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain family-options-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#americanairlines family options"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update AmericanAggregateModel and DeepAI sentiment analysis
        familyOptionsTweets = twint.output.tweets_list
        for familyOptionsTweet in familyOptionsTweets[:]:
            if not AmericanAggregateModel.objects.filter(tweet_id=familyOptionsTweet.id).exists(): # if new tweet
                DEEP_AI_KEY = os.getenv("DEEP_AI_KEY")
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': familyOptionsTweet.tweet},
                            headers={'api-key': 'DEEP_AI_KEY'})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = AmericanAggregateModel.objects.get_or_create(tweet_id=familyOptionsTweet.id, name=str(familyOptionsTweet.username), text=str(familyOptionsTweet.tweet), link=str(familyOptionsTweet.link), date=familyOptionsTweet.datestamp, prediction_level=score, category="family-options")

        # Update AmericanCondensedModel
        tweets = AmericanAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'family-options':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = AmericanCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="family-options")