def assert_status(resp, expeted=200):
    assert resp.status_code == expeted, \
    f"状态码错误: 预期 {expeted}, 实际 {resp.status_code}"

def assert_json_key(resp, key):
    assert key in resp.json(), \
    f"响应缺少字段 {key}"

def assert_json_value(resp, key, expected):
    value = resp.json().get(key)
    assert value == expected, \
    f"字段{key}错误,预期 {expected}, 实际 {value}"

def assert_response_time(resp, max_seconds=2):
    elapsed = resp.elapsed.total_seconds()
    assert elapsed < max_seconds, \
    f"响应时间过长, 预期 {max_seconds}s, 实际 {elapsed}s"

