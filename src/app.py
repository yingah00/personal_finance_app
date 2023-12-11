#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <html>
     <head>
         <title>Personal Finance App</title>
         <style>
             body {
                 font-family: Arial, sans-serif;
                 background-color: #f2f2f2;
                 color: #333;
             }
             .container {
                 max-width: 600px;
                 margin: 0 auto;
                 padding: 20px;
                 background-color: #fff;
                 border: 1px solid #ccc;
                 box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                 border-radius: 5px;
             }
             h1 {
                 text-align: center;
                 color: #555;
             }
             label {
                 display: block;
                 margin-bottom: 10px;
                 color: #555;
             }
             input[type="text"] {
                 width: 100%;
                 padding: 10px;
                 font-size: 16px;
                 border-radius: 5px;
                 border: 1px solid #ccc;
             }
             input[type="submit"] {
                 width: 100%;
                 padding: 10px;
                 font-size: 16px;
                 background-color: #4caf50;
                 color: #fff;
                 border: none;
                 border-radius: 5px;
                 cursor: pointer;
             }
         </style>
     </head>
     <body>
         <div class="container">
             <h1>Personal Finance App</h1>
             <form action="/echo_user_input" method="POST">
                 <label for="user_input">Enter your expense:</label>
                 <input name="user_input" id="user_input" type="text">
                 <input type="submit" value="Submit!">
             </form>
         </div>
     </body>
     </html>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return '''
     <html>
     <head>
         <title>Personal Finance App - Result</title>
         <style>
             body {
                 font-family: Arial, sans-serif;
                 background-color: #f2f2f2;
                 color: #333;
             }
             .container {
                 max-width: 600px;
                 margin: 0 auto;
                 padding: 20px;
                 background-color: #fff;
                 border: 1px solid #ccc;
                 box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                 border-radius: 5px;
             }
             h1 {
                 text-align: center;
                 color: #555;
             }
             p {
                 text-align: center;
                 font-size: 18px;
                 margin-bottom: 20px;
             }
             .result {
                 background-color: #f9f9f9;
                 padding: 10px;
                 border-radius: 5px;
                 border: 1px solid #ccc;
             }
         </style>
     </head>
     <body>
         <div class="container">
             <h1>Personal Finance App</h1>
             <p>You entered:</p>
             <div class="result">
                 <p>{}</p>
             </div>
         </div>
     </body>
     </html>
     '''.format(input_text)

if __name__ == "__main__":
    app.run()