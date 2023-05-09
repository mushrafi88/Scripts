import json

# Define the file paths
playlists_file = '/home/venerable_white/.Harmonoid/Playlists.JSON'
tracks_file = '/home/venerable_white/.Harmonoid/Tracks.JSON'

# Load the playlist file
with open(playlists_file, 'r') as f:
    playlists_data = json.load(f)

# Load the tracks file
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

# Function to check if the track already exists in the playlist
def track_exists(playlist, track):
    for existing_track in playlist['tracks']:
        if existing_track['uri'] == track['uri']:
            return True
    return False

# Loop through the tracks and add them to the appropriate playlist if they don't already exist
for track in tracks_data['tracks']:
    if 'file:///mnt/media_m/Music/Selection/youtube/' in track['uri']:
        # Add to the youtube playlist
        for playlist in playlists_data['playlists']:
            if playlist['name'] == 'youtube':
                if not track_exists(playlist, track):
                    playlist['tracks'].append(track)
    elif 'file:///mnt/media_m/Music/Selection/Anime/' in track['uri']:
        # Add to the Anime playlist
        for playlist in playlists_data['playlists']:
            if playlist['name'] == 'Anime':
                if not track_exists(playlist, track):
                    playlist['tracks'].append(track)

# Save the updated playlists_data to the playlist file
with open(playlists_file, 'w') as f:
    json.dump(playlists_data, f, indent=4)

