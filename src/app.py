from flask import Flask, render_template, request
import random
import re

app = Flask(__name__)

def generate_code(supplier_name):
    # Remove any non-letter characters from the supplier name
    cleaned_name = re.sub(r'[^A-Za-z]', '', supplier_name)
    
    # Extract the first letter of each word in the cleaned supplier name
    initials = ''.join([word[0] for word in cleaned_name.split()])
    
    # Ensure the initials are at least 5 characters long
    while len(initials) < 5:
        initials += random.choice(cleaned_name)
    
    # Create the code with "SU" prefix and the first 5 characters of initials
    code = "SU" + initials[:5]
    return code.upper()

@app.route('/', methods=['GET', 'POST'])
def index():
    code = ""
    if request.method == 'POST':
        supplier_name = request.form['supplier_name']
        code = generate_code(supplier_name)
    return render_template('index.html', code=code)

if __name__ == '__main__':
    app.run(debug=True)