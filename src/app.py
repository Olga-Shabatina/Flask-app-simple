from flask import Flask, render_template # importing the flask class
app = Flask(__name__) # creating an instance of the Flask class
 
@app.route('/') # The primary url for our application
def hello_world(): # This method returns 'Flask Dockerized', which is displayed in our browser.
    return render_template('index.html')
    #return 'Hello! I am dockerized Flask web framework'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # This statement starts the server on your local machine.