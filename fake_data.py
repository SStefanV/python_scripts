# -*- coding: utf-8 -*-
"""
Script for generating fake data very easily
A lot more info on the web site   https://faker.readthedocs.io/en/latest/providers.html
First: 'pip install Faker'
If you are using Anaconda distribution use: 'conda install -c conda-forge faker'

"""
from faker import Faker
fake = Faker('en_US')   #de_DE for Germany, es_ES for spanish, fr_FR France......lot more on the docs
                                                  


for i in range(60):
    street = fake.street_address() ;    
    # full_address = fake.address() ;                                     
    city = fake.city();                                  company = fake.company() ;
    # country = fake.country();                          #zip_code = fake.zipcode();
    # postal_code = fake.postalcode();                   #credit_card_exp = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y");
    rand_int = fake.random_int(min=1, max=3, step=1);    #credit_card_no =fake.credit_card_number(card_type=None);
    # state = fake.state();                              #credit_card_sec_code =fake.credit_card_security_code(card_type=None);
    email = fake.ascii_email();                          l_name = fake.last_name()
    # job = fake.job();                                  #female_l_name = fake.last_name_female()
    f_name = fake.first_name();                          #male_l_name = fake.last_name_male() 
    # female_f_name = fake.first_name_female();          #name = fake.name()
    # male_f_name =fake.first_name_male();               #female_name = fake.name_female()
    # male_name = fake.name_male()
    # phone = fake.phone_number()
    # color = fake.color_name()
    
    print(f"({rand_int},'{f_name}', '{l_name}', '{email}', '{company}', '{street}', '{city}',NULL),")     
           
