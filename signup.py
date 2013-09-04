from bottle import route, run, request, redirect
import cgi
import re

form = """
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 - Sign Up</title>
    <style type="text/css">
      .label {{text-align: right}}
      .error {{color: red}}
    </style>
  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
	<table>
		<tr>
			<td class="label">
				Username
			</td>
			<td>
				<input type="text" name="username" value="{username}">
			</td>
			<td class="error">
				{username_error}
			</td>
		</tr>
		<tr>
			<td class="label">
				Password
			</td>
			<td>
				<input type="password" name="password" value="">
			</td>
			<td class="error">
				{password_error}
			</td>
		<tr>
			<td class="label">
				Verify Password
			</td>
			<td>
				<input type="password" name="verify" value="">
			</td>
			<td class="error">
				{password_mismatch_error}
			</td>
		</tr>
		<tr>
			<td class="label">
				Email (optional)
			</td>
			<td>
				<input type="text" name="email" value="{email}">
			</td>
			<td class="error">
				{email_error}
			</td>
		</tr>
	</table>
	<br>
	<input type="submit">
	</form>
  </body>
</html>
"""

def write_form(username='', username_error='', password_error='', password_mismatch_error='',email='',email_error=''): # string substitution
	return form.format(**{'username':username,
						  'username_error':username_error,
						  'password_error':password_error,
						  'password_mismatch_error':password_mismatch_error,
						  'email':email,
						  'email_error':email_error})

def escape_html(s): # to escape html code in user input
    return cgi.escape(s, quote=True) # uses built-in python module


def valid_username(username):
	USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
	return USER_RE.match(username)

def valid_password(password):
	USER_RE = re.compile(r"^.{3,20}$")
	return USER_RE.match(password)

def valid_match(password,verify):
	return password==verify

def valid_email(email):
	USER_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
	return USER_RE.match(email)

@route('/signup', method='GET')
def signup():
	return write_form()
@route('/signup', method='POST')
def signup():
	user_username = request.POST.get('username')
	user_password = request.POST.get('password')
	user_verify = request.POST.get('verify')
	user_email = request.POST.get('email')
	
	username=valid_username(user_username)
	password=valid_password(user_password)
	verify=valid_match(user_password,user_verify)
	email=valid_email(user_email)

	if not username:
		username_error='Not a valid username.'
	else:
		username_error=''
	if not password:
		password_error='Not a valid password.'
	else:
		password_error=''
	if not verify:
		password_mismatch_error='Passwords do not match.'
	else:
		password_mismatch_error=''
	if user_email:
		if not email:
			email_error='Email not valid.'
		else:
			email_error=''
	else:
		email = True
		email_error=''

	if not (username and password and verify and email):
		return write_form(user_username,username_error,password_error,password_mismatch_error,user_email,email_error)
	else:
		redirect('/welcome?username='+user_username) 

@route('/welcome', method='GET')
def welcome(username=''):
	if request.GET.get('username'):
		username = request.GET.get('username')
	return 'Welcome, '+username+'!'


run(host='0.0.0.0', port=8080)
