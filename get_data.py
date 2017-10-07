#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'zhaotingting'
__Date__ = '20170927'
import logging
import re
import sys
import urllib2
import urllib
import json
import time
from parser_data_tools import parse_result_data
import global_config as _gv
reload(sys)
sys.setdefaultencoding('utf-8')

# 设置日志模块
logging.basicConfig(level=logging.DEBUG,
                    filename='log.txt',
                    filemode='a',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def format_cn_str(cn_str):
    """
        格式化中文字符串
    :param cn_str: 传入的中文字符串
    :return:
    """
    cn_str_byte = cn_str.encode('utf-8')
    cn_str_index = str(cn_str_byte).replace(r'\x', '%').replace(r"'", "")
    cn_str_index = re.sub('^b', '', cn_str_index)
    return cn_str_index


def lagou_spider_keyword(position_key='', city_key='', district_key='', px='new', result_file_name=''):
    """
        获取拉钩的职位信息
    :param position_key: 职位关键字
    :param city: 城市关键字
    :param district: 地区关键字
    :return:
    """
    kd = format_cn_str(position_key)
    city = format_cn_str(city_key)
    district = format_cn_str(district_key)
    # 所有页面
    totalPageCount = 0
    # 当前页面
    curpage = 1

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_' + kd + '?px=' + px + '&city=' + city + '&district=' + district,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    url = ('https://www.lagou.com/jobs/positionAjax.json?px=' + px + '&city=' + city + '&district=' + district +
          '&needAddtionalResult=false&isSchoolJob=0')

    init_param = {
        'first': 'true',
        'pn': 1,
        'kd': kd
    }
    data = urllib.urlencode(init_param)
    req = urllib2.Request(url, data=data, headers=headers)
    response = urllib2.urlopen(req)
    result_data = response.read()
    # 开始分析数据
    totalPageCount = get_page_num(result_data)
    logging.debug(totalPageCount)
    # 解析数据
    results_num = parse_result_data(result_data, result_file_name)
    # 等待1秒再继续操作
    time.sleep(1)
    for i in range(2, totalPageCount):
        param = {
            'first': 'true',
            'pn': i,
            'kd': kd
        }
        data = urllib.urlencode(param)
        req = urllib2.Request(url, data=data, headers=headers)
        response = urllib2.urlopen(req)
        result_data = response.read()
        # 解析数据
        results_num += parse_result_data(result_data, result_file_name)
        time.sleep(1)
        logging.debug('完成第' + str(i) + '页的数据解析')
        logging.debug('完成第' + str(results_num) + '条的数据获取')


def get_page_num(raw_data):
    """
        返回数据总行数
    :param raw_data: 获取的数据包
    :return:
    """
    page_num = 0
    data = json.loads(raw_data)
    content = data['content']
    if 'positionResult' in content:
        positionResult = content['positionResult']
        totalCount = positionResult['totalCount']
        resultSize = positionResult['resultSize']
        if resultSize > 0:
            page_num = totalCount / resultSize + 1
    return page_num

if __name__ == '__main__':
    # 添加一个文件头
    raw_string = ('financeStage@companyShortName@createTime@positionName@education@city@salary@industryField@district@'
                  'positionAdvantage@companyLabelList@jobNature@workYear@positionLables@industryLables@companySize@'
                  'businessZones@firstType@companyFullName@jobdescription')

    result_file_name = _gv.SPIDER_PARAM['result_file_name']
    result_file = open(result_file_name, 'w')
    result_file.write(raw_string)
    result_file.write('\n')
    result_file.close()
    # 开始获取数据
    position_key = _gv.SPIDER_PARAM['position_key']
    city_key = _gv.SPIDER_PARAM['city_key']
    district_key = _gv.SPIDER_PARAM['district_key']
    # Todo 这个可以使用python **kd 参数传递
    lagou_spider_keyword(position_key=position_key, city_key=district_key, district_key=district_key,
                         result_file_name=result_file_name)
