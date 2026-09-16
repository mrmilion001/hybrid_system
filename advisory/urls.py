from django.urls import path
from advisory.views import advisory_landing_view, advisory_query_view, advisory_ui_view

urlpatterns = [
    path('', advisory_landing_view, name='advisory_landing'),
    path('advisory/', advisory_landing_view, name='advisory_landing_alt'), # handles /advisory/
    path('portal/', advisory_ui_view, name='advisory_ui'),
    path('api/query/', advisory_query_view, name='advisory_query_api'),
]