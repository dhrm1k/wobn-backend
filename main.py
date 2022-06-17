from flask import Flask, request,jsonify, send_from_directory, redirect
import json
import os

app = Flask(__name__)

@app.route('/')
def data():
  return send_from_directory('', 'posts.json')

@app.route('/post', methods=["POST", "GET"])
def testpost():
  thoughts = request.form.get('thoughts')
  
  strthoughts = str(thoughts)

    
  entry = strthoughts
  if entry != "None" and len(entry) != 0:
    filename = 'posts.json'

      # 1. Read file contents
    with open(filename, "r") as file:
      data = json.load(file)
      #This code checks if the post inputted before and after is not the same. If it's the same, it will not get inserted.
      lenofall = len(data['thoughts'])

      if lenofall > 0: #0 cause 1 will look for second input.
        if data['thoughts'][0] != entry:
            data['thoughts'].insert(0, entry)
      else:
        data['thoughts'].insert(0, entry)

      # 3. Write json file
      with open(filename, "w") as file:
        json.dump(data, file)
        
      return redirect(request.referrer)
  

app.run(host='0.0.0.0', port=81)