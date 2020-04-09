import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search_indexes.documents.book import BookDocument


class BookDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = BookDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'title',
            'description',
            'summary',
            'publisher',
            'publication_date',
            'state',
            'isbn',
            'price',
            'pages',
            'stock_count',
            'tags',
        )

# Make serialisers read only
#
# class BookDocumentSerializer(serializers.Serializer):
#     """Serializer for the Book document."""
#
#     id = serializers.IntegerField(read_only=True)
#
#     title = serializers.CharField(read_only=True)
#     description = serializers.CharField(read_only=True)
#     summary = serializers.CharField(read_only=True)
#
#     publisher = serializers.CharField(read_only=True)
#     publication_date = serializers.DateField(read_only=True)
#     state = serializers.CharField(read_only=True)
#     isbn = serializers.CharField(read_only=True)
#     price = serializers.FloatField(read_only=True)
#     pages = serializers.IntegerField(read_only=True)
#     stock_count = serializers.IntegerField(read_only=True)
#     tags = serializers.SerializerMethodField()
#
#     class Meta(object):
#         """Meta options."""
#
#         # List the serializer fields. Note, that the order of the fields
#         # is preserved in the ViewSet.
#         fields = (
#             'id',
#             'title',
#             'description',
#             'summary',
#             'publisher',
#             'publication_date',
#             'state',
#             'isbn',
#             'price',
#             'pages',
#             'stock_count',
#             'tags',
#         )
#
#     def get_tags(self, obj):
#         """Get tags."""
#         if obj.tags:
#             return list(obj.tags)
#         else:
#             return []
