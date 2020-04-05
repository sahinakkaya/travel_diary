### Build instructions
In order to build and run

`docker-compose up -d --build`

Since it creates a fresh database, you need to apply migrations and create a superuser to use the API properly:

```
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
```
Then you can visit [your localhost](http://localhost:8000/) to browse the API.



### Notes
I have only completed the backend part of the project despite all my efforts. I had never used any of the 
technologies I was asked to use before (django, django rest, kafka, angular, spring and docker to be explicit).
So I decided to start learning from django since it is at least python related. It went well for me and
made me think that I should use Django more after this project. I have also implemented jwt for authentication
using djangorestframework-simplejwt but didn't include it here since it's hard to test my API with it without
having a frontend. Then it was the time for logging. I do my research about kafka and learned basic concepts, 
however couldn't manage to integrate it with my project. So the logging part remained as a single print 
statement in my code ¯\_(ツ)_/¯

Lastly, it was time for me to learn some frontend. Instead of following the official documentation for angular,
I decided to follow a tutorial on making a website using django rest as backend and angular as frontend since 
I didn't know anything about Angular literally. And it was really a painful process. The tutorial basically 
doesn't work! At the end, it shows a bunch of colorful buttons for creating or deleting something but my 
buttons aren't even clickable! I rewrote the whole thing couple of times but the result was same. The bad side
was, I learned nothing because the [tutorial](https://grokonez.com/frontend/django-angular-6-example-django-rest-framework-angular-crud-mysql-example-part-3-angular-client)
was like, "now copy these lines to 'some/file/that/i/have/no/clue/about/it'"

I decided to switch to another tutorial but this time I was picky. I knew that I need something that I can 
actually learn from. I found [this](https://www.techiediaries.com/angular-crud-tutorial-consume-a-rest-api/),
and it looked OK to me. I completed part 1 and have a feeling of I will finally be able to finish this project.
Components are like templates in a Django project and services are where all the logic lies, like views in Django.
OK, it makes more sense now. Let's move to part 2 which is about routing. Done! Let's move to part 3...
Disappointment. The author didn't published the part 3 yet :(

OK, never give up! Combine all the codes that I get from tutorial 1 and all the knowledge from tutorial 2 then fill
the gaps. Perfect plan! Did it work? Well, yes but actually no. Theoretically, I managed to list the data that I get
from an endpoint of an API but I don't have time to integrate it with my code. 

So that's all. Of course there are lots of thing that I didn't mention about but I need to end this before it becomes
a wailing wall. Thank you for all your patience while reading. 

Best,
Şahin

