from app import app,db
from flask import Blueprint,render_template,request,session,flash,redirect,url_for,abort
from app.blog.models import Entry

mod = Blueprint('blog', __name__, url_prefix='/blog')

@app.route('/')
def show_entries():
	entries = Entry.query.order_by('id')
	return render_template('blog/show_entries.html', entries = entries)

@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	title = request.form['title']
	text = request.form['text']
	if title != '' and text != '' :
		entry = Entry(title,text)
		db.session.add(entry)
		db.session.commit()
		flash('New entry was successfully posted')
	else:
		flash('Error:Empty title or text')
	return redirect(url_for('show_entries'))

@app.route('/delete/<int:entry_id>', methods=['GET'])
def del_entry(entry_id):
	if not session.get('logged_in'):
		abort(401)
	entry = Entry.query.filter_by(id=entry_id).first()
	if entry:
		entry.delete_by_id()
		flash('The entry was successfully deleted')
	return redirect(url_for('show_entries'))

@app.route('/edit/<int:entry_id>', methods=['GET','POST'])
def edit_entry(entry_id):
	if not session.get('logged_in'):
		abort(401)
	entry = Entry.query.filter_by(id=entry_id).first()
	if request.method == 'POST':
		Entry.query.filter_by(id=entry_id).update({Entry.title:request.form['title'],Entry.text:request.form['text']})
		db.session.commit()
		return redirect(url_for('show_entries'))
	return render_template('blog/edit.html', entry=entry)

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error =  'Invalid username'
		elif request.form['password'] != app.config[ 'PASSWORD' ]:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged_in')
			return redirect(url_for('show_entries'))
	return render_template('blog/login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))
		
