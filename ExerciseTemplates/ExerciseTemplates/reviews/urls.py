from django.urls import path, include

from reviews.views import recent_reviews_list, review_detail

app_name = 'reviews'
urlpatterns = [
    path('', include([
        path('recent/', recent_reviews_list, name='recent'),
        path('<int:pk>', review_detail, name='details'),
    ]))

]