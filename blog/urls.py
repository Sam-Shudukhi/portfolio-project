from django.urls import path
from . import views
urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]

"""
<int:blog_id>
means look for an integer after the blog segment and view
the corresponding details to that blog post.
blog_id gets passed as a parameter in the detail method in views.
"""
