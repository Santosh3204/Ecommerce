from django.db import models

# Create your models here.
"""
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)
"""

class UserRegister(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField() 
    user_dob = models.CharField(max_length=10)
    user_gender = models.CharField(max_length=10)
    user_phonenumber = models.IntegerField()
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50)
    user_password = models.CharField(max_length=100)
    user_address = models.TextField(default=None)
    def __str__(self):
        return self.user_name



"""
class UserProfile(models.Model):  
    user = models.ForeignKey(User, unique=True)
    location = models.CharField(max_length=140)  
    gender = models.CharField(max_length=140)  
    employer = models.ForeignKey(Employer)
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username
        """

class AddToCart(models.Model):
    cart_useremail = models.EmailField(default=None)
    cart_name = models.CharField(max_length=1024)
    cart_image = models.ImageField(upload_to = 'cartimages/')
    cart_price = models.PositiveIntegerField()
    cart_publisher = models.CharField(max_length=1024)
    cart_origin = models.CharField(max_length=1024)
    cart_description = models.TextField()
    cart_slug = models.SlugField()
    cart_quantity = models.PositiveIntegerField(default=0)
    cart_total_price = models.PositiveIntegerField(default=0)