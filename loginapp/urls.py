from django.urls import path
from .views import login_create_view, login_list_view, login_detail_view, login_update_view, login_delete_view

urlpatterns = [
    path('api/login/', login_list_view, name='login_list'),  # List all login entries
    path('api/login/create/', login_create_view, name='login_create'),  # Create a new login entry
    path('api/login/<int:pk>/', login_detail_view, name='login_detail'),  # Retrieve a specific entry
    path('api/login/<int:pk>/update/', login_update_view, name='login_update'),  # Update a specific entry
    path('api/login/<int:pk>/delete/', login_delete_view, name='login_delete'), 
]
