from django.core.management.base import BaseCommand
from ...models import JetblueAggregateModel, JetblueCondensedModel
from django.utils import timezone

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain legroom-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#jetblue legroom"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update JetblueAggregateModel and DeepAI sentiment analysis
        legroomTweets = twint.output.tweets_list
        for legroomTweet in legroomTweets[:]:
            if not JetblueAggregateModel.objects.filter(tweet_id=legroomTweet.id).exists(): # if new tweet
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': legroomTweet.tweet},
                            headers={'api-key': '98f982f3-91a3-4081-94ef-3249f5cebf89'})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = JetblueAggregateModel.objects.get_or_create(tweet_id=legroomTweet.id, name=str(legroomTweet.username), text=str(legroomTweet.tweet), link=str(legroomTweet.link), date=legroomTweet.datestamp, prediction_level=score, category="legroom")

        # Update JetblueCondensedModel
        tweets = JetblueAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'legroom':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = JetblueCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="legroom")