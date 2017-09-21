from string import digits, ascii_letters, punctuation
from random import randint, choice
from tornado import ioloop, web

class MainHandler(web.RequestHandler):
    def get(self):
        self.render("templates/pass.html")

    def post(self):
        self.write(generatePassword())

def makeApplication():
    """"Create Web Application"""
    return web.Application([
        (r"/",MainHandler)
    ])

def generatePassword():
    """"Function generate password"""
    return "".join([choice(signs) for sign in range(randint(8, 16))])

if __name__ == "__main__":
    #GeneratePassword
    signs = digits + ascii_letters + punctuation
    #generatePassword()

    #Tornado
    application = makeApplication()
    application.listen(8888)
    ioloop.IOLoop.current().start()
