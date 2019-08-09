# SokoPizza
A django pizza ordering system

## Steps to run SokoPizza on your PC:
1. `https://github.com/omingei/SokoPizza.git`
2. Turn on virtual env `myenv\Scripts\activate`
3. cd SokoPizza
4. Make migrations `py manage.py makemigrations`
5. Migrate `py manage.py migrate`
6. Run server `py manage.py runserver 80`

## Make orders
To make an order head to http://127.0.0.1/make_order
Enter the order in the format : *Size - Toppings, Toppings, Toppings*
Click on 'Order' to view your receipt.

## Add sizes and toppings using django rest framework:
POST `http://127.0.0.1/api/v1/toppings/`
`
{
    "id": 1,
    "name": "Cheese",
    "small_price": "50.00",
    "medium_price": "75.00",
    "large_price": "100.00",
    "type": "Basic"

}
`

POST `http://127.0.0.1/api/v1/size/`

`
{
  "id": 1,
  "size": "Small",
  "price": "1200.00"  
}
`
## PS:
The api's url is defined in the urls.py global file. I chose to use different a view file for the rest framework view **api_views.py** to maintain a level of structure in my code.
## Add sizes and toppings using django admin panel:
Read the ReadMe file in the ReadMe folder.
