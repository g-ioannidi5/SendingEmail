import webapp2

from emailsender import EmailSender
from google.appengine.ext import db

class ReviewHandler(webapp2.RequestHandler):

  def post(self):
    ratingValue = self.request.get('review.reviewRating.ratingValue')
    reviewBody = self.request.get('review.reviewBody')

    # the numeric rating is required
    if not ratingValue:
      self.error(400)
      return

    # insert the review into the Datastore
    review = Review(ratingValue=int(ratingValue), reviewBody=reviewBody)
    review.put()

  def get(self):
    # retrieve up to 1000 reviews from the Datastore
    reviews = Review.all().fetch(1000)

    if not reviews:
      self.response.write('No reviews')
      return

    total = 0
    count = len(reviews)

    for r in reviews:
      total += r.ratingValue
      reviewBody = r.reviewBody or 'No feedback'
      self.response.write('%d/5 - %s<br/>' % (r.ratingValue, reviewBody))

    self.response.write('<br/>')
    self.response.write('%d reviews - Average rating %.2f/5' % (count, total/float(count)))

class Review(db.Model):
    ratingValue = db.IntegerProperty(required=True)
    reviewBody = db.TextProperty(required=False)