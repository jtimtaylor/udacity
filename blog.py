from bottle import route, run, request, response, redirect, template, static_file
from render_functions import *
from encrypt_functions import *
from db_functions import *


@route('/blog', method='GET')
@route('/blog/')
def blog():
    blogposts = get_blogposts()
    return render_blog(blogposts)

@route('/blog/newpost', method='GET')
def newpost():
    return render_newpost()

@route('/blog/newpost', method='POST')
def newpost():
    user_subject = request.POST.get('subject')
    user_content = request.POST.get('content')

    if not (user_subject and user_content):
        error="You done goofed."
        return render_newpost(user_subject,user_content, error)
    else:
        add_entry(user_subject,user_content)
        entryid=str(get_last_blogpost()[0])
        redirect("/blog/"+entryid)

@route('/blog/<entryid:int>')
def perma_link(entryid=0):
    return render_entry(entryid)

@route('/blog/signup', method='GET')
def signup():
    return render_signup()
@route('/blog/signup', method='POST')
def signup():
    user_username = request.POST.get('username')
    user_password = request.POST.get('password')
    user_verify = request.POST.get('verify')
    user_email = request.POST.get('email')

    username=valid_username(user_username)
    new_user=existing_username(user_username)
    password=valid_password(user_password)
    verify=valid_match(user_password,user_verify)
    if user_email:
        email=valid_email(user_email)
    else:
        email=True

    args={}
    args['username'] = user_username
    args['email'] = user_email

    if not username:
        args['username_error']='Not a valid username.'
    if new_user:
        args['username_error']='User already exists.'
    if not password:
        args['password_error']='Not a valid password.'
    if not verify:
        args['password_mismatch_error']='Passwords do not match.'
    if user_email and not email:
        args['email_error']='Email not valid.'

    if not (username and password and verify and email):
        return render_signup(**args)
    else:
        h = make_hash(user_username,user_password) #create hash
        add_user(user_username,h,user_email) #add hash
        userid=str(lookup_user_by_username(user_username)[0]) #get userid val
        response.set_cookie('userid',userid+","+h,path='/') # set cookie
        redirect('/blog/welcome')

@route('/blog/welcome', method='GET')
def welcome(username=''):
    try:
        cookie = request.get_cookie('userid').split(',') #get cookie
        print(cookie)
        userid = cookie[0] #parse out userid
        h = cookie[1] #parse out hash
        user_record = lookup_user_by_id(userid) #get user record from db
        print(user_record)
        if not user_record:  #if user doesn't exist, redirect
            redirect('/signup')
        db_username = user_record[1] #if user exists, get username
        db_h = user_record[2]        # and hash
        if db_h == h:
            return 'Welcome, '+db_username+'!'
        else:
            print("Hash doesn't match")
            print(db_h)
            print(h)
            redirect('/blog/signup') #if hash doesn't match, redirect
    except:
        print("No cookie")
        redirect('/blog/signup') #if no cookie (or other errors), redirect

@route('/blog/login', method='GET')
def login():
    return render_login()
@route('/blog/login', method='POST')
def login():
    user_username = request.POST.get('username')
    user_password = request.POST.get('password')

    if existing_username(user_username):
        user_record = lookup_user_by_username(user_username)
        h = user_record[2]
        if valid_pw(user_username,user_password,h):
            userid=str(user_record[0]) #get userid val
            response.set_cookie('userid',userid+","+h,path='/') # set cookie
            redirect('/blog/welcome')
        else:
            password_error="Wrong password."
            return render_login(user_username,password_error)
    else:
        username_error="User does not exist.  Would you like to <a href='/blog/signup'>signup</a>?"
        return render_login(username_error=username_error)


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

create_db()

run(host='0.0.0.0', port=8080)
