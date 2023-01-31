from django.contrib import admin
from django.urls import path
from new import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home' ),
    path('feedback', views.feedback, name = 'feedback' ),
    path('solution', views.solution, name = 'solution' ),
    path('literature_survey', views.literature, name = 'literature_survey' ),
    path('inside_ewm', views.inside, name = 'inside_ewm' ),
    path('health_impact', views.health, name = 'health_impact' ),
    path('about', views.about, name = 'about' ),
    path('index', views.index, name = 'home' ),
    path('care', views.care, name = 'care' )
]
