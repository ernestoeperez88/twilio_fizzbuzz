from flask import Flask, request, render_template
import twilio.twiml
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dialing", methods=['POST'])
def dial():
    phone_num = "+1" + request.form['pNumber']
    phonebuzz_num = "+17606711394"

    # Credentials
    account_sid = "ACd0a9af9570cb3204b46a1c874003c045"
    auth_token = "61cc15906b94828995d98e608bbfb3a9"
    client = TwilioRestClient(account_sid, auth_token)
 
    # Making call
    call = client.calls.create(to=phone_num,  # Any phone number
                           from_=phonebuzz_num, # Must be a valid Twilio number
                           url="http://twiliofizzbuzz-ernestoeperez.rhcloud.com/play-phonebuzz")
    print call.sid

@app.route("/play-phonebuzz", methods=['GET', 'POST'])
def play_phoneBuzz():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    with resp.gather(action="/handle-input", method="POST", numDigits=2) as g:
        g.say("Please enter a two digit number to start playing")
    return str(resp)

@app.route("/handle-input", methods=['GET', 'POST'])
def handle_input():
    input_num = int(request.values.get('Digits', None))
    message = ''

    # FizzBuzz 
    for num in range(1, input_num + 1):
        next = ''
        if num % 3 == 0:
            next += 'Fizz'
        if num % 5 == 0:
            next += 'Buzz'
        if not next:
            next = str(num)
        message += next + ' '

    resp = twilio.twiml.Response()
    resp.say(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)