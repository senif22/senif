from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/',views.index),
    path('viewdata/',views.view_data),
    path('stordata/',views.stor_data,name="stordata"),
    path('showdata/',views.showdata),
    path('update/<rollno>',views.updaterecord),
    path('editdata/<rollno>',views.editdata),
    path('deletedata/<rollno>',views.delete_data),
    


]
