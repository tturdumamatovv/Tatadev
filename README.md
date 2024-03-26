<h3>Tatadev</h3>


1. Here we can check our endpoints: 
    1. Here you can see which endpoints are available and which fields are needed, and to make requests and create, I advise you to use Postman, since we will need to use tokens further: 
    https://cf-envision.com.kg/swagger/


    2. Here we can create a new user (post request):
    https://cf-envision.com.kg/api/v1/register/


    3. Here we can login and get tokens (post request): 
    https://cf-envision.com.kg/api/v1/login/


    4. Here we can create restaurants, we need access_token to do (post request): 
    https://cf-envision.com.kg/api/v1/restaurants/

    - Example 

    {
    "name": "Capito",
    "address": "Проспект Гагарина, 294",
    "description": "the best"
    }


    5. Here we can get all restaurants, we need access_token to do (get request): 
    https://cf-envision.com.kg/api/v1/restaurants/

    - Example

    {
    "name": "Capito",
    "address": "Проспект Гагарина, 294",
    "description": "the best",
    "latitude": "47.12763",
    "longitude": "58.2451"
    }

    * as you can see, latitude and longitude are created automatically because we use google maps


    6. Here we can retrieve one restaurants with id, we need access_token to do (get request):
    https://cf-envision.com.kg/api/v1/restaurants/{id}/

    7. Here we can update restaurants with id, only the owner can update their restaurants, we need access_token to do (put request or patch request):
    https://cf-envision.com.kg/api/v1/restaurants/{id}/

    8. Here we can update restaurants with id, only the owner can delete their restaurants, we need access_token to do (delete request):
    https://cf-envision.com.kg/api/v1/restaurants/{id}/

    9. Here you can get all reviews, we need access_token to do (get request): 
    https://cf-envision.com.kg/api/v1/reviews/

    10. Here you can create create new reiview for restaurant (post request): 
    https://cf-envision.com.kg/api/v1/reviews/

    11. Here you can update your review with id, only owner can do it (put or patch request): 
    https://cf-envision.com.kg/api/v1/reviews/{id}/

    12. Here you can delete your review, only owner can do it (delete request): 
    https://cf-envision.com.kg/api/v1/reviews/{id}/


<h3>If you didn't understand something, you can write to me in a telegram(https://t.me/muhxaa ) or in whatsapp(+996705560060)</h3>
