import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
django.setup()

# import the Company model and any other necessary modules
from app.models import Company

# define the path to the text file
file_path = 'text.txt'

# read the file and insert data into the database
with open(file_path, 'r') as file:
    for line in file:
        # print(line)
        name, headquarters, followers, location = line.strip().split('|')
        company = Company(
            name=name,
            headquarters=headquarters,
            followers=followers,
            location=location
        )
        
        company.save()
#         # print(company)

# print("Data inserted successfully.")
# from app.models import Company

# Delete all records from the Company model
# Company.objects.all().delete()
