from app import app
import os
if 'SERVER_SOFTWARE' in os.environ:
	print 'production'
	app.config.from_object('app.config.ProductionConfig')
else:
	print 'develop mode'
	app.config.from_object('app.config.DevelopmentConfig')

app.run(host='localhost',port=8888)