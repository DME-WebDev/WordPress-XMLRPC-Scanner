# Server is telling us what methods are available. Doesn't tell us if authentication is enabled. 

import xmlrpc.client

print("URL Format: example.org\n")
server_input = input("Enter the URL: ")
print("\nThe following calls require authentication and may be brute forced: \n")

server = xmlrpc.client.Server(f"https://www.{server_input}/xmlrpc.php")

authenticated_methods = ["wp.getUsersBlogs", "wp.getUsersBlogs", "wp.newPost","wp.editPost", "wp.deletePost", "wp.getPost","wp.getPosts", "wp.newTerm", "wp.editTerm", "wp.deleteTerm", 
"wp.getTerm", "wp.getTerms", "wp.getTaxonomy", "wp.getTaxonomies", "wp.getUser", "wp.getUsers", 
"wp.getProfile", "wp.editProfile", "wp.getPage", "wp.getPages", "wp.newPage", "wp.deletePage", 
"wp.editPage", "wp.getPageList", "wp.getAuthors", "wp.getTags", "wp.newCategory", "wp.deleteCategory", "wp.suggestCategories", "wp.getComment", "wp.getComments", "wp.deleteComment", "wp.editComment", "wp.newComment", "wp.getCommentStatusList", "wp.getCommentCount", "wp.getPostStatusList", "wp.getPageStatusList", "wp.getPageTemplates", 
"wp.getOptions", "wp.setOptions", "wp.getMediaItem", "wp.getMediaLibrary", "wp.getPostFormats", 
"wp.getPostType", "wp.getPostTypes", "wp.getRevisions", "wp.restoreRevision", "blogger.getUsersBlogs", "blogger.getUserInfo", "blogger.getPost", "blogger.getRecentPosts", 
"blogger.newPost", "blogger.editPost", "blogger.deletePost", "mw.newPost",
"mw.editPost", "mw.getPost", "mw.getRecentPosts", "mw.getCategories", "mw.newMediaObject", 
"mt.getRecentPostTitles", "mt.getPostCategories", "mt.setPostCategories"]

methods = server.system.listMethods()

find_authenticated_methods = set(methods).intersection(authenticated_methods)
for auth_methods in find_authenticated_methods:
	print(auth_methods, end=", ")
	print("\b\b", end="")
	print(" \n")
	
test = input("Would you like to test the exploitability of these methods? Y/N: ")

#make the calls and return output
