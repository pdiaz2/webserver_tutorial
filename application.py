from flaskblog import create_app

app = create_app()
# To run through python the thing below
if __name__ == "__main__":
    app.run(debug=True)