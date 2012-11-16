import sae
from app import app
import os
if 'SERVER_SOFTWARE' in os.environ:
	print 'Production Mode Working now...Mysql works too.'
	app.config.from_object('app.config.ProductionConfig')
else:
	print 'develop mode'
	app.config.from_object('app.config.DevelopmentConfig')

application = sae.create_wsgi_app(app)