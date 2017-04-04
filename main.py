import webapp2
import cgi
import re

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title> User Signup </title>


<style>
h1{
    font-family: Helvetica;
    color: #4bdca3;
}
form{
    font-family: Helvetica;

}
tr, td {
    padding: 5px;
    text-align: left;
}
table {
    width: 100%;
}
</style>
</head>
<body>
    <h1> Signup </h1>
"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming to '/' (root site for signup)"""
    def get(self):
        username = self.request.get("username")
        email = self.request.get("email")
        signup_form = """
            <form action = "/welcome" method = "post">
                <table style="width:100%">
                    <tr>
                        <td>
                            <label>
                                Username:
                                <input type = "text" name = "username" value="{0}"/>
                            <label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Password:
                                <input type = "password" name = "password"/>
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Verify Password:
                                <input type = "password" name = "verifypassword"/>
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Email (Optional):
                                <input type = "text" name = "email" value="{1}"/>
                            </label>
                        </td>
                    </tr>

                </table>
                <input type = "submit"/>
            </form>
        """.format(username, email) # value leaves form populated if value exists  .format leaves user submitted values to keep fields populated
        content = page_header + signup_form + page_footer
        self.response.write(content)

class Welcome(webapp2.RequestHandler):
    """ Handles requests coming from form """
    def get(self):
        username = self.request.get("username")
        self.response.write("<h1> Welcome, " + username + "! </h1>")

    def post(self):
        #retrieve user input
        username = self.request.get("username")
        password = self.request.get("password")
        verifypassword = self.request.get("verifypassword")
        email = self.request.get("email")

        #check if username, pw, or verify are left blank.  redirects to form
        if username == "" or password == "" or verifypassword =="":
            self.redirect("/")

        else:
            self.redirect("/welcome?username=" + username)



app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
