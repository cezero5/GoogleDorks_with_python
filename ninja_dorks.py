from dotenv import load_dotenv
import os
from google_search import GoogleSearch

load_dotenv()

API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

query = 'filetype:sql intext:password | pass | passwd intext:username intext:INSERT INTO `users` VALUES'

gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)

results = gsearch.search(query)

print(results)