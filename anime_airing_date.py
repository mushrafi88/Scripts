import requests
from dateutil.parser import parse
from datetime import datetime
import os

def seconds_to_human_readable(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return f"{days}d {hours:02}h {minutes:02}m {seconds:02}s"

anime_directory = "/mnt/media_m/Anime/Airing/"
anime_folders = os.listdir(anime_directory)
anime_list = [folder for folder in anime_folders if folder not in [".stfolder", "dl.txt"]]

api_url = "https://graphql.anilist.co"

query = """
query ($search: String) {
  Media (search: $search, type: ANIME) {
    title {
      romaji
    }
    nextAiringEpisode {
      airingAt
      timeUntilAiring
      episode
    }
  }
}
"""

def get_next_episode_release(search):
    variables = {"search": search}
    response = requests.post(api_url, json={"query": query, "variables": variables})
    data = response.json()
    
    if "errors" in data:
        print(f"Error fetching data for '{search}': {data['errors'][0]['message']}")
        return None

    media = data["data"]["Media"]
    title = media["title"]["romaji"]
    next_episode = media["nextAiringEpisode"]

    if next_episode:
        airing_at = parse(datetime.fromtimestamp(next_episode["airingAt"]).isoformat())
        time_until_airing = next_episode["timeUntilAiring"]
        episode = next_episode["episode"]
        return (title, airing_at, episode, time_until_airing)
    else:
        return (title, None, None, None)

# Fetch the next episode release data and store it in a list
anime_data = [get_next_episode_release(anime_title) for anime_title in anime_list]

# Sort the list by the time until the next episode
sorted_anime_data = sorted(anime_data, key=lambda x: x[3] if x[3] is not None else float("inf"))

# Format and print the sorted list
output_lines = []
for title, airing_at, episode, time_until_airing in sorted_anime_data:
    if airing_at:
        human_readable_time = seconds_to_human_readable(time_until_airing)
        output_lines.append(f"{title: <40} | Episode {episode: <3} | {human_readable_time}")
    else:
        output_lines.append(f"{title: <40} | No next airing episode found")

print("\n".join(output_lines))

