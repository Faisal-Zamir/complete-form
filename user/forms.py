from django import forms
from . models import user_rec

class userform(forms.ModelForm):
    
    userName= forms.CharField(max_length=20,min_length=5,widget= forms.TextInput
                           (attrs={'class':'form-control','placeholder':'Enter your first name'}))
    
    email= forms.CharField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    pwd = forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'placeholder':'Enter your Password'}))
    class Meta:
        model = user_rec
        fields = ['userName','email', 'pwd', 'website','image','term','gender','subjects','upload_cv','phon',]
        
       
        help_texts = {
            'email': 'Write Your Email here',
        }

        labels = {'image':'Upload your image','pwd':'Enter Password', 'email': 'Enter Email'}
        error_messages = {
            'userName':{'required':'Naam Likhna Jaruri Hai','max_lenght':'Your name is too long,please give readable name'},
            'pwd':{'required':'You have enter password'},
            'email':{'required':'You have enter Email'}
            }
        
        widgets = {
                'pwd':forms.PasswordInput(),
              
                }