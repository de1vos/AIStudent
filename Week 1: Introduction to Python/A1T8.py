# Task 8: Python dictionaries vs Dataclasses

# Activate the virtual environment again you created in Task 7. 
# We will now decode the JSON response from the API into a Python dataclass. 
# Dataclasses are a typed alternative to dictionaries (`{}`). 
# Dataclasses extend the functionality of dictionaries by allowing 
# you to make the dictionary conform to a schema. Dataclasses are also a class 
# which means you can add methods to them unlike to dictionaries.

## Tasks:
# - Create a dataclass `Post` with attributes `userId`, `id`, `title`, and `body`.
# - Decode the JSON response from the API into an instance of the `Post` dataclass. 
#   Repeat for 3 posts.

## Starting Point:
# ```python
import requests
import json

from dataclasses import dataclass

@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str

posts = []

# Decode the JSON response into a Post instance
for post_id in range(1, 4): 
    # URL: https://jsonplaceholder.typicode.com/posts/{post_id}
    # post_id is a number from 1 to max number of posts
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    post_data = json.loads(response.content)

    post = Post(userId=post_data["userId"], id=post_data["id"], title=post_data["title"], body=post_data["body"])
    posts.append(post)

# Print posts stored as dataclass instances
for i, post in enumerate(posts):
    print(f"Post {i+1}:")
    print(f"    User ID: {post.userId}")
    print(f"    ID: {post.id}")
    print(f"    Title: {post.title}")
    print(f"    Body: {post.body}\n")

# NOTE: post.userId to access the userId of the post

## Expected Output:
# ```
# Post 1:
#     User ID: 1
#     ID: 3
#     Title: ea molestias quasi exercitationem repellat qui ipsa sit aut
#     Body: et iusto sed quo iure
# voluptatem occaecati omnis eligendi aut ad
# voluptatem doloribus vel accusantium quis pariatur
# molestiae porro eius odio et labore et velit aut
# 
# Post 2:
#     User ID: 1
#     ID: 2
#     Title: qui est esse
#     Body: est rerum tempore vitae
# sequi sint nihil reprehenderit dolor beatae ea dolores neque
# fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis
# qui aperiam non debitis possimus qui neque nisi nulla
#
# Post 3:
#     User ID: 1
#     ID: 3
#     Title: ea molestias quasi exercitationem repellat qui ipsa sit aut
#     Body: et iusto sed quo iure
# voluptatem occaecati omnis eligendi aut ad
# voluptatem doloribus vel accusantium quis pariatur
# molestias et enim adipisci aut delectus
# ```