import json

from django.conf import settings
from django.core.files.storage import get_storage_class
from django.http import JsonResponse
from django.views import generic
from wagtail.api.v2.filters import (
    AncestorOfFilter,
    ChildOfFilter,
    DescendantOfFilter,
    FieldsFilter,
    LocaleFilter,
    OrderingFilter,
    SearchFilter,
    TranslationOfFilter,
)
from wagtail.api.v2.views import PagesAPIViewSet

from mycarehub.common.views.base_views import BaseView
from mycarehub.utils.signed_url import generate_media_blob_name, generate_signed_upload_url

from .filters import (
    CategoryFilter,
    ContentBookmarkFilter,
    ContentItemCategoryFilter,
    ContentLikeFilter,
    ContentShareFilter,
    ContentViewFilter,
    TagFilter,
)
from .models import ContentBookmark, ContentItemCategory, ContentLike, ContentShare, ContentView
from .serializers import (
    ContentBookmarkSerializer,
    ContentItemCategorySerializer,
    ContentLikeSerializer,
    ContentShareSerializer,
    ContentViewSerializer,
)


class CustomPageAPIViewset(PagesAPIViewSet):
    # the order is important...wagtail filters come last
    filter_backends = [
        TagFilter,
        CategoryFilter,
        FieldsFilter,
        ChildOfFilter,
        AncestorOfFilter,
        DescendantOfFilter,
        OrderingFilter,
        TranslationOfFilter,
        LocaleFilter,
        SearchFilter,  # must be last
    ]
    known_query_parameters = PagesAPIViewSet.known_query_parameters.union(
        ["tag", "category", "category_name"]
    )


class SignedURLView(generic.View):
    def post(self, request, *args, **kwargs):

        # Checks the storage class being used
        # Storage class should be Google Cloud Storage for signed url generation to proceed
        if get_storage_class().__name__ != "MediaRootGoogleCloudStorage":
            return JsonResponse({"url": ""})

        data = json.loads(request.body)

        file_name = data["fileName"]
        file_type = data["fileType"]

        bucket_name = settings.GS_BUCKET_NAME

        # created in this format
        # {the media root URL}/{Upload to directory defined in file field}/{camel cased file name}
        blob_name = generate_media_blob_name(file_name)

        url = generate_signed_upload_url(
            bucket_name=bucket_name,
            blob_name=blob_name,
            content_type=file_type,
        )

        return JsonResponse({"url": url})


class ContentItemCategoryViewSet(BaseView):
    queryset = ContentItemCategory.objects.all()
    serializer_class = ContentItemCategorySerializer
    filterset_class = ContentItemCategoryFilter


class ContentViewViewSet(BaseView):
    queryset = ContentView.objects.all()
    serializer_class = ContentViewSerializer
    filterset_class = ContentViewFilter


class ContentShareViewSet(BaseView):
    queryset = ContentShare.objects.all()
    serializer_class = ContentShareSerializer
    filterset_class = ContentShareFilter


class ContentLikeViewSet(BaseView):
    queryset = ContentLike.objects.all()
    serializer_class = ContentLikeSerializer
    filterset_class = ContentLikeFilter


class ContentBookmarkViewSet(BaseView):
    queryset = ContentBookmark.objects.all()
    serializer_class = ContentBookmarkSerializer
    filterset_class = ContentBookmarkFilter