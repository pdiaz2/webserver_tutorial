# Hot - topics

## Solved

- [x] Single quotes vs double quotes in python
  - Indifferent, just be consistent
- [x] Stop Intellisense being so fucking triggered
  - Have an answer ina a Coda
[x] Check HTML tags used in register.html
  - fieldset: for forms
  - legend: caption for fieldset element

## 5. HTTP

- [ ] 304 response from server `GET /static/main.css HTTP/1.1" 304`
- [ ] Difference between URI and URL
- [ ] Que shusha es el enctype en account.html

## 4. Server - Client

- [ ] __Where does the capturing of the information actually take place????????__
- [ ] __refresh distintos, uno carga la página y el otro no__
- [ ] __Check cmd when running the python to see all the requests that happen__

## 3. Decorators

- [x] Understand the app.route decorator (check Flask Doc)
  - I am calling the decorator @app and its route method everytime
  - The decorator is equivalent to this line: `func = my_decorator(func)` so it wrapps the function inside a decorator. Notice that the decorator __returns a function!!!!__, i.e., the decorated function `func`
  - That is equivalent to the @ syntax, i.e., when you see

  ```python
  @my_decorator
  def func():
    pass
  ```

  - you are looking at `func = my_decorator(func)`
  - So, what does route do?

  ```python
  @app.route('/endpoint')
  def this_function():
    pass
  ```

  - is equivalent to `this_function = app.route('/endpoint', this_function)`. And what does `route` do?
  - According to Flask documentation:

  > Here are the parameters that route() and add_url_rule() accept. The only difference is that with the route parameter the view function is defined with the decorator instead of the view_func parameter.
  >> __rule__: the URL rule as string
  >>
  >> __endpoint__: the endpoint for the registered URL rule. Flask itself assumes that the name of the view function is the name of the endpoint if not explicitly stated.
  >>
  >> __view_func__: the function to call when serving a request to the provided endpoint. If this is not provided one can specify the function later by storing it in the view_functions dictionary with the endpoint as key.

  - Therefore, `route` returns the function after doing a few things internally. Those things have to do with server side manipulation to "link"
  the function being decorated with the decorator.
  - The thing it does internally is call the `add_url_rule` method from Flask.
  - From Flask documentation:

  > Register a rule for routing incoming requests and building URLs. The route() decorator is a shortcut to call this with the view_func argument. These are equivalent:

  ```python
  @app.route("/")
  def index():
      ...
  def index():
      ...

  app.add_url_rule("/", view_func=index)
  ```

  - and therefore, the view function is the function called (in the above example, `index`). All that `routes` does is "link" the endpoint (the "/" par)
  with the view_function (for `route`, the chain of functions below it, in this case index) and __wrap the view function__ decorated (which is equivalente to returning it as `ìndex = app.route(endpoint, index)s`)

## 2. Flask

- [x] Understand the validate on submit
  - Checks `is_submitted` method of the `FlaskForm` class (checks for a PUSH request) and `is_validated` (long-tail)
- [ ] Necesito entender perfecto el flujo de flask, app, las funciones y los decoradores. No entiendo __perfecto__ como se ejecutan las cosas y en qué orden

  - `route` lo que hace es llamar varios métodos internamente. Entre ellos, está el `add_url_rule` que se encarga del tema de los endpoints y el GET method a ellos. De la documentación de la función en Flask:

  ```python
  The ``methods`` parameter defaults to ``["GET"]``. ``HEAD`` is
  always added automatically, and ``OPTIONS`` is added
  automatically by default.
  ```

  - Igual hay algo raro, porque el método `add_url_rule` no hace nada en realidad.

- [ ] __Entender bien el video 11 desde el minuto 30 en adelante__
- [x] La wea de retrievear parametros y el url_for (como sabe como construir la ruta)
  - From Flask documentation:
  
    > To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

  - Therefore, the `url_for` method gets __methods__ as the string arguments and a list of other arguments. If an argument of those __does not__ exist in the method declaration, it automatically links it to a query parameter in the URL

### Requests

- [x] Qué hace el request
  - Al final, lo que hace es interacturar con los métodos de HTTP para obtener sus argumentos, body, headers, etc.

### Responses

### SQL and SQLAlchemy

- [ ] SQLAlchemy call and parameters (primary_key)
- [ ] check the db.relationship thingy
  - it serves so as to generate the value automatically (since it is a primary key)
- [ ] understand the DB back-end, specially the thing about SQLite
- [ ] How the "session" works, read SQLAlchemy documentation
- [ ] Creating and dropping DBs

## 1. OOP and Python

- [x] `__repr__` method in python, class attributes and f formatting
  - Used to represent a class's objects as strings &rarr; official string for printing and debugging
  - The call returns a string as the representation of the object
  - That is why when you modify the `__repr__` method you change the way it is printed out __when called through the repr() function__
  - To change the call for `print`, you use the `__str__` thing. HOWEVER, if you have not defined the `__str__` then the print call defaults to the repr

  ```python
  >>> import datetime
  >>> now = datetime.datetime.now()
  >>> now.__str__()
  '2020-12-27 22:28:00.324317'
  >>> now.__repr__()
  'datetime.datetime(2020, 12, 27, 22, 28, 0, 324317)'
  ```

  - As you can see, from the repr call, I would be able to reconstruct the datetime

- [x] Understand the package thing in Python (crucial to deployment)
  - `__init__` = Package
  - `__init__` es como el root del nombre del modulo (flaskblog). cualquier otro modulo es una ruta bajo el init -> flaskblog.modulo

- [ ] understand the line in cmd `from flaskblog import db`

- [x] __Understand EXACTLY what happens when importing modules in python. I mean literally the from etc importc this, what happens as an engine__
  - regular package: A traditional package, such as a directory containing an `__init__.py` file.
  - Import works like this
    - When a regular package is imported, this `__init__.py` file is implicitly executed, and the objects it defines are bound to names in the package’s namespace.
    - When I import a module or package from python, all class and functions declarations __are executed__. Example:

    ```python
    class Class1():
      print('I am class 1. I am being imported.')
    class Class2():
      print('I am class 2. I am not being imported but I am declared anyways :)')
    ```

    - `super().supperClassMethod` allows me to call the superclasses' methods, in this case, `superClassMethod`. For example, I can call the `__init__` of the supper class.
      - When inheriting, it is likely and common that the __subclass__ does not have an init method and, therefore, inherits whatever the superclass initializes.

- [x] __Entender cada linea del run.py__

- [ ] static methods

## Misc

[] hashing and keying, private and public review, how does the password_hash work

## VS Code

[] Shift Enter manda a python, no python debugger, en VS Code. Averiguar qué es esto

# Notes

[Every different piece of code and GitHub](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog)

[Code snippet for HTML etc.](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets)

- You need to declare the Env variable beforehand (set FLASK_APP=name)
- Everytime I refresh the browser I get a GET request from the browser which ends in 200
- Changes in FLASK_APP file do not reflect when the browser is changed (maybe with browser sync it does??)
  - There are plugins/packages to do this actually
  - Best practice: run in debug mode by setting the environment variable (set FLASK_DEBUG=1)
- Run through Python (python ex.py):
  - use the if __name___ construct
  - don't forget to set the debug to True
- Cool trick for *secret keys*: `import secrets; secrets.token_hex`
- `url_for` is passed the value of the function (substites the "url for" the function in python [i.e., retrieves the decorating route])
- `href = "#"` goes nowhere (dummy test, placeholder)
- ORM: Object Relational Mapper (for databases)
- SQLAlchemy allows to point to different DBs easily and not change the handling in Python
- URL parameters es con question mark. RECORDAR ESA WEAAAAAAAA (tiene que ver con el curso de front end, refrescar)
- Python static methods (Corey tiene un tutotiral de OOP)

## Passing variables

- Jinja is the thing that Flask uses to pass variables between HTML and flask
  - It's like its own programming language and syntax (probably based on javascript?)
- It's like I __escape__ the context of html and can use other sort of programming things (I guess that's why you use the {} signs)

## Decorators

- [Decorator explanation](https://realpython.com/primer-on-python-decorators/)
- In the end, when I put a @ sign __above__ a function I am WRAPPING IT inside the decorator (@decorator).
  - It is equivalent to calling the function inside the wrapper, i.e., `function = decorator(function)`.
  - This wraps the execution of function in the decorator

# Questions

- Autocomplete de Jinja en VSCode? Encontré [este thread](https://stackoverflow.com/questions/60175608/visual-studio-code-and-jinja-templates/65514961)

- [x] Usai single o doble quotes (estandarizar)?
  - single quotes

- [x] Menos sensibilidad del editor de VSCode está en file preference settings textedito
- [x] forms.py linea 25
  - Lo hace el validate_on_submit, que busca metodos que partan con el string validate para ejecutarlos upon validate_on_submit

- [x] Models línea 10 (necesito entender bien esto de los decorators)
  - Son como h(g(f))
  - Probablemente heredan todas las variables del scope en el que están llamados. MENTIRA (?): le paso a la función render_templates las variables que quiero que pueda insertar ocn Jinja

- [x] Quién está respondiendo? O sea, el terminal me está mostrando los requessts que hace el cliente, correcto?
  - Siempre se arma una relación Client - Server y siempre alguien asume ese rol

## EB

- EB init -> es como github
  - Te crea un repositorio
  - Deployea los cambios commiteados (o sea, mínimo en tu working tree local) (no necesariamente tiene que estar pusheado en el remoto)
  