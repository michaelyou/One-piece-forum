#encoding=utf-8
from django.conf.urls import patterns, include, url
from forum.forms.user import LoginForm

from views import common, user, topic, notification
from forum.sitemap import TopicSitemap

from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()



urlpatterns = [
    #URLconfs have a hook that lets you pass extra arguments to your view functions, as a Python dictionary.
    #The django.conf.urls.url() function can take an optional third argument which should be a dictionary
    #of extra keyword arguments to pass to the view function.


    url(r'^$', common.method_splitter, {'GET': topic.get_index}),  #网站根目录
    url(r'^pictures/$', common.method_splitter, {'GET': user.get_picture}),
    url(r'^t/(\d+)/$', common.method_splitter, {'GET': topic.get_topic_view, 'POST': topic.post_topic_view}),
    url(r'^t/create/(.*)/$', common.method_splitter, {'GET': topic.get_topic_create, 'POST': topic.post_topic_create}),
    url(r'^t/edit/(\d+)/$', common.method_splitter, {'GET': topic.get_topic_edit, 'POST': topic.post_topic_edit}),
    url(r'^t/delete/(\d+)/$', common.method_splitter, {'GET': topic.get_topic_delete}),
    url(r'^reply/edit/(\d+)/$', common.method_splitter, {'GET': topic.get_reply_edit, 'POST': topic.post_reply_edit}),
    url(r'^reply/delete/(\d+)/$', common.method_splitter, {'GET': topic.get_reply_delete}),
    url(r'^node/(.*)/$', common.method_splitter, {'GET': topic.get_node_topics}),
    url(r'^u/(.*)/topics/$', common.method_splitter, {'GET': topic.get_user_topics}),
    url(r'^u/(.*)/replies/$', common.method_splitter, {'GET': topic.get_user_replies}),
    url(r'^u/(.*)/favorites/$', common.method_splitter, {'GET': topic.get_user_favorites}),
    url(r'^u/(.*)/$', common.method_splitter, {'GET': topic.get_profile}),
    url(r'^vote/$', common.method_splitter, {'GET': topic.get_vote}),
    url(r'^favorite/$', common.method_splitter, {'GET': topic.get_favorite}),
    url(r'^unfavorite/$', common.method_splitter, {'GET': topic.get_cancel_favorite}),
    url(r'^notifications/$', common.method_splitter, {'GET': notification.get_list}),
    url(r'^members/$', common.method_splitter, {'GET': topic.get_members}),
    url(r'^setting/$', common.method_splitter, {'GET': user.get_setting, 'POST': user.post_setting}),
    url(r'^setting/avatar/$', common.method_splitter, {'GET': user.get_setting_avatar, 'POST': user.post_setting_avatar}),
    url(r'^setting/password/$', common.method_splitter, {'GET': user.get_settingpwd, 'POST': user.post_settingpwd}),
    url(r'^forgot/$', common.method_splitter, {'GET': user.get_forgotpwd, 'POST': user.post_forgotpwd}),
    url(r'^login/$', common.method_splitter, {'GET': user.get_login, 'POST': user.post_login}),
    url(r'^logout/$', common.method_splitter, {'GET': user.get_logout}),
    url(r'^register/$', common.method_splitter, {'GET': user.get_register, 'POST': user.post_register}),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'topics': TopicSitemap}}),
]
