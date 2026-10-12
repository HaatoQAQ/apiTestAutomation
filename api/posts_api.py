from asyncio import timeout
from time import time
from zoneinfo import reset_tzpath

import requests
from config.config import Config

class PostsApi:
    def __init__(self, session=None):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT
        self.session = session or requests.session()

    def get_post(self, post_id):
        return self.session.get(
            f"{self.base_url}/posts/{post_id}",
            timeout=self.timeout
        )

    def get_posts(self, user_id=None):
        # 三元表达式,user_id,没传值,默认查所有人的帖子,传值就只查询固定人的帖子
        params = {"userId": user_id} if user_id else {}
        return self.session.get(
            f"{self.base_url}/posts",
            params = params,
            timeout = self.timeout
        )

    def create_post(self, data):
        return self.session.post(
            f"{self.base_url}/posts",
            json=data,
            timeout=self.timeout
        )

    def update_post(self, post_id, data):
        return self.session.put(
            f"{self.base_url}/posts/{post_id}",
            json=data,
            timeout=self.timeout
        )

    def delete_post(self, post_id):
        return self.session.delete(
            f"{self.base_url}/posts/{post_id}",
            timeout=self.timeout
        )