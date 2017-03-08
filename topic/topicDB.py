from topic import Topic
from db import *

class TopicDB:

    config ={
        'host':'127.0.0.1',#120.24.63.70
        'user':'jin',
        'passwd':'123qwe',
        'db':'zh',
        'port':3306
    }

    def __init__(self,config):
        self.database = db(config)


    def insertTopic(self,topic):
        sql_ = "insert into topic (id, name, parent_id, updata_time ) values (%(id)s, %(name)s, %(parent_id)s , now())"
        self.database.excute(sql_, topic.data())

    def updataTopic(self,topic):
        sql_ = "update topic set name = %(name)s, parent_id = %(parent_id)s , updata_time = now() where id = %(id)s"
        self.database.excute(sql_, topic.data())

    def queryTopicById(self,id):
        sql_ = 'select id,name,parent_id from topic where ( id = %s ) LIMIT 1'
        row = self.database.queryOne(sql_,(id,))
        if row == None:
            return None
        return Topic(row[0],row[1],row[2])

    def saveTopic(self,topic):
        t2 = self.queryTopicById(topic.id)
        if t2 == None:
            self.insertTopic(topic)
        self.updataTopic(topic)

    def insetHtml(self,url , txt):
        sql_ = "insert into page (url, text, time ) values (%s,%s,now())"
        self.database.excute(sql_, (url,txt))

