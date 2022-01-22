import xmlrpc.client
from wordpress_xmlrpc.methods.users import *
from wordpress_xmlrpc import Client

print("URL Format: example.org\n")
server_input = input("Enter the URL: ")
print("\nThe following calls require authentication and may be brute forced: \n")

server = xmlrpc.client.Server(f"https://www.{server_input}/xmlrpc.php")

authenticated_methods = ["wp.getUsersBlogs", 			  
			 "wp.getUsers", 
			 "wp.getProfile", 
			 "wp.getAuthors", 
			]

methods = server.system.listMethods()

find_authenticated_methods = set(methods).intersection(authenticated_methods)
for auth_methods in find_authenticated_methods:
    print(auth_methods, end=", ")
    print("\b\b", end="")
    print(" \n")
    
test = input("Would you like to test the exploitability of these methods? Y/N: ")

if(test.lower().startswith('y')):
    wp_methods = []
    blogger_methods = []
    mw_methods = []
    mt_methods = []
    for method in find_authenticated_methods:
        if(method.startswith('wp.')):
            temp_method = method.replace("wp.", "")
            wp_methods.append(temp_method[:1].upper() + temp_method[1:])
        if(method.startswith('blogger.')):
            temp_method = method.replace("blogger.", "")
            blogger_methods.append(temp_method[:1].upper() + temp_method[1:])
        if(method.startswith('mw.')):
            temp_method = method.replace("mw.", "")
            wp_methods.append(temp_method[:1].upper() + temp_method[1:])
        if(method.startswith('mt.')):
            temp_method = method.replace("mt.", "")
            wp_methods.append(temp_method[:1].upper() + temp_method[1:])

wp = Client(f"https://www.{server_input}/xmlrpc.php", 'loughrjl', 'password1')

for method in wp_methods:
    try:
        call= wp.call(locals()[method]())
        
    except xmlrpc.client.ProtocolError as err:
        auth_test = ("%d" % err.errcode, "%s" % err.errmsg)
        if err.errcode == 405:
            print('Authentication disabled. This site is protected from XMLRPC brute force attacks')
            

    except RuntimeError as err:
        print(err)

    except:
        print("testing", method, "didn't work")


