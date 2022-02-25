from django.urls import path
from . import views

app_name='blog'

urlpatterns=[
    path('index/',views.index,name='index'),
    path('',views.PostListView.as_view(),name='postlist'),
    path('postdetail/<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail,name='postdetail'),


]
