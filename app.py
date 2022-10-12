from flask import Flask, request, render_template, jsonify
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
  return render_template("index.html")
