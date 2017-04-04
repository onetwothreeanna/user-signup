import webapp2
import cgi

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
        signup_form = """
            <form action = "/welcome" method = "post">
                <table style="width:100%">
                    <tr>
                        <td>
                            <label>
                                Username:
                                <input type = "text" name = "username"/>
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
                                <input type = "text" name = "email"/>
                            </label>
                        </td>
                    </tr>

                </table>
                <input type = "submit"/>
            </form>
        """
        content = page_header + signup_form + page_footer
        self.response.write(content)


class Welcome(webapp2.RequestHandler):
    """ Handles requests coming from form """

    def post(self):
        #retrieve user input
        username = self.request.get("username")
        password = self.request.get("password")
        verifypassword = self.request.get("verifypassword")
        email = self.request.get("email")

        #check if username, pw, or verify are left blank.  redirects to form
        if username == "" or password == "" or verifypassword =="":
            self.redirect("/")

        self.response.write("<h1> Welcome, " + username + "!")

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
