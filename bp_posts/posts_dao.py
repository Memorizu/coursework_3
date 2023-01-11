import json
from json import JSONDecodeError


class PostDao:

    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"Путь: {self.path}"

    def load_posts(self):
        try:
            with open(self.path, encoding='utf-8') as file:
                data = json.load(file)
                return data
        except JSONDecodeError:
            return None

    def get_all_posts(self):
        return self.load_posts()

    def get_posts_by_user(self, user_name):
        posts = self.get_all_posts()
        post_by_name = []
        try:
            for post in posts:
                if user_name == post['poster_name']:
                    post_by_name.append(post)
                if post['content'] is None:
                    return []
            return post_by_name
        except ValueError:
            return 'Такого пользователя нет'

    def search_for_posts(self, query):
        posts = self.get_all_posts()
        lst_posts = []
        for post in posts:
            if query.lower() in post['content'].lower():
                print(post)
                print(type(query))
                lst_posts.append(post)
        return lst_posts

    def get_post_by_pk(self, pk):
        posts = self.get_all_posts()
        try:
            for post in posts:
                if pk == post['pk']:
                    return post
            return
        except ValueError:
            return "Такого пользователя нет"



