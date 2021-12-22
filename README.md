<h1> Session Manager | Flask </h1>
<h3> Last Update: 12/22/2021, 22:32 PM GMT+1</h3>

<h5> Session is a Session Managment Plugin to improve your Session Managment in Flask, to set it up
 you just have to initialize it with a token and assign it to the default session object in flask, here's
 an example: </h5>
 
> import objectmanager <br>
> from flask import Flask, session <br> <br>
> 
> app = Flask(__name__) <br>
>
> @app.route("/")
> def init(): <br>
> 	   objectmanager.InitializeSession("your token goes here") <br>
> 	   session['session'] = objectmanager.GetSession() <br>

<h3> Add Object to Session </h3>
<h4> Returns the created object </h4>

> objectmanager.CreateObject("selection", "top", str) <br>
> objectmanager.CreateObject("selection", ["top", "left", "right"], list) <br>
> objectmanager.CreateObject("selection", 43, int) <br>
> objectmanager.CreateObject("selection", {"faces": ['top': false, 'right': false]}, tuple) <br>

<h3> Update Session </h3>

<h5> Once you add an object to the session you must remember to update the session, to do so follow the following example: </h5>

> objectmanager.UpdateSession() <br>
> session['session'] = objectmanager.GetSession() <br>

<h3> Print on file or convert Json to Session Object </h3>

<h5> With PrintContentOnFile function you can write on a file the prettified json on a file, oh did I mention it? This plugin supports json! You can load objects with a json format, to do so, follow the example: </h5>

> jsonExample = { <br>
> "name": "selection", <br>
> "value": "top", <br>
> "type": "String" <br>
> } <br><br>
> obj = objectmanager.ConvertJsonToObject(jsonExample) <br>
> objectmanager.AddJson(obj) <br>
