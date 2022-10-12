from flask import Flask, request, render_template, jsonify
from flask.wrappers import Response
import git
from second import returnNameCombination

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
  return render_template("twoInputs.html")


@app.route('/square/', methods=['POST']) 
def square(): 
	num = float(request.form.get('number', 0)) 
	square = num ** 2 
	data = {'square': square} 
	data = jsonify(data) 
	return data 


@app.route('/twos', methods=['GET','POST'])
def receiveAndReturn():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
	output = returnNameCombination(firstname, lastname)
	
	
        if firstname and lastname:
            return jsonify({'output':'Your Name is ' + output + ', right?'})
        return jsonify({'error' : 'Missing data!'})
    return render_template('twoInputs.html')
 
if __name__ == '__main__': 
	app.run(debug=True)
