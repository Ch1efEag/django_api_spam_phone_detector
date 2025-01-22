# import os
# import django
# import random
# import string
# from datetime import datetime, timedelta

# # Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spam_detector.settings')  # Replace 'spam_detector' with your project name

# # Initialize Django
# django.setup()

# # Now import your models
# from api.models import User, Spam, Contacts

# # Initialize a starting phone number
# starting_phone_number = 1000000780  # Example: Start from this phone number

# # Function to generate random names
# def generate_random_name():
#     return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))

# # Function to generate random timestamp within the last 30 days
# def generate_random_timestamp():
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=30)
#     return start_date + (end_date - start_date) * random.random()

# # Create random users and related data
# def populate_data(num_users=10):
#     global starting_phone_number  # Access the global variable to maintain the counter
    
#     for _ in range(num_users):
#         # Create a User
#         name = generate_random_name()
#         phone_number = str(starting_phone_number)  # Use the current phone number
#         email = f"{name.lower()}@example.com"
#         password = "password123"  # For simplicity, you can keep a default password
#         user = User.objects.create_user(name=name, phone_number=phone_number, password=password, email=email)
        
#         # Increment the phone number for the next user
#         starting_phone_number += 1
        
#         # Create Contacts (1 contact per user)
#         contact_name = generate_random_name()
#         contact_number = str(starting_phone_number)  # Unique contact number based on the counter
#         Contacts.objects.create(user=user, name=contact_name, number=contact_number)
        
#         # Increment the phone number for the next contact
#         starting_phone_number += 1
        
#         # Create Spam report for a random phone number (some may be marked as spam)
#         if random.random() > 0.5:  # 50% chance to report this number as spam
#             spam_timestamp = generate_random_timestamp()
#             Spam.objects.create(number=phone_number, count=1, reported_by=user, timestamp=spam_timestamp)

#         print(f"User {name} with phone number {phone_number} created successfully!")

# # Call the populate_data function
# populate_data(num_users=10)  # You can change this number as needed
