# This works to test wp.GetUsersBlogs which is the most common xmlrpc brute force vector. I think this should be sufficient for our use. 

from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.users import GetUsersBlogs
from wordpress_xmlrpc.methods.demo import SayHello
import xmlrpc.client

wp = Client('https://www.dmeinterns.org/xmlrpc.php', 'loughrjl', 'password1')

try:
	call= wp.call(GetUsersBlogs())
	
except xmlrpc.client.ProtocolError as err:
	auth_test = ("%d" % err.errcode, "%s" % err.errmsg)
	if err.errcode == 405:
		print('Authentication disabled. This site is protected from XMLRPC brute force attacks')
