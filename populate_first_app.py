import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_web_site.settings')
import django
django.setup()


# fake stuff
import random
from first_app.models import *
from faker import Faker
fakegen = Faker()
topics = ['search','social','marketplace','news','games']
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get topic
        top = add_topic()

        #make fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #make webpage
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #make access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)

        fake_first = fakegen.name().split()[0]
        fake_last = fakegen.name().split()[1]
        fake_mail = fakegen.email()

        user = User.objects.get_or_create(First_name=fake_first,Last_name=fake_last,Email=fake_mail)


if __name__ == '__main__':
    print('populating')
    populate(20)
    print('populated')