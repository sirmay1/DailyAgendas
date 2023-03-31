Admin login & user name:

username: Admin
password: 123

description on files

NOTE: for the file newaccount.html, please make sure to place under the method section the same file name as where it is originating from.
EXAMPLE: 
<form method="POST" action="{% url 'newaccount.html' %}" class="form">
csrf_token = cross site request forgery token.
</form>

-----------------------------------------------------------------------------------------------------
NOTE: look into custom models, models.py file:
Note: You can also create users programmatically, as shown below. You would have to do this, for example, if developing an interface to allow "ordinary" users to create their own logins (you shouldn't give most users access to the admin site).

from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'Tyrone'
user.last_name = 'Citizen'
user.save()
Copy to Clipboard
It is highly recommended to set up a custom user model when starting an actual project. You'll be able to easily customize it in the future if the need arises. For more information, see Using a custom user model when starting a project (Django docs).
