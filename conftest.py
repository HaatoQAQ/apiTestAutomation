import pytest
from api.posts_api import PostsApi

@pytest.fixture(scope="session")
def posts_api():
    # 全局公用 PostApi 实例
    return PostsApi()