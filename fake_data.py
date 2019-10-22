# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
from faker import Faker
fake = Faker()
for i in range(20):
    print(f'(\'{fake.first_name()}\',\'{fake.last_name()}\', \'{fake.ascii_email()}\',\'{fake.company()}\', \'{fake.street_address()}\',\'{fake.city()}\', NULL),')
           
           