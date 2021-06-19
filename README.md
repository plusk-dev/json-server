# JSON Server

## An tiny CLI to load data from a JSON File during development.

<br>

After installing `json-server` by

```
pip install json_server
```

You can run

```
json_server <path-to-JSON-file> <port:optional>
```

The port argument defaults to `5000` <br>

This shall output:

```
 * Serving Flask app 'json_server.main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 816-527-262
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Which is similar to what a standard Flask app logs.

Now that you have run the command, `http://127.0.0.1:<port>/` shall respond with your JSON.
