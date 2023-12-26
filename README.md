# Acme Blog api quick start guide#
This API was built with the Django Rest Framework (DRF) 
and was deployed on render.
to visit deployment go to `https://blog-api-val0.onrender.com/` on your browser

##Setup local environment##
To run the development server follow these steps (please take note to properly run the following commands on your terminal):

1. **Create virtual environment (env)**: Start by creating a virtual environment using python venv package. Run `python -m venv env`
2. **Activate virtual environment**: Activate the virtual environment by running this command `env/Scripts/activate`
3. **CD into blog directory**: run `cd/blog`
4. **Install dependencies**: run `pip install -r requirements.txt`
5. **Start development server**: run `py manage.py runserver` it should start a development server at `http://localhost:8000`

## Access docs ##
If your dev server is running visit `http://localhost:8000/docs` to access the swagger docs for the project. there you should see a list of all endpoints in the project
**Please note**: certain requests that have to do with submitting images arent working properly on the swagger doc so you to test those requests, simply type the url endpoint of the request on your browser
and visit the associated page, there you can test the endpoint with the DRF endpoint testing form. This is an alternate way of testing endpoints.
For example the `/users/update-profile-image` endpoint doesnt work properly on swagger but if you visit `http://localhost:8000/users/update-profile-image` on your browser you will see a UI from DRF 
that you can use to test the endpoint
