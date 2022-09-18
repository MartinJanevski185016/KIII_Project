from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('artstyle/', views.artstyle, name="artstyle"),
    path('bestsculpt/', views.bestsculpt, name="bestsculpt"),
    path('blendersculpting/', views.blendersculpting, name="blendersculpting"),
    path('buyatablet/', views.buyatablet, name="buyatablet"),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('digitalpainting/', views.digitalpainting, name="digitalpainting"),
    path('glowinthedark/', views.glowinthedark, name="glowinthedark"),
    path('introphotoshop/', views.introphotoshop, name="introphotoshop"),
    path('photobashing/', views.photobashing, name="photobashing"),
    path('rig3dsmax/', views.rig3dsmax, name="rig3dsmax"),
    path('rigblender/', views.rigblender, name="rigblender"),
    path('squash&stretch/', views.squashandstretch, name="squash&stretch"),
    path('walk_cycles/', views.walk_cycles, name="walk_cycles"),
      path('whytmanga/', views.whytmanga, name="whytmanga"),
        path('imagebetter/', views.imagebetter, name="imagebetter")
]