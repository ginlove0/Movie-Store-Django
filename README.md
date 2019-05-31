## ISD Movie Store Assignment

# Application Structure

1. cart: Managing cart by using session

2. movie: Managing all movies of the store

3. MovieStore: Main setting application (Don't touch this)

4. order: Managing customer order

5. user: customer feature

6. templates: the "View" of the MVC, user interface


# Template (the "View") files structure

1. base.html: template extending, ou can use the same parts of your HTML for different pages of your website.
Plase put all your css and js link in this file

2. headers.html: app header, navbar

3. registration: view for user app

4. movie: view for movie app

# How to run

## 1 Make miragte the database
```
docker-compose run moviestore python /app/manage.py migrate
```
## 2 Create local admin

```
docker-compose run moviestore python /app/manage.py createsuperuser
```
## 3 Run the application
```
docker-compose up
```

# Show database

## 1 Know postgres Database container ID by running
docker ps
## 2 Access it with container ID
docker execc -it <container-id> bash
## 3 Access postgres shell script
psql -U postgres
## 4 Show all the databases
\l
## 5 Show all tables
\dt
## 6 Make query
select * from movie_movie;