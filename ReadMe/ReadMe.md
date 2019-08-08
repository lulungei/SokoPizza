#Setup Project

##Clone Soko Pizza on your PC
`git-clone...`

##Create a postgres database with the following credentials
 name- *sokopizza*
 user - *postgres*
 password - *G33kslivehere*


##Make Database migrations
cd into the project root and run:
`py manage.py makemigrations pizza`
`py manage.py migrate`

##Create an admin superuser to login to the admin panel:
`py manage.py createsuperuser`
Username : **admin**
Email: **admin@mailer.com**
Password: **password**

Login to the admin panel and add the toppings and size data in the Pizzasize and Toppings models.
*Screenshot 433*

Run the project 
`py manage.py runserver 80`

##Make order
To make a pizza order, go to http://127.0.0.1/make_order

Enter an order in the format 
*Size - Toppings, Toppings, Toppings*
*Screenshot 434*

Click Order to make your order
*Screenshot 432*


