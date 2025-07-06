from flask import Flask

app=Flask(_name_)

@app.route("/info")
def myinfo():
	return "i am Abhishek"


@app.route("/phone")
def myphone():
	return "1234567890"

app.run(host="0.0.0.0")