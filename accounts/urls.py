from unicodedata import name
from django.urls import path ,include
# from .models import 
from .views import  signup
from posts import urls

from posts.views import blogHome 


app_name="accounts"

urlpatterns = [
     path('signup/',signup,name ='signup'),
     path('', blogHome.as_view() ,name='home')
     
 ]
