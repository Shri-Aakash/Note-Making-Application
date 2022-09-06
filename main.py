from website import create_app

app=create_app()
if __name__=='__main__':
    app.secret_key='12345'
    app.run(debug=True) ##Whenever a change is made to the python code the web server is re-run.
    #On running the above line of code we get an error URL not found on copying the fiven URL into the browser
    #This actually means that our website is running but does not have any routes or homapage or anything.


