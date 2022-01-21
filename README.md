# WordPress-XMLRPC-Scanner

This is a WordPress XMLRPC scanner created by the DME Web Security team. It uses the Python xmlrpc.client library to make calls to test the exploitability of authenticated and pingback.ping methods. 

Dependancies 

1/21/2022
method_scan.py only asks the server what XMLRPC methods are available then prints a list of methods that require authentication. 
method_test.py only tests wp.getUsersBlogs for now. 

TODO: 
1. Merge method_test and method_scan. 
2. Find what error code/message a vulnerable WP site gives when authentication is enabled but the credentials are incorrect.
3. Implement testing for pingback.ping. 

Documentation:

https://python-wordpress-xmlrpc.readthedocs.io/en/latest/overview.html
https://docs.python.org/3/library/xmlrpc.client.html
