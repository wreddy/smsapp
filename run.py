from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hi_app():
    resp = twilio.twiml.Response()
    resp.message("Hello from W again")    
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
    
