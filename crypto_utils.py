
from cryptography.fernet import Fernet
import base64
import hashlib
import os
import json

class CitizenDataCrypto:
    """Handles encryption/decryption of citizen registration data"""
    
    def __init__(self, secret_key=None):
        if secret_key is None:
            # Use environment variable or generate a fixed key for demo
            secret_key = os.environ.get('GLORBENIA_SECRET_KEY', 'glorbenia-micronation-2024')
        
        # Create a consistent key from the secret
        key = hashlib.sha256(secret_key.encode()).digest()
        self.fernet = Fernet(base64.urlsafe_b64encode(key))
    
    def encrypt_data(self, data_dict):
        """Encrypt citizen data and return encrypted string"""
        # Convert dict to JSON string
        json_data = json.dumps(data_dict)
        # Encrypt the JSON data
        encrypted_data = self.fernet.encrypt(json_data.encode())
        # Return base64 encoded string
        return base64.urlsafe_b64encode(encrypted_data).decode()
    
    def decrypt_data(self, encrypted_string):
        """Decrypt citizen data and return dict"""
        try:
            # Decode from base64
            encrypted_data = base64.urlsafe_b64decode(encrypted_string.encode())
            # Decrypt
            json_data = self.fernet.decrypt(encrypted_data)
            # Convert back to dict
            return json.loads(json_data.decode())
        except Exception as e:
            raise ValueError(f"Failed to decrypt data: {str(e)}")
    
    def encrypt_id_and_name(self, citizen_id, name):
        """Convenience method to encrypt just ID and name"""
        return self.encrypt_data({
            'id': citizen_id,
            'name': name,
            'encrypted': True
        })
    
    def decrypt_id_and_name(self, encrypted_data):
        """Convenience method to decrypt ID and name"""
        return self.decrypt_data(encrypted_data)

# Global crypto instance
crypto = CitizenDataCrypto()

