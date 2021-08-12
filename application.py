from flaskblog import create_app

application = create_app()
# To run through python the thing below
if __name__ == "__main__":
    application.run(debug=True)