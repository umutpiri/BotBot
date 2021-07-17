from flask import Flask, request, Response
from threading import Thread
from replit import db


app = Flask('')

@app.route('/')
def home():
  return "Im alive!"

@app.route('/taboo', methods=['POST'])
def taboo():
  try:
    data = request.json
    for key in data.keys():
      if not key in db:
        db[key] = data[key]
    return Response(status=201)
  except:
    return Response(status=400)

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
