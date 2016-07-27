# myblog
Django框架实现的一个博客系统
# 软件版本
python： 2.7
Django: 1.6
# 其他
- 使用markdown来进行格式控制(服务器需要安装markdown)
- 实现了代码高亮
# 注意
在使用的时候需要删除数据库sqlite3.db， 然后运行下面的代码，重新生成数据库
```
//linux下
python manage.py syncdb
//windows下
manage.py syncdb
```
