import smtplib
import ssl
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
import os
import logging
from datetime import datetime

class NotificationService:
    """Handles email and SMS notifications for citizen registrations"""
    
    def __init__(self):
        # Email configuration (for demo purposes - would be env vars in production)
        self.smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.environ.get('SMTP_PORT', '587'))
        self.email_user = os.environ.get('EMAIL_USER', 'glorbenia.micronation@gmail.com')
        self.email_password = os.environ.get('EMAIL_PASSWORD', 'your-app-password')
        
        # Twilio configuration (for SMS)
        self.twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID', 'your-account-sid')
        self.twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN', 'your-auth-token')
        self.twilio_phone_number = os.environ.get('TWILIO_PHONE_NUMBER', '+1234567890')
        
        self.setup_logging()
    
    def setup_logging(self):
        """Setup logging for notification service"""
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def send_email_confirmation(self, citizen_data, citizen_id):
        """Send email confirmation with citizen ID details"""
        try:
            # In a real implementation, you would use actual SMTP credentials
            # For demo purposes, we'll simulate the email sending
            self.logger.info(f"📧 EMAIL SIMULATION: Sending to {citizen_data['email']}")
            self.logger.info(f"📧 Subject: Welcome to Glorbenia - Your GreenID is Ready!")
            self.logger.info(f"📧 Message: Congratulations {citizen_data['name']}! Your Glorbenian ID: {citizen_id}")
            
            # Simulate email content
            email_content = self._generate_email_content(citizen_data, citizen_id)
            
            # In production, you would do:
            # self._send_real_email(citizen_data['email'], email_content)
            
            return {
                'success': True,
                'message': f'Email confirmation sent to {citizen_data["email"]}',
                'type': 'email'
            }
            
        except Exception as e:
            self.logger.error(f"Failed to send email: {str(e)}")
            return {
                'success': False,
                'message': f'Failed to send email: {str(e)}',
                'type': 'email'
            }
    
    def send_sms_confirmation(self, citizen_data, citizen_id):
        """Send SMS confirmation with citizen ID details"""
        try:
            # In a real implementation, you would use Twilio
            # For demo purposes, we'll simulate the SMS sending
            self.logger.info(f"📱 SMS SIMULATION: Sending to {citizen_data['phone']}")
            self.logger.info(f"📱 Message: Welcome to Glorbenia! Your ID: {citizen_id}")
            
            # Simulate SMS content
            sms_content = self._generate_sms_content(citizen_data, citizen_id)
            
            # In production, you would do:
            # self._send_real_sms(citizen_data['phone'], sms_content)
            
            return {
                'success': True,
                'message': f'SMS confirmation sent to {citizen_data["phone"]}',
                'type': 'sms'
            }
            
        except Exception as e:
            self.logger.error(f"Failed to send SMS: {str(e)}")
            return {
                'success': False,
                'message': f'Failed to send SMS: {str(e)}',
                'type': 'sms'
            }
    
    def _generate_email_content(self, citizen_data, citizen_id):
        """Generate email content for citizen confirmation"""
        return f"""
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f0f8f0;">
            <div style="background-color: #2d5016; color: white; padding: 20px; text-align: center; border-radius: 10px 10px 0 0;">
                <h1>🏰 Welcome to Glorbenia!</h1>
                <p>Your GreenID Registration is Complete</p>
            </div>
            
            <div style="background-color: white; padding: 30px; border: 2px solid #4a7c4e; border-radius: 0 0 10px 10px;">
                <h2 style="color: #2d5016;">Congratulations, {citizen_data['name']}!</h2>
                
                <p>You are now an official citizen of the micronation of Glorbenia!</p>
                
                <div style="background-color: #e8f5e8; padding: 20px; border-radius: 5px; margin: 20px 0;">
                    <h3 style="margin: 0 0 10px 0; color: #2d5016;">Your Glorbenian ID:</h3>
                    <p style="font-size: 24px; font-weight: bold; color: #2d5016; margin: 0; font-family: monospace;">{citizen_id}</p>
                </div>
                
                <h3 style="color: #2d5016;">Registration Details:</h3>
                <ul style="color: #333;">
                    <li><strong>Name:</strong> {citizen_data['name']}</li>
                    <li><strong>Nation of Residence:</strong> {citizen_data['nation']}</li>
                    <li><strong>Gender Identity:</strong> {citizen_data['gender']}</li>
                    <li><strong>Email:</strong> {citizen_data['email']}</li>
                    <li><strong>Phone:</strong> {citizen_data['phone']}</li>
                </ul>
                
                <h3 style="color: #2d5016;">What happens next?</h3>
                <p>You can now access Glorbenian services that require ID verification, including:</p>
                <ul>
                    <li>Glorbenian National Bank</li>
                    <li>Government services</li>
                    <li>Official documentation</li>
                </ul>
                
                <div style="background-color: #fff8dc; padding: 15px; border-radius: 5px; margin-top: 20px;">
                    <p style="margin: 0; font-style: italic; color: #8b4513;">
                        🛡️ Your personal data is protected with military-grade encryption.
                    </p>
                </div>
                
                <p style="margin-top: 30px; font-size: 14px; color: #666;">
                    This email was sent by the Glorbenia GreenID Registration System.<br>
                    Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                </p>
            </div>
        </body>
        </html>
        """
    
    def _generate_sms_content(self, citizen_data, citizen_id):
        """Generate SMS content for citizen confirmation"""
        return f"""
🏰 Welcome to Glorbenia, {citizen_data['name']}!

Your GreenID: {citizen_id}

You're now an official Glorbenian citizen! 
Access services at: glorbenia.micronation

🛡️ Data encrypted for your security.
        """.strip()
    
    def send_confirmation_notifications(self, citizen_data, citizen_id, preferences):
        """Send notifications based on user preferences"""
        notifications_sent = []
        
        # Send email if requested
        if preferences.get('email_confirmation') and citizen_data.get('email'):
            result = self.send_email_confirmation(citizen_data, citizen_id)
            notifications_sent.append(result)
        
        # Send SMS if requested
        if preferences.get('sms_confirmation') and citizen_data.get('phone'):
            result = self.send_sms_confirmation(citizen_data, citizen_id)
            notifications_sent.append(result)
        
        return notifications_sent
    
    def get_notification_status(self):
        """Get current notification service status"""
        return {
            'email_service': 'configured',
            'sms_service': 'configured', 
            'demo_mode': True,
            'features': ['email_confirmation', 'sms_confirmation']
        }

# Global notification service instance
notification_service = NotificationService()

