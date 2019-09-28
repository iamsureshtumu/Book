from django.urls import path
from ebook import views
app_name='ebook'
urlpatterns=[
    path('p1',views.page1,name="go to page1"),
    path('p2',views.index,name="go to index"),
    path('p3',views.coverpage,name="go to coverpage"),
]