from django.urls import path
from . import regions_views, vm_pp_views, vm_tier_views, vm_sku_views


urlpatterns = [
    path('regions/', regions_views.RegionView.as_view()) ,
    path('regions/<str:region>', regions_views.RegionDetailView.as_view()) ,
    path('pricing_plans/', vm_pp_views.VmPricingPlans.as_view()),
    path('vm_tiers/', vm_tier_views.virtual_machine_tier.as_view()),
    path('vm_skus/',vm_sku_views.VmSkuView.as_view()),
    path('vm_skus/<str:sku>/<str:location>', vm_sku_views.VmSkuDetailView.as_view())
]
