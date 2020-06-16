from django.core.management.base import BaseCommand

import json
import twint
import os
import pathlib

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain time-related tweets.'
    
    def handle(self, *args, **options):
        if os.path.exists("TimeTweets/tweets.json"):
            path = pathlib.Path("TimeTweets/tweets.json")
            path.unlink()

        c = twint.Config()
        c.Search = "#jetblue time"
        c.Limit = 5
        c.Store_json = True
        c.Output = "TimeTweets"

        # Run
        twint.run.Search(c)