#coding:utf-8

class Topic:

    id = ''
    name = ''
    parent = ''
    child = []

    def __init__(self, id, name,parent):
        self.name = name
        self.id = id
        self.parent = parent

    def setParent(self,pid):
        self.parent = pid

    def getParent(self):
        return self.parent

    def addChild(self,cid):
        self.child += cid

    def removeChild(self,cid):
        self.child.remove(cid)

    def data(self):
        return {'id':str(self.id),'name':self.name,'parent_id':self.parent}

