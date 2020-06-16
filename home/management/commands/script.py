from django.core.management.base import BaseCommand

import json
import twint
import os
import pathlib

class Command(BaseCommand):
    help = 'Scrapes spoj.com to obtain the details of all the classical problems.'
    
    def handle(self, *args, **options):
        if os.path.exists("CostTweets/tweets.json"):
            path = pathlib.Path("CostTweets/tweets.json")
            path.unlink()

        c = twint.Config()
        c.Search = "#jetblue cost"
        c.Limit = 5
        c.Store_json = True
        c.Output = "CostTweets"

        # Run
        twint.run.Search(c)