from flask import render_template, request, Blueprint
from flaskblog.models import Post


# pretty much like calling the flask object in the app object
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home") # Handling multiple route, same function
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    # Note that render template looks in template folder by
    # default
    # Passing the post variable as a post argument to render
    # template
@main.route("/about", methods=["GET", "POST"])
def about():
    # print(request.json)
    # print(request.json.get("fullname"))
    # print(request.json.get("fullnam2e"))
    # return jsonify({"apellido": "diaz"}), 200
    return render_template("about.html")









################################################
@main.route('/debugger')
def debug():
    return render_template('debugger.html')