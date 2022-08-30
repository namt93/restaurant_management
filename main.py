from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

# global database
my_posts = [{"title": "title of content 1", "content": "content of post 1", "id": 1},{"title": "favorite foods", "content": "I like pizza", "id": 2}]

# request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}

#@app.post("/createposts")
#def create_posts(payload: dict = Body(...)):
#    print(payload)
#    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}


# ultimate a data we expect
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.post("/posts")
def create_posts(new_post: Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0,10000)
    my_posts.append(post_dict)
    return {"data":post_dict}
