#!/system/bin/sh

# Live Captions
device_config put device_personalization_services Captions__manifest_url_template 'https://storage.googleapis.com/captions/%{NAMESPACE}_%{VERSION}_manifest.json'
device_config put device_personalization_services Captions__model_version_v1 '20190613'
device_config put device_personalization_services Captions__model_version_v1_2 '20200112'
device_config put device_personalization_services Captions__speech_threshold '0.2'
device_config put device_personalization_services Captions__surface_sound_events 'true'
device_config put device_personalization_services Captions__visibility_playing_duration_millis '5000'
device_config put device_personalization_services Captions__visibility_stopped_duration_millis '1500'

# Now Playing
device_config put device_personalization_services NowPlaying__ambient_music_index_manifest_17_09_02 '148:https://storage.googleapis.com/music-iq-db/updatable_db_v2/20201006-025738/manifest.json'
