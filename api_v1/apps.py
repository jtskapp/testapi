from django.apps import AppConfig
from django.conf import settings
import sys, os

class ApiV1Config(AppConfig):
    name = 'api_v1'

    def ready(self):
        dataloaded = []
        if (os.environ.get("DYNO")):
            print('In Heroku Dyno')
        # you must import your modules here 
        # to avoid AppRegistryNotReady exception
        if settings.LOAD_DATA:
            print('LOAD DATA Flag is TRUE')
            from .models import Customer
            from . import dataloader
            # startup code here
            dataloaded = dataloader.loaddata()
            if dataloaded:
                print('Total Data Retrieved = {}'.format(len(dataloaded)))
                if len(dataloaded) > 0:
                    print('Loading data ...')
                    for customer in dataloaded:
                        cus_gender = customer['gender']
                        cus_title = customer['title']
                        cus_firstname = customer['first_name'].decode('utf-8')
                        cus_lastname = customer['last_name'].decode('utf-8')
                        cus_dispname = customer['display_name']
                        cus_email = customer['email_address'].decode('utf-8')
                        cus_street = customer['street'].decode('utf-8')
                        cus_city = customer['city'].decode('utf-8')
                        cus_state = customer['state'].decode('utf-8')
                        cus_postcode = customer['postal_code']
                        cus_age = customer['age']
                        cus_phone = customer['phone'].decode('utf-8')
                        cus_cell = customer['cell'].decode('utf-8')
                        cus_image = customer['image'].decode('utf-8')
                        customer = Customer.objects.filter(display_name__iexact=cus_dispname,
                            email_address__iexact=cus_email)
                        if customer.count() > 0:
                            print('Customer {} data found'.format(cus_dispname))
                        else:
                            print('Customer {} data not found'.format(cus_dispname))
                            cust = Customer(gender=cus_gender,
                                title = cus_title,
                                first_name = cus_firstname,
                                last_name = cus_lastname,
                                display_name = cus_dispname,
                                email_address = cus_email,
                                street = cus_street,
                                city = cus_city,
                                state = cus_state,
                                postal_code = cus_postcode,
                                age = cus_age,
                                phone = cus_phone,
                                cell = cus_cell,
                                image = cus_image)
                            cust.save()
                else:
                    print('No data set to be loaded')
            else:
                print('Failed to retrieve data from api endpoint')
        else:
            print('LOAD DATA Flag is FALSE')
        if 'runserver' not in sys.argv:
            print('Total Data Retrieved = {}'.format(len(dataloaded)))
            return True