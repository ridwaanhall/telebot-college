from flask import Flask, Response, request

from Controller.FunctionController import (
    generate_answer,
    message_parser,
    send_message_telegram,
    send_photo_telegram,
)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    msg = request.get_json()
    chat_id, incoming_que = message_parser(msg)
    answer = generate_answer(incoming_que)

    if answer.startswith('http'):
      send_photo_telegram(chat_id, answer)
    else:
      send_message_telegram(chat_id, answer)
    return Response('ok', status=200)
  else:
    return "<h1>Something went wrong</h1>"