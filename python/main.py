#coding:utf-8

import random
import time

import demjson
import redis

from helper import config
from http import *
from topic.topic import Topic
from topic.topicDB import TopicDB
from topic.topicHtml import TopicHtml


def wideTrasvel(rootTopic,db,cache):
    http = Http()
    topic = rootTopic
    while topic != None and topic.id != '':
        basePage = http.getHtml(TopicHtml.childsUrl(rootTopic.id))
        topics = TopicHtml.childTopicsFormChildsUrlPage(basePage.text, rootTopic)
        db.insetHtml(TopicHtml.childsUrl(rootTopic.id),basePage.text)
        visic(topic)
        for t in topics:
            cache.lpush('topic_queue',t.data());
        topic = cache.rpop('topic_queque')

def getTopicFromJason(s):
    d = demjson.decode(s)
    return Topic(d['id'], d['name'], d['parent_id'])

def sleep():
    t = random.uniform(0.5, 3)
    time.sleep(t)

def visic(topic):
    sleep()
    db.saveTopic(topic)


cache = redis.Redis(host=config.get("redis", "host"),
                    port=config.get("redis", "port"), db=0,
                    password=config.get("redis", "password"))
db = TopicDB(TopicDB.config)
rootTopicJson =cache.rpop('topic_queue')
if rootTopicJson == None:
    rtId = '19776749' #root
    rootTopic =  db.queryTopicById(rtId)
else :
    rootTopic = getTopicFromJason(rootTopicJson)
wideTrasvel(rootTopic,db,cache)




