from flask import Flask, request, jsonify, send_file
import json
import os
from id import generate_glorbenian_id

app = Flask(__name__)

# Store registered citizens (in a real application, you'd use a database)
citizens_db = []

@app.route('/')
def index():
    """Serve the main registration page"""
    return send_file('index.html')

@app.route('/generate_id', methods=['POST'])
def generate_id():
    """Generate a new Glorbenian ID for a citizen"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('nation') or not data.get('name') or not data.get('gender'):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Ensure nation is not Glorbenia
        if data['nation'] == 'Glorbenia':
            return jsonify({'error': 'Nation of residence cannot be Glorbenia'}), 400
        
        # Generate the ID using the existing function
        citizen_id = generate_glorbenian_id()
        
        # Create citizen record
        citizen_record = {
            'id': citizen_id,
            'name': data['name'].strip(),
            'nation': data['nation'],
            'gender': data['gender'],
            'registration_timestamp': '2024-12-19'  # You could use datetime for real timestamp
        }
        
        # Store in our "database"
        citizens_db.append(citizen_record)
        
        # Return success response
        return jsonify({
            'success': True,
            'id': citizen_id,
            'name': citizen_record['name'],
            'nation': citizen_record['nation'],
            'gender': citizen_record['gender'],
            'message': f'Welcome to Glorbenia, {citizen_record["name"]}!'
        })
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/citizens', methods=['GET'])
def get_citizens():
    """Get list of all registered citizens (for admin purposes)"""
    return jsonify({
        'total_citizens': len(citizens_db),
        'citizens': citizens_db
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Glorbenia GreenID Registration System',
        'version': '1.0'
    })

if __name__ == '__main__':
    print("🏰 Welcome to the Glorbenia GreenID Registration System!")

    print("🌐 Starting web server...")
    print("📝 Make sure you have Flask installed: pip install flask")
    print("🌍 Access the registration form at: http://localhost:8080")
    print("📊 View all citizens at: http://localhost:8080/citizens")
    print("❤️  Health check at: http://localhost:8080/health")
    print("\n" + "="*50)
    

    app.run(debug=True, host='0.0.0.0', port=8080)
