from django.core.management.base import BaseCommand
from ...models import SpiritAggregateModel, SpiritCondensedModel
from django.utils import timezone 

import json
import twint
import os
import pathlib
import requests

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain reimbursement-related tweets.'
    
    def handle(self, *args, **options):
        # Twint tweet retrieval script
        c = twint.Config()
        c.Search = "#spiritairlines reimbursement"
        c.Limit = 5
        c.Store_object = True
        c.Hide_output = True
        twint.run.Search(c)
        
        # Update SpiritAggregateModel and DeepAI sentiment analysis
        reimbursementTweets = twint.output.tweets_list
        for reimbursementTweet in reimbursementTweets[:]:
            if not SpiritAggregateModel.objects.filter(tweet_id=reimbursementTweet.id).exists(): # if new tweet
                DEEP_AI_KEY = os.getenv("DEEP_AI_KEY")
                r = requests.post("https://api.deepai.org/api/sentiment-analysis",
                            data={'text': reimbursementTweet.tweet},
                            headers={'api-key': 'DEEP_AI_KEY'})
                resultJSON = r.json()
                resultOutput = resultJSON['output']
                score = 0
                for x in resultOutput:
                    if x == "Negative":
                        score-=1
                    elif x == "Positive":
                        score+=1
                    
                aggregateCreated = SpiritAggregateModel.objects.get_or_create(tweet_id=reimbursementTweet.id, name=str(reimbursementTweet.username), text=str(reimbursementTweet.tweet), link=str(reimbursementTweet.link), date=reimbursementTweet.datestamp, prediction_level=score, category="reimbursement")

        # Update SpiritCondensedModel
        tweets = SpiritAggregateModel.objects.all()
        score = 0
        count = 0
        for tweet in tweets:
            if tweet.category == 'reimbursement':
                score += tweet.prediction_level
                count += 1
        averageScore = 0
        if not count == 0:
            averageScore = score / count
        condensedCreated = SpiritCondensedModel.objects.get_or_create(date=timezone.now(), average_prediction=averageScore, category="reimbursement")