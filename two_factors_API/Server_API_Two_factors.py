from flask import Flask, request, jsonify
import random
from flask_mail import Mail, Message
import time

app = Flask(__name__)

# Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'daniucs.teste1@gmail.com'
app.config['MAIL_PASSWORD'] = 'ciarkhyrkbqlwxyv'

mail = Mail(app)

# Dictionary to Store Verification Codes
verification_codes = {}

# Function to Generate the Verification Code
def generate_verification_code():
    return str(random.randint(1000, 9999))

# Endpoint to Generate and Send the Verification Code
@app.route('/generate-code', methods=['POST'])
def generate_code():
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    code = generate_verification_code()
    expires_at = time.time() + 300  # code expires in 5 minutes
    verification_codes[email] = {'code': code, 'expires_at': expires_at}


    # Sends the Email with the Verification Code
    try:
        send_email(email, code)
        return jsonify({'message': 'Verification code sent'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to send email'}), 500

def send_email(recipient, code):
    with app.app_context():
        msg = Message('Your Verification Code',
                      sender='daniucs.teste1@gmail.com',
                      recipients=[recipient])
        msg.body = f'Your verification code is DH-{code}'
        mail.send(msg)

# Endpoint to Verify the Verification Code
@app.route('/verify-code', methods=['POST'])
def verify_code():
    email = request.json.get('email')
    code = request.json.get('code')
    if not email or not code:
        return jsonify({'error': 'Email and code are required'}), 400

    if email in verification_codes:
        stored_code = verification_codes[email]['code']
        expires_at = verification_codes[email]['expires_at']
        if time.time() > expires_at:
            return jsonify({'error': 'Code has expired'}), 400
        if code == stored_code:
            return jsonify({'message': 'Verification successful'}), 200
        else:
            return jsonify({'error': 'Invalid code'}), 400
    else:
        return jsonify({'error': 'No code found for this email'}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)
