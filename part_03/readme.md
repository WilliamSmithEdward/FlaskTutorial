# Part 03

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-templates

### Things I Learned Settings Up A Ubuntu Linux Environment (Linode)

Update IP tables so that port 8080 routes to 80: https://serverfault.com/questions/112795/how-to-run-a-server-on-port-80-as-a-normal-user-on-linux

```shell
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```

Update microblog.py to work with Waitress library: https://stackoverflow.com/questions/12269537/is-the-server-bundled-with-flask-safe-to-use-in-production

```py
from waitress import serve

...

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080, url_scheme='https')
```

```shell
python3 microblog.py
```

#### Unfortunately it looks like waitress does not support https requests. Need to solve for this down the road.

The following site suggests using a combination of gunicorn and nginx to reverse proxy an https request to an WSGI instance. Seems like Waitress and Gunicorn serve similar purposes. I'll need to look into this. https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

### I'm thinking about how I can have a Python script run without hanging the terminal. Suggestions:

* https://stackoverflow.com/questions/50792048/running-a-python-script-without-opening-terminal
* https://superuser.com/questions/446808/how-to-manually-stop-a-python-script-that-runs-continuously-on-linux

### Flask Redirection Mechanics

I noticed that in the example "/" and "/index" both route to the index() function. I questioned how url_for would know which endpoint to redirect to. It seems Flask's default behavior is to route to the endpoint defined in the last decorator before the function. Reading this stackoverflow post gave me insight to the Alias parameter of the decorator, which marks the endpoint as not active for url_for and overrides the default redirect behavior.

https://stackoverflow.com/questions/7782046/how-do-i-use-url-for-if-my-method-has-multiple-route-annotations