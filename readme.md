## 项目名称：spider_lagou
## 项目介绍
--------------------------------------------------
本项目是爬取拉钩网站的职位信息，包括职位信息摘要和职位详情！
最终爬取结果保存到文件中。
## 项目使用方式
<pre>python spider_lagou/get_data.py</pre>

## 项目依赖包
1. beautifulsoup4
2. 安装方式
<pre>pip install beautifulsoup4</pre>

## 项目提醒
1. 更改相关参数，请在global_config.py文件中更改，参数介绍如下
<pre>
# 参数的key值不能更改， value值可以更改，value值除了结果文件存放目录不为空，其它默认为空
SPIDER_PARAM = {
    'position_key': '数据分析', # 职位关键字
    'city_key': '',  # 职位所在城市关键字
    'district_key': '',  # 职位所在城市地区关键字
    'result_file_name': result_file_name  # 结果文件名称
}
</pre>
2. 若要更改更多的内容，可以详细阅读代码，代码有相关注释！

## PS：欢迎拍砖
