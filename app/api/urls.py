from django.urls import path
from . import views
from .views import MyTokenObtainPairView




from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('notes',views.getNotes),

    path('createuser',views.createUser),
    path('userlist',views.CurrentUserViewSet.as_view({'get': 'list'}), name='user_list'),


]