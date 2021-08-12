from flaskblog import app, bcrypt, db
import json

with open('./posts.json') as f:
  data = json.load(f)
print(type(data))

for item in data:
  print(item)
  print(type(item))
# print(data)

# snipp for adding posts
for js in data:
  post = Post(title=js['title'], content=js['content'], user_id=js['user_id'])
  db.session.add(post)

db.session.commit()

import os
clear = lambda: os.system('cls')
clear()

