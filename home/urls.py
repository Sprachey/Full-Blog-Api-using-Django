from django.urls import path,include
from .views import BlogView, PublicBlogView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts',PublicBlogView)

urlpatterns = [
    path('',include(router.urls)),
    path('blog/',BlogView.as_view()),
    # path('post/',PublicView.as_view())


]