<h1> 🔑 Session Manager | Flask </h1>
<h3> 📀 Last Update: 12/23/2021, 2:34 PM GMT+1</h3>

<h5> Session is a Session Managment Plugin to improve your Session Managment in Flask, to set it up
 you just have to initialize it with a token and assign it to the default session object in flask, here's
 an example: </h5>
 
> import sessionOffedul <br>
> from flask import Flask, session <br> <br>
> 
> app = Flask(__name__) <br>
>
> @app.route("/") <br>
> def init(): <br>
> 	   sessionOffedul.InitializeSession("your token goes here") <br>
> 	   session['session'] = sessionOffedul.GetSession() <br>

<h3> ✅ Installation </h3>

> pip install sessionOffedul==0.4

<h3> 👘 Create Object </h3>

> sessionOffedul.CreateObject("selection", "top", str) <br>
> sessionOffedul.CreateObject("selection", ["top", "left", "right"], list) <br>
> sessionOffedul.CreateObject("selection", 43, int) <br>
> sessionOffedul.CreateObject("selection", {"faces": ['top': false, 'right': false]}, tuple) <br>

<h3> 👘 Update Session </h3>

<h5> Once you add an object to the session you must remember to update the session, to do so follow the following example: </h5>

> sessionOffedul.UpdateSession() <br>
> session['session'] = sessionOffedul.GetSession() <br>

<h3> 👘 Print on file or convert Json to Session Object </h3>

<p> With PrintContentOnFile function you can write on a file the prettified json on a file, oh did I mention it? This plugin supports json! You can load objects with a json format, to do so, follow the example: <p>

> jsonExample = { <br>
> "name": "selection", <br>
> "value": "top", <br>
> "type": "String" <br>
> } <br><br><br><br> 
> obj = sessionOffedul.ConvertJsonToObject(jsonExample) <br>
> sessionOffedul.AddJson(obj) <br>
