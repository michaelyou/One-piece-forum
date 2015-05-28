# coding: utf-8

#就是试一下怎么用processor，直接写到html里也是可以的
def custom_proc(request):
    return dict(
        navigation_bar = [
            ('/', 'topic', '社区'),
            ('/members/', 'members', '成员'),
            ('/pictures/', 'picture', '照片墙'),
            ('/static/pages/timeline/index.html', 'timeline', '大事记'),
        ],
    )
