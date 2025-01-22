from django.urls import path
from .views import SignupView
# LoginView
# , SpamMarkerView, FindByNameView, FindByNumberView,CustomTokenObtainPairView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    # path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    # path('report-spam/', SpamMarkerView.as_view(), name='spam-marker'),
    # path('find-by-name/', FindByNameView.as_view(), name='find-by-name'),
    # path('find-by-number/', FindByNumberView.as_view(), name='find-by-number'),
]
