from django.conf import settings
from django_elasticsearch_dsl import DocType as Document, Index, fields
from elasticsearch_dsl import analyzer

from books.models import Book

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

# custom analyser
html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@INDEX.doc_type
class BookDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    title = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', fielddata=True),
        }
    )

    description = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword',fielddata=True),
        }
    )

    summary = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword',fielddata=True),
        }
    )

    publisher = fields.TextField(
        attr='publisher_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword',fielddata=True),
        }
    )

    publication_date = fields.DateField()

    state = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword',fielddata=True),
        }
    )

    isbn = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', fielddata=True),
        },fielddata=True
    )

    price = fields.FloatField(
        fields={
            'raw': fields.FloatField(),
        }
    )

    pages = fields.IntegerField()

    stock_count = fields.IntegerField()

    tags = fields.TextField(
        attr='tags_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', multi=True),
            'suggest': fields.CompletionField(multi=True),
        },fielddata=True,
        multi=True
    )

    class Meta(object):
        """Inner nested class Django."""

        model = Book  # The model associate with this Document