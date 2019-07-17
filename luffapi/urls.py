from django.conf.urls import url,include
from luffapi.views import course
from luffapi.views import account
from luffapi.views import teacher
from luffapi.views import techno
from luffapi.views import shopping_car

urlpatterns=[
    url(r'course/$',course.CourseView.as_view({'get':'list',"post":'post'})),
    url(r'course/(?P<pk>\d+)/$',course.CourseView.as_view({'get':'retrieve','post':'addchapter'})),
    url(r'auth/$',account.AuthView.as_view()),
    url(r'techno/(?P<pk>\d+)/$',techno.TechnoDetailView.as_view({'post':'post'})),
    url(r'techno/$',techno.TechnoView.as_view()),
    url(r'teacher/$',teacher.TeacherView.as_view({'get': 'list',})),
    url(r'shoppingcar/$',shopping_car.ShoppingCarView.as_view({'post': 'post','delete':'delete'})),
]