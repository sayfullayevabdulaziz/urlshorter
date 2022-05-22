from django.urls import path
from .views import indexView, shortToOriginal, urlcounter, terms_service,privacy_policy, report, contact_view
urlpatterns = [
    path('',indexView),
    path('url-click-counter',urlcounter),
    path('terms-of-service', terms_service),
    path('report-malicious-url',report),
    path('contact', contact_view),
    path('privacy-policy', privacy_policy),
    path('<str:slug>',shortToOriginal),
]
