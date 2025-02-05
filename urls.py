from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.demoindex,name="demoindex"),
    path('index/',views.index,name="index"),
    path('personal/',views.personal,name="personal"),
    path('detail/<int:id>/',views.detail,name="detail"),
    path('admins/',views.admin,name="admin"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('bride/',views.bride,name="bride"),
    path('groom/',views.groom,name="groom"),
    path('filter/',views.filter,name="filter"),
    path('message/',views.message,name="message"),

    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('event/',views.event,name="event"),
    path('gallery/',views.gallery,name="gallery"),
    path('list_detail/<int:id>/',views.list_detail,name="list_detail"),
    path('list/',views.list,name="list"),
    path('list1/',views.list1,name="list1"),
    path('search/',views.search,name="search"),
    path('team/',views.team,name="team"),
    path('login/',views.login,name="login"),
    path('reg/',views.reg,name="reg"),
    path('logout/',views.logout_user,name="logout"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
