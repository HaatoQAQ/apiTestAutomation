# 接口自动化测试项目

## 技术栈
- Python
- Requests
- Pytest
- Allure
- PyYAML

## 项目结构
- config：配置
- api：接口封装
- common：公共断言
- data：测试数据
- testcases：测试用例

## 运行方式
pip install -r requirements.txt
pytest

## 生成 Allure 报告
pytest --alluredir=./results
## 网页查看
allure serve ./results
## 生成离线报告
allure generate ./results -o ./allure-report --clean
## 打开测试报告
allure open ./allure-report

## 覆盖场景
- 帖子查询、创建、更新、删除
- 参数化
- 异常场景
- 断言封装
- 数据驱动