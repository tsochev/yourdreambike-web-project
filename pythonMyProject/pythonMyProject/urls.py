from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from pythonMyProject.bikes.views.generic import HomeView, DashboardView, PostBikeView, BikesForSale

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('posted_bikes/', PostBikeView.as_view(), name='posted bikes'),
    path('bikes_for_sale/', BikesForSale.as_view(), name='bikes for sale'),

    path('accounts/', include('pythonMyProject.accounts.urls')),
    path('bikes/', include('pythonMyProject.bikes.urls')),


    path('404_error/', TemplateView.as_view(template_name='403_no_permission.html'), name='404 error')

    # path('', TemplateView.as_view(template_name='base.html'), name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'pythonMyProject.common.helpers.error_404'