import webapp2

from emailsender import EmailSender
from review import ReviewHandler

app = webapp2.WSGIApplication([('/', ReviewHandler), ('/email', EmailSender)], debug=True)