from bottle import route, run, request, redirect
import cgi

form = """
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
	<br>
	<textarea name="text"
		      style="height: 100px; width: 400px;">{input}</textarea>
	<br>
	<input type="submit">
	</form>
  </body>
</html>
"""

def write_form(input=''): # string substitution
	return form.format(**{'input':escape_html(input)})

def encrypt(s):
	chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
		   'p','q','r','s','t','u','v','w','x','y','z']
	output = ''
	for char in s:
		if char.lower() in chars:
			newchar = chars[(chars.index(char.lower())+13) % 26]
			if char.isupper():
				newchar=newchar.upper()
			output += newchar
		else:
			output += char
	return output

def escape_html(s): # to escape html code in user input
    return cgi.escape(s, quote=True) # uses built-in python module

@route('/rot13', method="GET")
def rot():
	return write_form()
@route('/rot13', method="POST")
def rot():
	user_text = request.POST.get("text")

	rotted = encrypt(user_text)

	return write_form(rotted)

run(host='0.0.0.0', port=8080)


#this is a test
# This is another test
