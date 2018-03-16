# -*- coding: utf-8 -*-
from constant import  SearchArticleType, SearchArticleTime

from request import SogouRequest
from exceptions import SogouCrawlerRequestsException, SogouCrawlerVerificationCodeException

import requests
import time

cache = dict()

class SogouAPI:


    def __init__(self,retries=5):
        self.retries = retries


    def fetch_official_account_info(self,keyword):
        url = SogouRequest.generate_search_official_account_url(keyword)
        response =


    def __get_and_unlock(self, url, unlock_function, identify_image_callback):
        session = requests.session()
        response = self._get(session, url)

        if 'antispider' in response.url or u'请输入验证码' in response.text:
            unlock_function(session, response, url, identify_image_callback)
            response = self._get(session, url)

        return response


    def _get(self, session, url):
        response = session.get(url)
        retries=0

        while not response.ok or retries < self.retries:
            response = session.get(url)
            retries += 1
        if not response.ok:
            raise SogouCrawlerRequestsException('Get error', response)

        return response

    def unlock_sogou(self, url, session, resp, identify_image_callback=None):
        millis = int(round(time.time() * 1000))
        r_captcha = session.get('http://weixin.sogou.com/antispider/util/seccode.php?tc={}'.format(millis))

        if not r_captcha.ok:
            raise SogouCrawlerRequestsException('SogouAPI get verfication code faild:',resp)

        r_unlock = self.unlock_sogou_callback(url, session, resp, r_captcha.content, identify_image_callback)

        if r_unlock['code'] != 0:
            raise SogouCrawlerVerificationCodeException(
                '[SogouAPI identify image] code: %s, msg: %s, cookie_count: %s' % (
                    r_unlock.get('ret'), r_unlock.get('errmsg'), r_unlock.get('cookie_count')))

    def unlock_sogou_callback(self, url, seesion, req, resp, img, identify_image_callback):

        url_quote = url.split('weixin.sogou.com/')[-1]

        unlock_url = 'http://weixin.sogou.com/antispider/thank.php'
        data = {
            'c': identify_image_callback(img),
            'r': '%2F' + url_quote,
            'v': 5
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://weixin.sogou.com/antispider/?from=%2f' + url_quote
        }
        r_unlock = req.post(unlock_url, data, headers=headers)
        if not r_unlock.ok:
            raise SogouCrawlerVerificationCodeException(
                'url: %s unlock[%s] failed: %s' % (unlock_url, r_unlock.text, r_unlock.status_code))

        return r_unlock.json()
