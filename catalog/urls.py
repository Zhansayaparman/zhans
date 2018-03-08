from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('kafedra/<int:pk>', views.KafedraDetailView.as_view(), name='kafedra-detail'),

	path('students/', views.StudentListView.as_view(), name='students'),
	path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('prepods/', views.PrepodListView.as_view(), name='prepods'),
	path('prepod/<int:pk>', views.PrepodDetailView.as_view(), name='prepod-detail'),
]
