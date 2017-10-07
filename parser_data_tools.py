#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'zhaotingting'
__Date__ = '20170929'

import json
import urllib2
from bs4 import BeautifulSoup
import sys
import logging
import time
reload(sys)
sys.setdefaultencoding('utf-8')

job_detial_url = 'https://www.lagou.com/jobs/'
job_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'user_trace_token=20170809103105-6ffbc76652a64c6198c361655b555b8e; LGUID=20170809103106-cbcc025a-7caa-11e7-844e-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=4ec2b1b2ce2a48a694878670179dacbf; fromsite="localhost:63342"; _gid=GA1.2.317337945.1506474803; JSESSIONID=ABAAABAACEBACDG8C98BBE01C8EEF4BB9D40E3C5C48695C; X_HTTP_TOKEN=8e8cdc5c6502c49728580058eb869a65; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1506483187,1506499960,1506500769,1506514774; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1506517229; _ga=GA1.2.302982284.1502245749; _gat=1; LGSID=20170927201937-20db6bf9-a37e-11e7-afa5-525400f775ce; LGRID=20170927210031-d7b224d9-a383-11e7-9300-5254005c3644',
    'Host':'www.lagou.com',
    'Pragma':'no-cache',
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}

logging.basicConfig(level=logging.DEBUG,
                    filename='log.txt',
                    filemode='a',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def get_position_description(positionId):
    """
        获取职位的详细描述
    :param positionId: 职位对应的id值
    :return:
    """
    # 根据positionId获取职位详细描述
    position_html_data = ''
    descriptions = ''
    url = job_detial_url + str(positionId) + '.html'
    try:
        req = urllib2.Request(url, headers=job_headers)
        response = urllib2.urlopen(req)
        position_html_data = response.read().decode('utf-8')
    except Exception, e:
        logging.error(str(e) + '------' +url)
    if position_html_data:
        soup = BeautifulSoup(position_html_data, 'lxml')
        job_description = soup.find('dd', {'class': 'job_bt'})
        if job_description:
            description_results = job_description.findAll('p')
            for result in description_results:
                if result.string:
                    descriptions += str(result.string) + '\t'
    return descriptions


def parse_result_data(raw_data, result_file_name):
    """
        解析拉钩网站获取的职位信息
    :param raw_data: 获取的拉钩网的原始json数据
    :return:
    """
    results_num = 0
    result_file = open(result_file_name, 'a')
    data = ''
    try:
        data = json.loads(raw_data)
    except Exception, e:
        logging.error(str(e))

    if 'content' in data:
        content = data['content']
        if 'positionResult' in content:
            positionResult = content['positionResult']
            if positionResult:
                if 'result' in positionResult:
                    results = positionResult['result']
                    for result in results:
                        file_result_data = ''
                        positionId = (result['positionId'] if 'positionId' in result else '')
                        job_description = get_position_description(positionId)
                        results_num += 1
                        if 'district' in result and result['district']:
                            district = result['district']
                        else:
                            district = ''
                        if 'companyLabelList' in result and result['companyLabelList']:
                            companyLabelList = ",".join(result['companyLabelList'])
                        else:
                            companyLabelList = ''
                        if 'positionLables' in result and result['positionLables']:
                            positionLables = ",".join(result['positionLables'])
                        else:
                            positionLables = ''
                        if 'industryLables' in result and result['industryLables']:
                            industryLables = "".join(result['industryLables'])
                        else:
                            industryLables = ''
                        if 'businessZones' in result and result['businessZones']:
                            businessZones = "".join(result['businessZones'])
                        else:
                            businessZones = ''
                        if 'companyFullName' in result and result['companyFullName']:
                            companyFullName = result['companyFullName']
                        else:
                            companyFullName = ''
                        if 'financeStage' in result and result['financeStage']:
                            financeStage = result['financeStage']
                        else:
                            financeStage = ''
                        if 'companyShortName' in result and result['companyShortName']:
                            companyShortName = result['companyShortName']
                        else:
                            companyShortName = ''
                        if 'createTime' in result and result['createTime']:
                            createTime = result['createTime']
                        else:
                            createTime = ''
                        if 'positionName' in result and result['positionName']:
                            positionName = result['positionName']
                        else:
                            positionName = ''
                        if 'education' in result and result['education']:
                            education = result['education']
                        else:
                            education = ''
                        if 'city' in result and result['city']:
                            city = result['city']
                        else:
                            city = ''
                        if 'salary' in result and result['salary']:
                            salary = result['salary']
                        else:
                            salary = ''
                        if 'industryField' in result and result['industryField']:
                            industryField = result['industryField']
                        else:
                            industryField = ''
                        if 'positionAdvantage' in result and result['positionAdvantage']:
                            positionAdvantage = result['positionAdvantage']
                        else:
                            positionAdvantage = ''
                        if 'jobNature' in result and result['jobNature']:
                            jobNature = result['jobNature']
                        else:
                            jobNature = ''
                        if 'workYear' in result and result['workYear']:
                            workYear = result['workYear']
                        else:
                            workYear = ''
                        if 'companySize' in result and result['companySize']:
                            companySize = result['companySize']
                        else:
                            companySize = ''
                        if 'firstType' in result and result['firstType']:
                            firstType = result['firstType']
                        else:
                            firstType = ''
                        try:
                            file_result_data = (financeStage + '@' + companyShortName + '@' + createTime + '@'
                                                + positionName + '@'+ education + '@'+ city + '@'
                                                + salary + '@'+ industryField + '@'+ district + '@'
                                                + positionAdvantage + companyLabelList + '@'+ jobNature + '@'
                                                + workYear + '@'+ positionLables + '@'+ industryLables + '@'
                                                + companySize + '@'+ businessZones + '@'+ firstType + '@'
                                                + companyFullName + '@' + str(job_description))
                        except Exception, e:
                            logging.error(str(result))
                        print job_description
                        print file_result_data
                        result_file.write(file_result_data)
                        result_file.write('\n')
                        time.sleep(5)
    result_file.close()
    return results_num


