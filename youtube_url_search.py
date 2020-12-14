import sys
from youtubesearchpython import SearchVideos

search_term = sys.argv[1]
sorted_term = sys.argv[2]


search = SearchVideos(search_term, offset = 1, mode = "json", max_results = 20)

#json_str = search.result()
titles = search.titles
links = search.links
#view = search.views
#thumbnail_link = search.thumbnails

d = dict(zip(titles,links))

print(d[sorted_term])

