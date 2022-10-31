from django.urls import path
from .views import Post_ListView, Post_DetailView
app_name = 'core'

urlpatterns = [
    path('', Post_ListView.as_view(), name = 'list-view'),
    path('<int:pk>/<int:year>/<int:month>/<int:day>/<slug:slug>/', Post_DetailView, name = 'detail')
    #path('', listview, name ='list-view')
]