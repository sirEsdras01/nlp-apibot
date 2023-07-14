from googlesearch import search
#An application programming interface or API is a software interface for two applications or services to talk to each other.
#The GET request is used to retrieve information using a given URL.
#A POST request is used to send information to a server.
#The DELETE method is used to request the server to delete a file at a location specified by the given URL.

# query string to search on Google
query = "As you are by Harry Styles"

# number of top search results to fetch
numResults = 3
#The googlesearch Python library is used to do an effective Google search.
google_search_results = list(search(query, stop=numResults, pause=1))

print("Here's a list of the top {} search results on Google:\n".format(numResults))
print(google_search_results)