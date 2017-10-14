from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *
from .forms import UserForm
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    users = User.objects.order_by('First_name')
    date_dic = {'access_records': webpage_list, 'users': users}
    # my_dic = {'insert_me': [i for i in range(8)]}
    return render(request, 'first_app/index.html', context=date_dic)

def help(request):
    my_dic = {'insert_one': "help is on the way!",
              'insert_two': "help has arrived!"}
    return render(request,'first_app/help.html',context=my_dic)

def relative_url(request):
    return render(request,'first_app/relative_url_templates.html')

def user_form_view(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    else:
        return render(request, 'first_app/form_page.html', {'form': form})