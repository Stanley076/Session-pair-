import os
import random
import string
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def generate_session_id():
    # Static prefix parts
    prefix = "STANY"
    codes = ["TXR", "ZMD", "QKR", "PLM", "VBN"]
    suffixes = ["BTC", "ETH", "XRP", "LTC", "BNB"]
    
    # Generate random components
    part1 = random.choice(codes)
    part2 = random.choice(codes)
    random_str1 = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    random_str2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    
    return f"{prefix}-{part1}-{part2}~{random_str1}#{random.choice(suffixes)}{random_str2}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)
    
    session_id = generate_session_id()
    filename = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
    file.save(filename)
    
    return render_template('result.html', session_id=session_id)

if __name__ == '__main__':
    app.run(debug=True)
