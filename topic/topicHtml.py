#coding:utf-8

from topic import Topic
from bs4 import BeautifulSoup

class TopicHtml:

    URL_BASE = 'https://www.zhihu.com/topic/'
    TOP_ANSBER = '/top-answers'
    CHILD_LIST = '/organize/entire'
    PAGE = '?page='

    @staticmethod
    def baseUrl(id, page):
        url = TopicHtml.URL_BASE + str(id) + TopicHtml.TOP_ANSBER
        if (page > 1):
            url = url + TopicHtml.PAGE + str(page)
        return url

    @staticmethod
    def childsUrl(id):
        return TopicHtml.URL_BASE + str(id) + TopicHtml.CHILD_LIST

    # form topic page
    @staticmethod
    def parentTopicFromBaseUrlPage(html):
        soup = BeautifulSoup(html, "html.parser")
        i = soup.find("a", {"class", "zm-item-tag"})
        t = Topic(unicode(i.attrs['data-token']), unicode(i.string).strip(),'0')
        return t

    @staticmethod
    def childTopicsFormChildsUrlPage(html,currentTopic):
        topics = []
        soup = BeautifulSoup(html, "html.parser")
        all = soup.find_all("a", {"class", "zm-item-tag"})
        for i in all:
            t = Topic(unicode(i.attrs['data-token']), unicode(i.string).strip(),currentTopic.id)
            if(currentTopic.id != t.id):
                topics.append(t)
        return topics








