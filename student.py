from flask import Flask
app=Flask(__name__)

@app.route('/')
def first():
    return "hell0"
app.run(debug=True)