<h3>Boomerang</h3>

1. First you need to make a git clone of our project
> git clone git@github.com:tturdumamatovv/boomerang.git


2. Here we create a virtual environment (for linux), also you activate it
> python3 -m venv venv
>
> source venv venv/bin/activate


3. Next, download all the libraries
> pip install -r requirements.txt


4. Here we create a .env file (for linux), and copy paste data from env_example
> touch .env


5. Here we can start our docker to run project
> docker compose up -d --build


6. Here we can check our endpoints: 
    1. Here you can see which endpoints are available and which fields are needed, and to make requests and create, I advise you to use Postman, since we will need to use tokens further: 
    http://localhost:8000/swagger/

    2. Here we can create a new user (post request):
    http://localhost:8000/api/v1/register/

    3. Here we can login and get tokens (post request): 
    http://localhost:8000/api/v1/login/

    4. Here we can create product, we need access_token to do (post request): 
    http://127.0.0.1:8000/api/v2/products/

    5. Here we can get all products, we need access_token to do (get request): 
    http://127.0.0.1:8000/api/v2/products/

    6. Here we can retrieve one product with id, we need access_token to do (get request):
    http://127.0.0.1:8000/api/v2/products/{id}/

    7. Here we can update product with id, only the owner can update their product, we need access_token to do (put request or patch request):
    http://127.0.0.1:8000/api/v2/products/{id}/

    8. Here we can update product with id, only the owner can delete their product, we need access_token to do (delete request):
    http://127.0.0.1:8000/api/v2/products/{id}/

    9. Here you can add products to the cart and choose the quantity as you wish, if you have not selected the quantity, then 1 is automatically selected, we need access_token to do (post request): 
    http://127.0.0.1:8000/api/v2/cart/

    10. Here you can see what is in your cart using the token as well, and other users cannot view what is in your cart (post request): 
    http://127.0.0.1:8000/api/v2/cart/list/

    11. Here you can place an order, when ordering, if the order is successful, all the goods are removed from the basket, since you have already ordered them, also if your basket is empty, then the order will not pass (post request): 
    http://127.0.0.1:8000/api/v2/order/create/

    12. Here we can view our orders and we will also need a token (get request): 
    http://127.0.0.1:8000/api/v2/orders/

7. You can use this code to run tests:
> python manage.py test


<h3>If you didn't understand something, you can write to me in a telegram(https://t.me/muhxaa ) or in whatsapp(+996705560060)</h3>
