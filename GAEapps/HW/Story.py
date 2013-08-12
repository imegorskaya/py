from django.core.cache.backends import db

__author__ = 'wombat'
class Story(db.Model):
    title = db.StringProperty()
    body = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)
