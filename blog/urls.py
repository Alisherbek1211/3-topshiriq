from django.urls import path
from .views import CommentView, PostDateView,PostDateView,PostRecommendedView,PostDetailView,PostReadNextView,PostPopularView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'postdate/', PostDateView,basename="Post Date")
router.register(r'popular/', PostPopularView,basename="Popular")
router.register(r'recommended/', PostRecommendedView,basename="Recommended")
router.register(r'post/', PostDetailView,basename="post detail")
router.register(r'next/', PostReadNextView,basename="Next Posts")
router.register(r'comment/', CommentView,basename="Commnent")

urlpatterns = router.urls