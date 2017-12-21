from flask import Flask,render_template,url_for,redirect
from flask import request
from flask import make_response
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

@app.route('/user/<username>')
def user_index(username):
    if username == 'invalid':
        abort(404)
    resp = make_response(render_template('user_index.html',username=username))
    resp.set_cookie('username',username)
    return resp

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
