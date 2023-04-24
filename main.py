from flask import Flask

# need to create a application and application is application is simply a object of class Flask
# __name__ how a particular script is invoked
app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello World</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
