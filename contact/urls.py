from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('',views.index,name='index'),
    
    path('BSc_admission_Form/',views.BSc_admission_Form,name='BSc_admission_Form'),
    path('download_confirmation/',views.download_confirmation,name='download_confirmation'),
    path('tabledata/',views.tabledata,name='tabledata'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('results/', views.results_view, name='results'),

    path('ug_course_details/<str:course_name>/', views.ug_course_details, name='ug_course_details'),
    path('time_table/', views.time_table, name='time_table'),
    path('UG_Study/', views.UG_Studys, name='UG_Study'),
    path('contact/', views.contact, name='contact'),
    path('about2/', views.about2, name='about2'),
    path('notification_view/', views.notification_view, name='notification_view'),
    path('gallery_view/', views.gallery_view, name='gallery_view'),
    path('working/', views.working, name='working'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)