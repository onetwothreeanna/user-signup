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
    font-style: oblique;

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
        content = page_header + "<h1> Signup </h1>" + signup_form + page_footer
        self.response.write(content)

class Welcome(webapp2.RequestHandler):
    """ Handles requests coming from form """

    def get(self):
        username = self.request.get("username")
        self.response.write("<h1> Welcome, " + username + "! </h1>")

        content = page_header + page_footer
        self.response.write(content)

    def post(self):
        #retrieve user input
        username = self.request.get("username")
        password = self.request.get("password")
        verifypassword = self.request.get("verifypassword")
        email = self.request.get("email")

        username_checks = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        username_okay = username_checks.match(username)

        email_checks = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        email_okay = email_checks.match(email)

        password_checks = re.compile(r"^.{3,20}$")
        password_okay = password_checks.match(password)

        if username == "" or password == "" or verifypassword =="":
            self.redirect("/")

        elif password != verifypassword:
            self.redirect("/")

        elif not username_okay:
            self.redirect("/")

        elif not email_okay:
            self.redirect("/")

        elif not password_okay:
            self.redirect("/")

        else:
            self.redirect("/welcome?username=" + username)




app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
