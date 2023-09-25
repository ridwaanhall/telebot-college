import os

import requests

token = os.environ['TELEGRAM_BOT_TOKEN']



def generate_answer(message):
  if message == message:
    url_new = f'https://api-frontend.kemdikbud.go.id/hit_mhs/{message}'
    response = requests.get(url_new)

    if response.status_code == 200:
      info = response.json()
      
      # Extract the relevant data from the JSON response
      data = info.get('mahasiswa', [])
      if data:
        result = []
        for item in data:
          result.append(item.get('text', ''))
        return '\n'.join(result)
      else:
        return "No data available."
    else:
      return {"error": "Unable to fetch data from the URL."}
  
  return "Invalid command."


def message_parser(message):
  chat_id = message['message']['chat']['id']
  if 'text' in message['message']:
    text = message['message']['text']
    print("Chat ID: ", chat_id)
    print("Message: ", text)
    return chat_id, text
  else:
    print("Chat ID: ", chat_id)
    print("Message does not contain text.")
    return chat_id, "Message does not contain text."


def send_message_telegram(chat_id, text):
  url = f'https://api.telegram.org/bot{token}/sendMessage'
  payload = {'chat_id': chat_id, 'text': text}
  response = requests.post(url, json=payload)
  return response