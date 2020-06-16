from django.core.management.base import BaseCommand

import json
import twint
import os
import pathlib

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain availability-related tweets.'
    
    def handle(self, *args, **options):
        if os.path.exists("AvailabilityTweets/tweets.json"):
            path = pathlib.Path("AvailabilityTweets/tweets.json")
            path.unlink()

        c = twint.Config()
        c.Search = "#jetblue available"
        c.Limit = 5
        c.Store_json = True
        c.Output = "AvailabilityTweets"

        # Run
        twint.run.Search(c)