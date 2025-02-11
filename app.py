import google.generativeai as genai
import os
from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set your API key
genai.configure(api_key="AIzaSyDj0vdXb2qKDzxzGD7l5G0AcITn_ZsAkZI")  # Replace with your actual key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/diet')
def diet():
    return render_template('diet.html')

@app.route('/fitness')
def fitness():
    return render_template('fitness.html')

@app.route('/hydration')
def hydration():
    return render_template('hydration.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')

@app.route('/form1')
def form1():
    return render_template('form1.html')

@app.route('/form2')
def form2():
    return render_template('form2.html')

@app.route('/form3')
def form3():
    return render_template('form3.html')

@app.route('/form4')
def form4():
    return render_template('form4.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)
        reply = response.text
    except Exception as e:
        reply = f"Error: {str(e)}"
    
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
