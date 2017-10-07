#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'zhaotingting'
__Date__ = '20170927'

# 爬取的数据保存的文件
result_file_name = 'data_analysis.csv'

# 爬取数据设置参数
# 参数的key值不能更改， value值可以更改，value值除了结果文件存放目录不为空，其它默认为空
SPIDER_PARAM = {
    'position_key': '数据分析', # 职位关键字
    'city_key': '',  # 职位所在城市关键字
    'district_key': '',  # 职位所在城市地区关键字
    'result_file_name': result_file_name  # 结果文件名称
}