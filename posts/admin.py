from django.contrib import admin
from posts.models import ExchangePost,ExchangePostImage,Offers,ExchangePostDeliveryInfo

# Register your models here.
admin.site.register(ExchangePost)
admin.site.register(ExchangePostImage)
admin.site.register(ExchangePostDeliveryInfo)
admin.site.register(Offers)
