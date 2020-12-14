import sys
from youtubesearchpython import SearchVideos

search_term = sys.argv[1]

search = SearchVideos(search_term, offset = 1, mode = "json", max_results = 20)

#json_str = search.result()
titles = search.titles

for title in titles:
    print(title)