import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/photos.html')
        options = {'title': 'Photos', 'path': self.request.path}
    	self.response.write(template.render(options))
    def post(self):
        name = self.request.get('name')
        password = self.request.get('password')
        if name == 'Colleen' and password == 'pass':
            template = JINJA_ENVIRONMENT.get_template('templates/photos.html')
            self.response.write(template.render())
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/photos.html')
            
            print name
            print password

            options = {
                'error': 'Invalid input. Enter again.'
            }
            self.response.write(template.render(options))

class OneHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.path == "/myresume.html":
            template = JINJA_ENVIRONMENT.get_template('templates/myresume.html')
        
            options = {
                'title': 'Resume',
                'path': self.request.path,
            }
            self.response.write(template.render(options))
        elif self.request.path == "/mybio.html":
            template = JINJA_ENVIRONMENT.get_template('templates/mybio.html')
        
            options = {
                'title': 'Bio',
                'path': self.request.path
            }
            self.response.write(template.render(options))
        elif self.request.path == "/home.html":
            template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        
            options = {
                'title': 'Home',
                'path': self.request.path
            }

            self.response.write(template.render(options))
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.path == '/':
            template = JINJA_ENVIRONMENT.get_template('templates/home.html')

            options = {
                'title': 'Home',
                'path': self.request.path
            }

            self.response.write(template.render(options))
        
    
app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/myresume.html', OneHandler),
    ('/mybio.html', OneHandler),
    ('/home.html', OneHandler),
    ('/photos.html', LoginHandler)
], debug=True)
