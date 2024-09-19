import vk_api as vkpi
from api_key import vk_key, yan_key
import datetime
from yandex_geocoder import Client

sigmund = 10


def address_to_coordinate(a):
    client = Client(yan_key)
    coordinates = client.coordinates(a)
    return (coordinates)


def unix_to_date(unix_timestamp):
    date_obj = datetime.datetime.fromtimestamp(unix_timestamp)
    date_formatted = date_obj.strftime('%d:%m:%y')
    return date_formatted


def search_vk_posts(token, query, address, count=sigmund):
    vk_session = vkpi.VkApi(token=token)
    vk = vk_session.get_api()
    if address != "":
        coordinate = address_to_coordinate(address)
        posts = vk.newsfeed.search(q=query, count=count, latitude=coordinate[1], longitude=coordinate[0])['items']
        print(f'latitude = {coordinate[1]}, longitude = {coordinate[0]}')
    else:
        posts = vk.newsfeed.search(q=query, count=count)['items']
    return [[post['date'], post['text'], f'https://vk.com/wall{int(post["from_id"])}_{post["id"]}'] for post in
            posts
            if 'промокод' not in post['text'].lower() and 'скидк' not in post['text'].lower() and 'акци' not in post[
                'text'].lower()
            and 'промо' not in post['text'].lower() and 'продам' not in post['text'].lower() and 'продаж' not in post[
                'text'].lower() and 'магазин' not in post['text'].lower()]
