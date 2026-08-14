from django.contrib import admin
from django.urls import path
from predictor import views   # <-- import your app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.predict_price, name='predict_price'),  # homepage → form + prediction
]
