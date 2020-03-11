from django.urls import path
from py_app import views
app_name='py_app'
urlpatterns=[
    path('html',views.html,name="html"),
    path('css',views.css,name="css"),
    path('js',views.js,name="js"),
]