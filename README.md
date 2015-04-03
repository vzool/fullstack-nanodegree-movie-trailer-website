## Full-Stack Nanodegree Movie Trailer Website

This is a python application working as a web server which is serving my best Movies Trailer, I hope that we met in something interesting in common.

## Application File Structure

I organized the app files with consideration of isolation which is based on functionality.

```
	app.py		(Server Startup File)
	app
	|
	|- db 		(All App Data, ex: Movie Data)
	|- http 	(Website Root)
	|- lib 		(All App Library)
	|- model	(All App Models)
	|- view		(All App Views)

```

## What is Happening inside this App?

When you run this command

```

$ python app.py

```

The application will do its objective as following:

1. Read Movie data from app.db.movie.
2. Call fresh_tomatoes.open_movies_page.
3. Then a file will be generated with name index.html at app/http directory.
4. App will create A Thread to open website after deploy.
5. WebServer will be started at app/http forever until you press CTRL + C.

I use Thread because when you already start WebServer the app will be busy on serving HTTP requests on main Thread.
So, to solve this problem I create another Thread for anything I can do when main Thread is busy. 


## Instructions

Our application is a client/server base.

So, you will run both of them to experiment this app.

### Server side

To run this Web Application you will need to run app.py in command line as following:

```

$ python app.py

```

After that application server will open browser directly after deploy the system.

Application will run normal on port 13579, so if you want to change that port you can use this method:

```
$ python app.py PORT_NUMBER
```


### Client side

To run this application on the client side you need to run the server first then the app.py will automatically open an app with the default browser in your system.
If that never happened by any reason, open this url in your favorite browser:

```

http://127.0.0.1:13579

```

## Requirements

### Server side

You need a Python 2.x language installed in your server system.

### Client side


To run this Web Application you will need a browser which should be in specific versions that fully supports the JavaScript language, which those browsers and versions are:

- Chrome: 4.0+
- IE(Internet Explorer): 9.0+
- Firefox: 2.0+
- Safari: 3.1+
- Opera: 9.0+

## Licence

It's Completely Free. But, Do whatever you like to do on your own full responsibility;

This licence is known with [MIT License](http://vzool.mit-license.org/) in professional networks.
