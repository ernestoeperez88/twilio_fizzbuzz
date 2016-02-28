from flask import Flask, request
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def index():
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