# Flask Blogging Website

## Flask App

Documentation: [Flask Blogging Website]()

Docker Image @  [DockerHub](https://hub.docker.com/r/giraycoskun/flask-blog)

### Usage

(Still under-development so not working properly)

Using via **Github**

(configure .env)

```
git clone https://github.com/giraycoskun/Flask-Blogging-Website.git
```
```
docker-compose build
```
```
docker-compose run
```

Using via **DockerHub**

(Only includes Docker Image of Flask App)
```
docker pull giraycoskun/flask-blog
```


### Dependencies

- Docs: https://flask.palletsprojects.com/en/2.2.x/

- https://docs.gunicorn.org/en/stable/

### Website Templates

[Clean Blog Template](https://startbootstrap.com/theme/clean-blog)

[Login Form Template](https://colorlib.com/wp/template/login-form-v1/)

[404 Template](https://colorlib.com/wp/template/colorlib-error-404-3/)

### Services

- MySQL
  - Official Image @ [DockerHub](https://hub.docker.com/_/mysql)
- Nginx
  - Official Image @ [DockerHub](https://hub.docker.com/_/nginx)

---

## Notes during Development

### MySQL Commands

```
docker run --rm -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=flask-blog -p 3306:3306 mysql:latest
```

```
mysql --host=127.0.0.1 -P 3306 --user=root --password=root flask-blog
```

```
CREATE USER db_user IDENTIFIED BY 'db_password';
GRANT ALL ON 'flask-blog'.* TO db_user;
```

---

## Help

### Helpful Articles & Tutorials

- https://towardsdatascience.com/how-to-set-up-a-production-grade-flask-application-using-application-factory-pattern-and-celery-90281349fb7a

- https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d

### Helpful Resources

- https://cdnjs.com/

---

by giraycoskun