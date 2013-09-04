from bottle import route, run, request, redirect
import cgi

form = """
<form method="post">
What is your birthday?
<br>
<label>Month<input type="text" name="month" value="{month}"></label>
<label>Day<input type="text" name="day" value="{day}"></label>
<label>Year<input type="text" name="year" value="{year}"></label>
<div style='color: red'>{error}</div>
<br>
<br>
<input type="submit">
</form>
"""

def write_form(error='',month='',day='',year=''): # string substitution
	return form.format(**{'error':escape_html(error), # needs expanding **
						  'month':escape_html(month),
						  'day':escape_html(day),
						  'year':escape_html(year)})

def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if day>0 and day<=31:
			return day

def valid_month(month):
	months = ["January","February","March","April","May","June","July",
				"August","September","October","November","December"]
	months_d = {m[:3].lower():m for m in months}
	
	if month and month.isalpha():
		return months_d.get(month[:3].lower())

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year>1900 and year<2020:
			return year

def escape_html(s): # to escape html code in user input
    return cgi.escape(s, quote=True) # uses built-in python module

@route('/', method="GET")
def hello():
	return write_form()
@route('/', method="POST")
def hello():
	user_month = request.POST.get("month")
	user_day = request.POST.get("day")
	user_year = request.POST.get("year")

	month = valid_month(user_month)
	day = valid_day(user_day)
	year = valid_year(user_year)

	if not (month and day and year):
		return write_form("OH SHIT",user_month,user_day,user_year)
	else:
		redirect('/thanks') # redirect to thanks page

@route('/thanks', method="GET")
def thanks():
	return "Thanks!  That's a totally valid day!"

run(host='0.0.0.0', port=8080)
