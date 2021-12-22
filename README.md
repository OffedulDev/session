<h1> Session Manager | Flask </h1>
<h3> Last Update: 12/22/2021, 22:32 PM GMT+1</h3>

<h5> Session is a Session Managment Plugin to improve your Session Managment in Flask, to set it up
 you just have to initialize it with a token and assign it to the default session object in flask, here's
 an example: </h5>
 
> import objectmanager
> from flask import Flask, session
> 
> app = Flask(__name__)
>
> @app.route("/")
> def init():
> 	objectmanager.InitializeSession("your token goes here")


