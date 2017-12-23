from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Method used: %s" % request.method # this will show the method used by http to reach the route

@app.route('/hello/')
def hello():
    return render_template('htm.html') #here we ask Flask to use the template when the URL /hello is typed

@app.route('/hey/')
@app.route('/hey/<name>')
def hey(name='Vasya'):
    return render_template('hey.html', name='Vasya')



@app.route('/method', methods = ['GET', 'POST'])
def method_used():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"


@app.route('/user/<username>') # here we pass variable to the URL
def show_user_profile(username):
    # show the user profile for that user
    return 'User {}'.format(username)

@app.route('/post/<post_id>')
def show_post(post_id):
    return 'Post %s' % post_id

with app.test_request_context(): # here and below we ask the program to print URLs for all functions we have
    print (url_for('index'))
    print (url_for('show_user_profile', username = 'Igor'))
    print (url_for('show_post', post_id = '34'))
    print (url_for('method_used'))
if __name__ == '__main__':
    app.run()

