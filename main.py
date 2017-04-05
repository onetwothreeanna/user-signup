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
    font-style: oblique;
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

.error{
    font-family: Helvetica;
    font-size: 14px;
    font-style: oblique;
    color: navy;
}
</style>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""

#Global function to build the form, taking in all values as parameters
def buildForm(username, email, error_username, error_password, error_verify, error_email):
    signup_form = """
        <form method = "post">
            <table style="width:100%">
                <tr>
                    <td>
                        <label>
                            Username:
                            <input type = "text" name = "username" value = "{0}"/>
                            <span class = error>{2}</span>
                        <label>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>
                            Password:
                            <input type = "password" name = "password"/>
                            <span class = error>{3}</span>
                        </label>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>
                            Verify Password:
                            <input type = "password" name = "verifypassword"/>
                            <span class = error> {4} </span>
                        </label>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>
                            Email (Optional):
                            <input type = "text" name = "email" value = "{1}"/>
                            <span class = error>{5}</span>
                        </label>
                    </td>
                </tr>

            </table>
            <input type = "submit"/>
        </form>
    """.format(username, email, error_username, error_password, error_verify, error_email)
    return signup_form



class Index(webapp2.RequestHandler):
    """ Handles requests coming to '/' (root site for signup)"""
#Upon request, build page with empty form
    def get(self):
        username = ""
        email = ""
        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""
        form = buildForm(username, email, error_username, error_password, error_verify, error_email)
        title = '<h1> Signup </h1>'
        content = (page_header + title + form + page_footer)
        self.response.write(content)

#Once submitted, retrieve input from user and start with empty errors
    def post(self):
        #retrieve user input
        username = self.request.get("username")
        password = self.request.get("password")
        verifypassword = self.request.get("verifypassword")
        email = self.request.get("email")
        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""

        #check for regular expressions
        username_checks = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        username_okay = username_checks.match(username)

        email_checks = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        email_okay = email_checks.match(email)

        password_checks = re.compile(r"^.{3,20}$")
        password_okay = password_checks.match(password)

        #check for plethora of errors, default to no errors
        errors = False

        #if errors = True, update error name to include message.
        if username == "" or not username_okay:
            error_username= "Please enter a valid username."
            errors = True

        elif password == "" or not password_okay:
            error_password=  "Please enter a valid password."
            errors = True

        elif password != verifypassword:
            error_verify=  "Passwords do not match."
            errors = True

        elif email != "" and not email_okay:
            error_email= "Please enter a valid email address."
            errors = True

        #if no errors, send to welcome page, including username
        if errors == False:
            self.redirect("/welcome?username=" + username)

        #if errors, rebuild form with populated fields using updated values
        else:
            form = buildForm(username, email, error_username, error_password, error_verify, error_email)
            title = '<h1> Signup </h1>'
            content = (page_header + title + form + page_footer)
            self.response.write(content)

class Welcome(webapp2.RequestHandler):
    """ Handles requests coming from form """

    def get(self):
        username = self.request.get("username")
        message = "<h1> Welcome, " + username + "! </h1>"
        content = page_header + message + page_footer
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
