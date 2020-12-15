### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
    - JavaScript uses curly braces and Python uses indentation.
    - JavaScript runs files in the browser while Python runs files on the server through the command line (then it can be rendered on a browser).
    - JavaScript is better for mobil.
    - JavaScript helps you build a website or native application while Python is used for tasks related to data analytics, machine learning, and math-intensive operations.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
    - {"a": 1, "b": 2}.get("c")
    - my_dict\['c'] if 'c' in my_dict else None

- What is a unit test?
    - It is a test that checks that each individual function is doing what you expect it to do.

- What is an integration test?
    - It is a test that checks that all the functions of the application work together as expected.

- What is the role of web application framework, like Flask?
    - Web application frameworks are built on top of other languages but they reduce the amount of code needed to get desired results. Flask, in particular, is a server-side web app framework. Server-side frameworks keep the logic on the back-end, which means that requests are processed on the server (server side scripts).

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    - '/foods/pretzel' is going to create a dedicated route for those parameters. This is a better choice if you needed to render a specific template dedicated to pretzel with different logic in the view function from other food options/routes. If there is going to be more than one option for foods but the logic for any given food item passed in the parameters is the same, it is okay to handle the logic in the same route.
  
- How do you collect data from a URL placeholder parameter using Flask?
    - you pass the placeholder parameter to the view function which makes the value available inside the view function.
  
- How do you collect data from the query string using Flask?
    - from flask import request. Then, inside the view function save request.args\['whatever_arg'] to a variable.

- How do you collect data from the body of the request using Flask?
    - request.data, request.json, request.form\['whatever_arg']

- What is a cookie and what kinds of things are they commonly used for?
    - Is a way to collect and save info in the browser reagarding the state of the client's activity. The browser tells the client to store these cookies and the client sends the cookies to the browser with each request so the browser knows how to respond to the particular client.
  
- What is the session object in Flask?
    - Is a dictionary built on top of cookies that stores information for the current browser (current state). It is stored criptographically but can be accessed and shared globally accross your application and in templates using jinja. 

- What does Flask's `jsonify()` do?
    - It returns a flask response object formatting a Python dictionary to json 