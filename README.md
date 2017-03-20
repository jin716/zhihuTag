# zhihuTag

#### 技术工具：Python/BeautifulSoup/Redis/Mysql/RestAPI

#### 技术实现：通过Redis中央队列的形式，对知乎的标签页进行广度优先遍历，通过FIFO，实现分布式爬虫,并协同抓取全知乎的标签及子标签的树状结构，将此全量树状结构存储入MySQL数据库。此机制保证任何一个爬虫技能单独而协同。
