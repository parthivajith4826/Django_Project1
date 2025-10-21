from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.book_list,name = 'book_list'),
    path('list/<int:book_id>/',views.book_detail,name = 'book_detail'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',views.login,name = 'login'),
    path('list_login/',views.book_list_login,name = 'book_list_login'),





    path('list_admin_login/',views.book_list_admin_login,name = 'admin_login'),
    path('add/',views.book_create,name = 'create'),
    path('update_s/',views.book_update_s,name = 'update_s'),
    path('update_f/<int:id>',views.book_update_f,name = 'update_f'),
    path('remove_s/',views.book_remove_s,name = 'remove_s'),
    path('remove_f/<int:id>',views.book_remove_f,name = 'remove_f'),
]
