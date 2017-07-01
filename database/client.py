import os
import csv
import json

from pymongo import MongoClient

mongodb_uri = os.environ['MONGODB_URI']

client = MongoClient(mongodb_uri)
