from django.conf.urls import url
from django.urls import path

from skill.views import inside_view
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        path('/', views.index, name ="index"),
        path('contact/', views.contact, name="contact"),
        path('inside/', views.inside_view, name="inside"),
        path('service/', views.service, name="service"),
        path('blog/', views.blog_view, name="blog"),
]

