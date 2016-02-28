from flask import Flask, request
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def index():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    with resp.gather(action="/handle-input", method="POST", numDigits=3) as g:
        g.say("Please enter a number to start playing")
    return str(resp)

@app.route("/handle-input", methods=['GET', 'POST'])
def handle_input():
    input_num = request.values.get('Digits', None)
    resp = twilio.twiml.Response()
    resp.say("You entered " + input_num)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)