import modules.web as web
operation={
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
def browser(command):
    for key,func in operation.items():
                if key in command:
                        func()
                        return
    print("Command not found...")