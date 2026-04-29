class GmailClientPlaceholder:
    def __init__(self, integration=None):
        self.integration = integration

    def send_email(self, recipient_email, subject, body, attachments=None):
        return {
            "sent": False,
            "message": "Gmail OAuth belum diimplementasikan. Ini placeholder interface.",
            "recipient_email": recipient_email,
            "subject": subject,
            "attachments": attachments or [],
        }
