import sys
from youtube_search import YoutubeSearch

search_term = sys.argv[1]
sorted_term = sys.argv[2]


results = YoutubeSearch(search_term, max_results=13).to_dict()
for i in range(13):
    if results[i]['title'] == sorted_term:
    	print('https://www.youtube.com'+results[i]['url_suffix'])    
