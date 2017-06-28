![Azure Functions + Python HTTP](http://mediarealm.com.au/wp-content/uploads/2016/05/Azure-Functions-Python-HTTP.png)

# HomeRun Checker Azure Function + Python HTTP Example Code With Requests 
*Example code for Azure Functions (written in Python).*

This example code is designed to demonstrate how to use Azure Functions with Python for HTTP Triggers. It demonstrates:

* Receiving GET (Query String) data
* Posting a Reply with Custom Formatting

This package includes the requests library and all dependencies. It shows how to use requests to get recent mlb notifications from http://gd2.mlb.com/components/game/mlb/notifications.json and returns any notifications that contain the text "homerun". 

A helper library from (http://mediarealm.com.au/articles/2016/05/azure-functions-python-http-example-code/) is included which would allow parsing of input strings, and other functions. I decided that requests was a more pleasant library to use for the http stuff but kept the helper lib in place for reference.

Included is a simple HTTP Helper Class to parse the input data. This should make code changes easier when the Azure Functions team introduce a new interface for Python.

