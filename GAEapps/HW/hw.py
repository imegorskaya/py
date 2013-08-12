__author__ = 'wombat'
from google.appengine.ext.webapp import util
from google.appengine.ext import webapp


class HwHandler(webapp.RequestHandler):
#todo clarify
    def get(self):
        self.response.out.write('Hi there!')
#    todo write doc comment
def main():
    application = webapp.WSGIApplication([('/', HwHandler)],
        debug=True)
    util.run_wsgi_app(application)



if __name__ == '__main__':
    main()
