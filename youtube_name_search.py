import sys
from youtube_search import YoutubeSearch

search_term = sys.argv[1]


results = YoutubeSearch(search_term, max_results=13).to_dict()
for i in range(13):
    print(results[i]['title'])

