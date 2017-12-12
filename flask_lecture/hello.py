from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/buy')
def buy_world():
    return 'Good Buy :) !'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User name is <h1> {} </h1>'.format(username)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
