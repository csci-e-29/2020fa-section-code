# Create your views here.
from django.shortcuts import render

"""
You can see how the urls are calling the views, but here you see ways to redirect to other parts of your website. You can also redirect to other websites, etc. 
This CONTROLS what the users "view", not WHAT they view 
"""


def index(request):
    return render(request, 'webpage/index.html')
