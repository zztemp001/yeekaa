任务
=========

1、scrapy
2、分解任务
2、文档书写工具及环境
3、widget库结构
4、晚上到家：虾米网下载音乐（邓丽君、龙飘飘、革命歌曲、徐小凤、小娟、蔡琴、影视主题曲、降央卓玛、粤剧等）
5、晚上到家：找到我的notebook文件，并入github

处理静态文件的步骤（使用开发服务器时）：
1、django缺省会在项目根目录，以及每个app的static目录下找静态文件
2、settings.py - 在INSTALLED_APPS中加入django.contrib.staticfiles
3、urls.py -
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
4、模板中可以使用绝对路径来引用静态文件，或通过{{ STATIC_URL }}，后者需要确保在views中使用了RequestContext

# 打开git shell的颜色高亮
git config --global color.ui "auto"

# 打开git的图形界面（自带的）
git gui

打开scrapy相关网页
打开asana、gantter
打开github issue list
下载rst中文参考文档（最好是离线的html版）
搜索pycharm的rst文件支持（预览）

