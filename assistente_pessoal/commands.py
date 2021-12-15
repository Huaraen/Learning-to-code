import webbrowser as browser

def trigger(trigger): 
  # Hora
    if "fogo" in trigger:
        "fire()"
    elif "command" in trigger:
        input =  "Que horas são"
        entity =  "time"
        action = "getTime()"
    elif "command" in trigger:
        input =  "Me digas horas"
        entity = "time"
        action = "getTime()"
    elif "command" in trigger:
        input =  "Eu quero saber as horas"
        entity = "time"
        action = "getTime()"
  # Data
    elif "command" in trigger:
        input =  "Qual é a data de hoje"
        entity = "time"
        action = "getDate()"
    elif "command" in trigger:
        input =  "Data de hoje"
        entity = "time"
        action = "getDate()"
  # Tempo
    elif "command" in trigger:
        input =  "Previsão do tempo"
        entity = "weather"
        action = "getWeather()"
    elif "command" in trigger:
        input =  "Como está o clima?"
        entity = "weather"
        action = "getWeather()"
    elif "command" in trigger:
        input =  "Abrir google"
        entity = "open"
        action = ""     
    elif "command" in trigger:
        input =  "Abrir google"
        entity = "open"
        action = ""
    elif "command" in trigger:
        input =  "Abra youtube"
        entity = "open"
        action = "url" 
  # Playlist
    elif "toca" & "anime" in trigger:
        playlist ("anime")
    elif "toca" & "bad apple" in trigger:
        playlist ("bad_apple")

def playlist (album):
    if album == "bad_apple":
        browser.open("https://open.spotify.com/track/3urItfkvXw8tPjwNs2lXdd?si=06f4bc2e97174db7")
    elif album == "anime":
        browser.open("https://open.spotify.com/playlist/3lsfveO1cBycWxcjbQ54Gw?si=d7fcc215816747ac")
