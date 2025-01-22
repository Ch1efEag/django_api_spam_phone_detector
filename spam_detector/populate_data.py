import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spam_detector.settings')  # Replace 'spam_detector' with your project name

# Initialize Django
django.setup()

# Now import your models
from api.models import User, Spam, Contacts

# Now you can use the models, for example:
# Populating data
user = User.objects.create_user(name="John Doe", phone_number="1234567890", password="password123", email="john@example.com")
spam = Spam.objects.create(number="1234567890", count=1)
contact = Contacts.objects.create(user=user, name="Jane Doe", number="0987654321")

print("Data populated successfully!")
