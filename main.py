from flask import Flask

app = Flask("HelloWorld")

@app.route("/helloworld", methods=["GET"])

def helloworld():
    return{"Hello": "World"}


app.run()
