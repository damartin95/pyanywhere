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
  return render_template("json.html")

 
@app.route('/square/', methods=['POST']) 
def square(): 
	num = float(request.form.get('number', 0)) 
	square = num ** 2 
	data = {'square': square} 
	data = jsonify(data) 
	return data 
 
if __name__ == '__main__': 
	app.run(debug=True) 
