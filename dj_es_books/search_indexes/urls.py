from django.conf.urls import url, include
from rest_framework_extensions.routers import ExtendedDefaultRouter

from .viewsets.book import BookDocumentView


router = ExtendedDefaultRouter()
books = router.register(r'books',
                        BookDocumentView,
                        basename='bookdocument')

urlpatterns = [
    url(r'^', include(router.urls)),
]
