import pytest
import yaml
import allure
from allure_pytest.utils import allure_links

from common.assert_util import (
    assert_status,
    assert_json_key,
    assert_response_time,
    assert_json_value
)
from conftest import posts_api


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

@allure.epic("jsonplaceholder 接口测试")
@allure.feature("帖子管理")
class TestPosts:

    @allure.story("查询帖子")
    @allure.title("获取单个帖子")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_post(self, posts_api):
        r = posts_api.get_post(1)
        assert_status(r,200)
        assert_json_key(r,"title")
        assert_json_value(r,"id",1)

    @allure.story("查询帖子")
    @allure.title("参数化获取多个帖子")
    @pytest.mark.parametrize("posts_id", [1,2,3])
    def test_get_post_param(self, posts_api, posts_id):
        r = posts_api.get_post(posts_id)
        assert_status(r,200)
        assert_json_value(r,"id",posts_id)

    def test_get_posts_userId(self, posts_api):
        r = posts_api.get_posts(user_id=1)
        assert_status(r,200)
        data = r.json()
        assert len(data) > 0
        for item in data:
            assert item["userId"] == 1

    def test_create_post(self, posts_api):
        data = load_yaml("data/posts_data.yaml")["create_post"]
        r = posts_api.create_post(data)
        assert_status(r,201)
        assert_json_value(r,"title",data["title"])

    def test_update_post(self, posts_api):
        data = load_yaml("data/posts_data.yaml")["update_post"]
        r = posts_api.update_post(1,data)
        assert_status(r, 200)
        assert_json_value(r, "title", data["title"])

    def test_delete_post(self, posts_api):
        r = posts_api.delete_post(1)
        assert_status(r, 200)