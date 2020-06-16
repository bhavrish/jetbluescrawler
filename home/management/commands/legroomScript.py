from django.core.management.base import BaseCommand

import json
import twint
import os
import pathlib

class Command(BaseCommand):
    help = 'Scrapes twitter.com to obtain legroom-related tweets.'
    
    def handle(self, *args, **options):
        if os.path.exists("LegroomTweets/tweets.json"):
            path = pathlib.Path("LegroomTweets/tweets.json")
            path.unlink()

        c = twint.Config()
        c.Search = "#jetblue legroom"
        c.Limit = 5
        c.Store_json = True
        c.Output = "LegroomTweets"

        # Run
        twint.run.Search(c)