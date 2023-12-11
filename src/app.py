#!/usr/bin/env python3
#<link rel="stylesheet" type="text/css" href="style.css">

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
         <label for="user_input">Enter your expense:</label>
         <input name="user_input" id="user_input" type="text">
         <input type="submit" value="Submit!">
     </form>
     '''
@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text