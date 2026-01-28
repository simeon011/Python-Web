from django.urls import path, include

from reviews.views import recent_reviews_list, review_detail, create_review, update_review, delete_review

app_name = 'reviews'
urlpatterns = [
    path('', include([
        path('recent/', recent_reviews_list, name='recent'),
        path('create/', create_review, name='create'),
        path('<int:pk>/update/', update_review, name='update'),
        path('<int:pk>/delete/', delete_review, name='delete'),
        path('<int:pk>', review_detail, name='details'),

    ]))

]