Given a CVS of restaurants and their hours,
create an api that accepts a date time string
and returns a list of restaurants open at that time.

1. Create Repo and initial setup.
2. Django Setup
3. Setup Models
   - show some Normalization? Restaraunt Model/Buisness Model with type? Day model-name, is_weekend, hours of operations model
4. Add Models to Admin Panel
5. Create Parser for CSV file on init command? Maybe pull from a location and upload it? Allow for a way to drop file just within the file structure and upload from it on click in admin panel?
   - should consider updates via CSV file...
6. Actually Parse file, with breaks on "," and "/" watching for any gotchas along the way. Make setup for Mon, Tues, Wed, Thu, Fri, Sat, Sun. "-" Character will setup a from first day to next day with said time. also making sure to take into account the possible additional days.
7. Create endpoint to show info, possibly include django-filter? if there is enought to filter on.
8. Contanerize for bonus points.

Run Tests:

```
python manage.py test
```

Run Tests for Coverage and report:

```
coverage run ./manage.py test
coverage report -m
```

Curl command for results:

```
 curl -X GET http://localhost:8000/restaurants/open_restaurants/\?time\=Monday@12:00pm
```

Docker Setup:

```
docker build -t liine_app .
docker run -d -p 8000:8000 --name my-django-container liine_app:latest
docker ps
```
