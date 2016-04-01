# CSDN-blog-classify
CSDN博客智能分类系统

CSDN博客分类系统是基于Python和朴素贝叶斯分类算法进行博客分类推荐的智能识别系统。

web页面展示和服务器都是基于 python django框架。

1：本机环境          

 python 2.7                                                                                                                 
 django 1.8  //Web框架                                                                                                      
 beautifulsoup  //爬虫库，用于解析网页标签                                                                                 

 jieba         // 分词模块                                                                                                  

 本项目是建立一个django工程，然后在它的模块中进行爬取，分词和分类
                                                                                                                           2：目录说明                                                                                                                
                                                                                                                   ——csdn_blog_classify              //工程主目录
                                                                                                                   
    ——blog_classify                //博客分类
    
    ——blog_fenci                   //文章进行分词
    
    ——blog_spider                  //爬取文章内容，分类别进行存储
    
    ——csdn_blog_classify           //django工程目录
    
    ——static                       //静态文件目录
    
    ——templates                    //模板目录
    
    ——db.sqlite3                   //django自带的轻量级数据库
    
    ——manage.py                    //测试启动服务等

    django系列教程请参考：
    http://blog.csdn.net/Gamer_gyt/article/category/5996523

    python爬虫相关教程请查看：
    http://blog.csdn.net/Gamer_gyt/article/category/2949495

    python相关博客请参考：
    http://blog.csdn.net/Gamer_gyt/article/category/2816997


3:具体效果图在此不能展示了，不过有兴趣的可以联系小编，大家一起交流进步

Thinkgamer，CyanScikit科技创始人，热爱大数据家族，机器学习算法，和无所不能的python

QQ：1923361654

wechat：gyt13342445911
