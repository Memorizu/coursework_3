import pytest
from bp_posts.posts_dao import PostDao
from config import POST_PATH


class TestPostDao:

    def test_load_posts(self):
        pass

    def test_get_posts_by_user(self):
        post_dao = PostDao(POST_PATH)
        assert post_dao.get_posts_by_user('leo') == {
    "poster_name": "leo",
    "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
    "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
    "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
    "views_count": 376,
    "likes_count": 154,
    "pk": 1
  }

        pass




