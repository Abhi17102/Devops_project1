from flask import Flask

github=Flask(_name_)

@github.route("/info")
def myinfo():
	return "i am Abhishek"


@github.route("/phone")
def myphone():
	return "1234567890"

github.run(host="0.0.0.0")
