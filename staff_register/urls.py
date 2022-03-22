from django.urls import path,include
from . import views


#views.index()
urlpatterns = [
    path('',views.staff_form ,name='staff_insert'),
    path('<int:id>/',views.staff_form,name='staff_update'),
    path('delete/<int:id>/', views.staff_delete, name='staff_delete'),
    path('list/',views.staff_list, name='staff_list')
]
 