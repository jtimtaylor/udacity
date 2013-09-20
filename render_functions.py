from bottle import template
from db_functions import *
import re

### RENDER FUNCTIONS ###

def render_blog(blogposts=""):
    return template('blog', blogposts=blogposts)

def render_newpost(subject="",content="",error=""):
    return template('newpost', subject=subject, content=content, error=error)

def render_entry(entryid=99999):
    blogpost = get_blogpost(entryid)
    return template('entry', blogpost=blogpost)

def render_signup(username="",email="",username_error="",password_error="",password_mismatch_error="",email_error=""):
    return template('signup', username=username,email=email,username_error=username_error,password_error=password_error,password_mismatch_error=password_mismatch_error,email_error=email_error)

def render_welcome(username=""):
    return template('welcome', username=username)

def render_login(username="",username_error="",password_error=""):
    return template('login', username=username, username_error=username_error, password_error=password_error)

### INPUT VALIDATION FUNCTIONS ###
def valid_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

def existing_username(username):
    return lookup_user_by_username(username)

def valid_password(password):
    USER_RE = re.compile(r"^.{3,20}$")
    return USER_RE.match(password)

def valid_match(password,verify):
    return password==verify

def valid_email(email):
    USER_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    return USER_RE.match(email)


