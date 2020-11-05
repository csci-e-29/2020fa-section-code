# Section 11 - REST

We're wrapping up the Django section by creating this culmination of everything we've worked on. We'll take our project and add a Swagger interface and combine it with a Zappa deployment!


### Walkthrough

0. Begin by launching the webserver and taking a look around
```python manage.py runserver```. You'll see the same two features as last time (webpage and forms). Make sure to `makemigrations`/`migrate` as well so that we have our sqlite database

1. One of the new features we have now is the swagger spec! You can see that at
```http://127.0.0.1:8000/people/swagger/```. Play around with the GET and POSTS request - you can create a new person for fun

2. You can see the redoc version at ```http://127.0.0.1:8000/people/redoc/``` or the Django REST framework at ```http://127.0.0.1:8000/people/people-serializer/```


### Optional - Deployment

Now that we've seen the API, we want to deploy this via Zappa. 

0. Make sure you have your AWS credentials in the .aws directory - you can check this with `cd ~/.aws `

1. Begin by running `zappa init` within the pipenv environment. For the config settings that pop up, just click enter through them - accept their defaults. At the end of this, we should see a zappa_settings.json file being created. We DO NOT want to commit this.

2. Let's begin our deployment! It's as easy as doing `zappa deploy`.

3. You'll see a "Deployment complete" popup, as well as an url - keep track of that URL, it's where our project has been deployed to! Click on the link.
 
4. Uh oh! No worries, we have to do a few things now so that Django is configured to work with our AWS Lambda site. Copy that url from the previous step and go into the settings. Find `ALLOWED_HOSTS` and replace the empty list with 
`ALLOWED_HOSTS = ["127.0.0.1", "<<myurl>>.execute-api.us-west-2.amazonaws.com"]`

5. Towards the bottom of `settings.py`, add the following:

```
S3_BUCKET = "<<my_zappa_bucket>>"

STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"

AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET

STATIC_URL = "https://%s.s3.amazonaws.com/" % S3_BUCKET
```

`<<my_zappa_bucket>>` is the name of your aws bucket that everything gets deployed to - you can also find this in your `zappa_settings.json` file.

6. Time to mess around with some AWS configurations - we'll need to go to the AWS console at this point (https://aws.amazon.com/console/)

7. Click on S3 

8. We should see our Zappa bucket! Click on that, then click the "Permissions" tab.

9. We're going to be edit our "CORS Configuration". Add the following and save.

```
<CORSConfiguration>
      <CORSRule>
            <AllowedOrigin>*</AllowedOrigin>
            <AllowedMethod>GET</AllowedMethod>
            <MaxAgeSeconds>3000</MaxAgeSeconds>
            <AllowedHeader>Authorization</AllowedHeader>
      </CORSRule>
</CORSConfiguration>
```

10. We're now going to push all of our static files to s3 - do so via the following commands:

```
python manage.py collectstatic --noinput
```

<b> This will take a while! Do NOT quit </b>

11. We'll need to switch this to our sqlite database on S3, not our local database - change this by going again into the settings.py

```
DATABASES = {
    "default": {
        "ENGINE": "django_s3_sqlite",
        "NAME": "db.sqlite3",
        "BUCKET": "<<my_bucket>>",
    }
}
```

12. We also need to update our `zappa_settings.json file`; add this line to the bottom `"use_precompiled_packages": false,`

13. And now let's re-do our deployment once again with all of our changes.

```
zappa update
```

14. We'll need to do one more command: 
`zappa manage dev migrate`. Some weird bug, see [here](https://github.com/FlipperPA/django-s3-sqlite/issues/5) 

15. Finally, go and check out our website! It's live again and this time you will see everything.

16. We can submit requests as follows:

```
import requests
requests.post("https://<<my_server>>.execute-api.us-west-2.amazonaws.com/dev/people/people-serializer/person/", 
json={'name': 'MY NAME', 'email': 'abc@gmail.com', 'job_title': 'MY JOB TITLE', 'bio': 'MY BIO'})
```

17. We can pull the data as follows:

```
temp = requests.get("https://<<my_server>>.execute-api.us-west-2.amazonaws.com/dev/people/people-serializer/person/")
temp.text
```


A few notes - this can definitely be improved. Some suggestions: a. don't use a sqlite3 database, configure one specifically w/ AWS such as Postgres. b. some authentication! Oauth is a good choice here

#### Helpful guides

* For the Django [Swagger spec](https://github.com/axnsan12/drf-yasg)
* Setting up [databases with Zappa](https://romandc.com/zappa-django-guide/walk_database/)
* Sqlite [database with Zappa](https://github.com/flipperpa/django-s3-sqlite)
* Django zappa deployment [tutorial](https://www.agiliq.com/blog/2019/01/complete-serverless-django/#go-to-django-app)