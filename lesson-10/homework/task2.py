import requests
api_key="64f2fa557eb79338bc9941bf5d29df84"
base_url = "https://api.themoviedb.org/3/search/movie"

query = input("Enter movie genre: ")  


response = requests.get(base_url, params={"api_key": api_key, "query": query})

# Print the JSON response
print(response.json())