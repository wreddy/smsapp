from flask import Flask, request
from twilio import twiml

app = Flask(__name__)

@app.route('/sms', methods = ['POST'])

def sms():
    number= request.form['FROM']
    message_body = request.form['BODY']

    resp = twiml.Response()
    resp.message('Hey phone num{}, you said: {}'.format(number, message_body))
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
