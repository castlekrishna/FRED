import modules.web as web
from modules.games_routing import games

# brower work
browsing={
    "youtube" : web.open_youtube,
    "google" : web.open_google,
    "drive" : web.open_drive,
    "whatsapp" : web.open_whatsapp,
    "chatgpt" : web.open_chatgpt,
    "docs" : web.open_docs,
    "sheet" : web.open_sheet,
    "github" : web.open_github,
    "telegram" : web.open_telegram
}


play_map = {
    "game" : games,
    "music" : web.play_music
}