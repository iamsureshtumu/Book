from django.urls import path
from ebook import views
app_name='ebook'
urlpatterns=[
    path('p1',views.page,name="go to page"),
    path('p2',views.index,name="go to index"),
    path('p3',views.coverpage,name="go to coverpage"),
    path('page3/',views.page3,name="page3"),
]