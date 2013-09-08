from bottle import route, run, request, redirect, template
import sqlite3

def create_db():
	con = sqlite3.connect('blogs.db')
	con.execute("CREATE TABLE blogs (id INTEGER PRIMARY KEY, title TEXT, entry TEXT, created TEXT)")

def write_form():
	def add_entry(title, entry):
	con = sqlite3.connect('blogs.db')
	con.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")

@route('/blog', method='GET')
def signup():
	return write_form()

@route('/blog', method='POST')
def signup():

@route('/newpost', method='GET')
def welcome(username=''):
	if request.GET.get('username'):
		username = request.GET.get('username')
	return 'Welcome, '+username+'!'


run(host='0.0.0.0', port=8080)
