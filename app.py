from flask import Flask
app = Flask(__name__)

@app.route("/")
def login():
    return '''
    <html>
        <head>
            <title>Flask App</title>
        </head>
        <body>
        <center> <h1> Welcome to Login Page </h1> </center>
        <form>
            <label>Username: </label>
            <input type=text name="uname">
            <br><br>
            <label>Password: </label>
            <input type=password name="pwd">
            <br><br>
            <label>Remember me: </label>
            <input type="checkbox">
        
            <br><br>
            <input type="button" name="Login" id="login" value="Login">       
            <input type="button" name="cancel" id="cancel" value="Cancel">
            <br><br>
            <span class="psw">Forgot <a href="#">password?</a></span>
        </form>
        </body>
    </html>
    '''
