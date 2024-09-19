from api import search_vk_posts
import vk_api as vkpi
from api_key import key
import numpy as np
import time

sigmund = 100 # amount of posts to read per use

id = 687
from_id = '-225405295'

keywords = ['space']   #из тгбота

print(f'https://vk.com/wall{from_id}_{id}')

def search_vk_posts(token, query, count=sigmund):
    vk_session = vkpi.VkApi(token=token)
    vk = vk_session.get_api()
    posts = vk.newsfeed.search(q = query, count=count)
    return [{'text': post['text'], 'date': post['date']} for post in posts]

def get_vk_posts(token, owner_id, count=sigmund):
    vk_session = vkpi.VkApi(token=token)
    vk = vk_session.get_api()
    posts = vk.wall.get(owner_id=owner_id, count=count)['items']
    return [{'text': post['text'], 'date': post['date']} for post in posts]

def filter_posts_by_keywords(posts, keywords):
    filtered_posts = []
    for post in posts:
        if any(keyword.lower() in post['text'].lower() for keyword in keywords):
            filtered_posts.append(post)
    return filtered_posts


for i in range(0, len(filter_posts_by_keywords(get_vk_posts(key, id), keywords))):
    print(filter_posts_by_keywords(get_vk_posts(key, id), keywords)[i]['text'])
    print(time.gmtime(filter_posts_by_keywords(get_vk_posts(key, id), keywords)[i]['date']))
    print("__________________________________________________________________")