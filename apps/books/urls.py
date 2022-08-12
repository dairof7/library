# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from apps.books import views

# urlpatterns = [
#     path('authors/', views.AuthorsList.as_view()),
#     path('list/', views.BooksListView.as_view()),
#     path('book/create/', views.BooksCreateView.as_view()),
#     path('book/retrieve/<int:pk>/', views.BooksRetrieveApiView.as_view(), name='product_retrieve'),
#     path('book/delete/<int:pk>/', views.BooksDeleteApiView.as_view(), name='product_delete'),
#     path('book/update/<int:pk>/', views.BookUpdateApiView.as_view(), name='product_update'),
#     path('authors/<int:pk>/', views.AuthorDetailView.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)