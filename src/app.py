from flask import Flask, render_template # importing the flask class
app = Flask(__name__) # creating an instance of the Flask class
 
data = {
    "cat": [
            {
            "name": "Snow", 
            "description": "This is a white cat",
            },
            {
            "name": "Fluffy", 
            "description": "This is a cat with a glorious fur",
            },
            {
            "name": "Blacky", 
            "description": "This is a black cat",
            }
    ]
}

@app.route('/') # The primary url for our application
def hello_world(): # This method returns 'Flask Dockerized', which is displayed in our browser.
    return render_template('index.html')
    #return 'Hello! I am dockerized Flask web framework'

@app.route('/cats')
def get_cats():
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # This statement starts the server on your local machine.