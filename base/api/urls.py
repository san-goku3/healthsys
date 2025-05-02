from django.urls import path
from . import views

#from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns=[
    path('auth/register/', views.register_user, name='register'),
    path('protected/', views.protected_view, name='protected'),
    path('auth/login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('patients/',views.all_patients),
    path('patients/<int:pk>',views.one_patient),

    path('doctors/',views.all_doctors),
    path('doctors/<int:pk>',views.one_doctor),

    path('maps/',views.all_mapping),
    path('maps/<int:pk>',views.one_map),
]

'''
from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('',views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
'''