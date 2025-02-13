## Task 7: Installing and Using External Libraries
# In python, the standard package manager is `pip`. You can use `pip` to install external libraries that are not part of the standard library. In this task, you will install the `requests` library and use it to make a simple HTTP GET request to a public API. The `requests` library is a popular library for making HTTP requests in Python and does not come pre-installed with Python. 
# We will install the package into a virtual environment, using `venv`. Virtual environments help us separate the dependencies for different projects and is a best practice in Python development.

## Tasks:
# - Create a virtual environment using `venv`.
# - Activate the virtual environment.
# - Install the `requests` library using `pip`.
# - Use the `requests` library to make a GET request to the URL `https://jsonplaceholder.typicode.com/posts/1` and display the response content.

## Starting Point:
# If you are using MacOS or Linux, you can create a virtual environment using the following commands:
# ```bash

# Create a virtual environment
# python3 -m venv venv

# Activate the virtual environment
# source venv/bin/activate

# After activating the virtual environment, you can install the `requests` library using `pip`:
# ```bash
# pip install requests
# ```

# Now you can use the `requests` library to make an HTTP GET request:
# ```python
# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.content)
# ```

# To reproduce the environment, you can create a `requirements.txt` file using the following command:
# ```bash
# pip freeze > requirements.txt
# ```

# You can install the dependencies from the `requirements.txt` file using the following command:
# ```bash
# pip install -r requirements.txt
# ```

# Lastly, to deactivate the virtual environment, you can use the following command:
# ```bash
# deactivate # For both MacOS/Linux and Windows
# ```

## Expected Output:
# The output should be the content of the response from the API, which is a JSON object representing a post. It should look something like this:
# ```python
# b'{\n  "userId": 1,\n  "id": 1,\n  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",\n  "body": "quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto"\n}'
# ```