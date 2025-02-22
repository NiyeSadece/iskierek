"""
URL configuration for iskierek project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iskierek_site.views import GetUser, UpdateExp, SubExp, UpdateLvl, RankingAPI, UserActive, UserInactive, Ranking, GetStudent, GetProfessor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ranking/', Ranking.as_view(), name='ranking'),
    path('api/<int:discord_id>/', GetUser.as_view(), name='user'),
    path('api/exp/update/', UpdateExp.as_view(), name='exp_update'),
    path('api/exp/sub/', SubExp.as_view(), name='exp_sub'),
    path('api/lvl/update/', UpdateLvl.as_view(), name='lvl_update'),
    path('api/ranking/', RankingAPI.as_view(), name='ranking_api'),
    path('api/user/active/', UserActive.as_view(), name='active_user'),
    path('api/user/inactive/', UserInactive.as_view(), name='inactive_user'),
    path('api/s/<str:name>/', GetStudent.as_view(), name='student'),
    path('api/p/<str:name>/', GetProfessor.as_view(), name='professor'),
]
