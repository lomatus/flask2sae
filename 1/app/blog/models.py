#models.py
from app import db

class Entry(db.Model):
	'''SQLAlchemy'''
	__tablename__ = 'entries'
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(80),nullable=False)
	text = db.Column(db.Text(),nullable=False)
	"""docstring for entries"""
	def __init__(self, title, text):
		self.title = title
		self.text = text

	def __repr__(self):
		return '<Entry('%r','%r','%r')>' % (self.id, self.title, self.text)

	def delete_by_id(self):
		db.session.delete(self)
		db.session.commit()