from django.urls import path, re_path
from .views import index, error, login

urlpatterns = [
    path('error/', error, name="error"),
    # path('user/<str:login>/<str:directory_name>/<int:directory_number>', login, name='login'),
    # path('user/<str:login>/<str:directory_name>', login, name='login'),
    # path('user/<str:login>', login, name='login'),
    # path('user/', login, name='login'),
    re_path(r'^user/(?P<login>\w+)/(?P<directory_name>\w+)/(?P<directory_number>\d+)/$', login, name='login'),
    re_path(r'^user/(?P<login>\w+)/(?P<directory_name>\w+)/$', login, name='login'),
    re_path(r'^user/(?P<login>\w+)/$', login, name='login'),
    re_path(r'^user/$', login, name='login'),


    # re_path(r'^user/(?P<name>\D+)', index, name='strokabeznumbers'),
    #path('user/<str:name>/<int:age>', index, name="home"),
    #path('user/<str:name>', index, name="home"),
    path('', index, name="home"),

]
