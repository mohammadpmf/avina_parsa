from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.show_weblogs_homepage, name='home'),
    path('detail/<int:pk>/', views.show_weblogs_detail, name='detail'),
    path('new_post/', views.new_post, name='new_post'),
    path('about_us/', views.about_us, name='about_us'),
]
