from flask import request, session, escape


class Utils:
    def isLoggedIn(self):
        if 'username' in session:
            return True
        else:
            return False


    def getUserName(self):
        if(self.isLoggedIn()):
            return session['username']
        else:
            return None


