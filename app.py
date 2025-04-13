from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyC84HCcvR-7tU_Rvyiuks5x25k6uSk0vlA"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        # Create a prompt for the AI
        prompt = f"""Generate 3-5 questions and their answers about {user_message}. 
        Format the response as follows:
        Question 1: [question]
        Answer 1: [answer]
        
        Question 2: [question]
        Answer 2: [answer]
        
        And so on..."""
        
        # Get response from Gemini
        response = model.generate_content(prompt)
        
        return jsonify({
            'status': 'success',
            'response': response.text
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'response': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True) 