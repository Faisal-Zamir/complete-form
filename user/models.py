from django.db import models

class user_rec(models.Model):

    userName = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    pwd = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_img')
    term = models.BooleanField(null=True, blank=True)

    CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    gender = models.CharField(max_length=100, choices=CHOICES)
    date_joining = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    Subj_choice = [
        ('chem', 'Chemistry'),
        ('phy', 'Physics'),
        ('bio', 'Biology'),
    ]

    subjects = models.CharField(max_length=100, choices=Subj_choice)
    upload_cv = models.FileField(upload_to='doc\\', null=True, blank= True)
    phon = models.IntegerField(null=True, blank=True)
