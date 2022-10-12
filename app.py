from flask import Flask, request, render_template, json
from flask.wrappers import Response
import git

app = Flask(__name__)

@app.route('/git-update', methods=['POST'])
def git_update():
  repo = git.Repo('./pyanywhere')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()                                
  origin.pull()
  return '', 200

@app.route('/')
def index():
  return render_template("json.html")

#background process happening without any refreshing
@app.route('/background_process_test', methods=['POST']) 
def background_process_test():
    print ("Hello")
    return ("nothing")
