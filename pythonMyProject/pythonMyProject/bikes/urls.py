from django.urls import path
from django.views.generic import TemplateView

from pythonMyProject.bikes.views.cart import cart, checkout, update_item
from pythonMyProject.bikes.views.generic import DashboardView
from pythonMyProject.bikes.views.bike import CreateBikeView, SellBikeView, EditBikeView, DeleteBikeView, \
    EditSellBikeView, DeleteSellBikeView

urlpatterns = (
    path('bike/create/', CreateBikeView.as_view(), name='create bike'),
    path('bike/edit/<int:pk>/', EditBikeView.as_view(), name='edit bike'),
    path('bike/delete/<int:pk>/', DeleteBikeView.as_view(), name='delete bike'),

    path('for_sale/', SellBikeView.as_view(), name='sell bike'),
    path('sell_bike_edit/<int:pk>/', EditSellBikeView.as_view(), name='edit sell bike'),
    path('sell_bike_delete/<int:pk>', DeleteSellBikeView.as_view(), name='delete sell bike'),


    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_item, name='update item')


)
