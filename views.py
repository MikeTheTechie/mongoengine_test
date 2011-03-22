# use debug settings 
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
#import pdb

from django import template
from django.template.loader import get_template
from django.template import  Context
from django.http import  HttpResponse

from mongoengine import  *
from mongoengine_test.models import *

def mongoengine_test_view(request):
    # t = datetime.datetime.now()
    #mytemplate = template.Template('<html><body>My first name is {{ person.name }} and I am {{ person.age }}.<body></html>')
    #mytemplate = get_template('MyDataCaptureTemplate.html')
    
    person={'name':"test1",'age':22}

    # connect to our MOngoDB database...    
    connect('tumblelog')
    john = User(email='jdoe@example.com', first_name='John', last_name='Doe')
    john.save()


    post1 = TextPost(title='Fun with MongoEngine', author=john)
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()
    
    post2 = LinkPost(title='MongoEngine Documentation', author=john)
    post2.link_url = 'http://tractiondigital.com/labs/mongoengine/docs'
    post2.tags = ['mongoengine']
    post2.save()

    
    mycontext = template.Context({'person':person})
    #myoutput = mytemplate.render(mycontext)
    return render_to_response('BooksTemplate.html', mycontext)
    #return render_to_response('FancyTemplate.html', mycontext)
    ##return render_to_response('MyDataCaptureTemplate.html', mycontext)
    # return HttpResponse(myoutput)
    #return HttpResponse("Hello datacapture world {0}".format(t))
# Create your views here.


