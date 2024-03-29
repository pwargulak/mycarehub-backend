import pytest
from django.urls import reverse
from rest_framework import status

from mycarehub.common.models import Facility
from mycarehub.common.serializers import FacilitySerializer
from mycarehub.common.views import DRFSerializerExcelIOMixin, HomeView
from mycarehub.utils.excel_utils import DRFSerializerExcelIO, DRFSerializerExcelIOTemplate

pytestmark = pytest.mark.django_db


def test_approved_mixin_approved_user(rf, user_with_all_permissions):
    approved_user = user_with_all_permissions
    url = "/"
    request = rf.get(url)
    request.user = approved_user
    view = HomeView()
    view.setup(request)
    view.dispatch(request)  # no error raised


def test_home_view(user_with_all_permissions, client):
    client.force_login(user_with_all_permissions)
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_about_view(user_with_all_permissions, client):
    client.force_login(user_with_all_permissions)
    url = reverse("about")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_facility_view(user_with_all_permissions, client):
    client.force_login(user_with_all_permissions)
    url = reverse("common:facilities")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_user_facility_allotment_view(user_with_all_permissions, client):
    client.force_login(user_with_all_permissions)
    url = reverse("common:user_facility_allotments")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_drf_excel_io_mixin_get_filter_form(rf, user_with_all_permissions):
    url = reverse("api:facility-dump-data")
    request = rf.get(url)
    request.user = user_with_all_permissions
    response = DRFSerializerExcelIOMixin.as_view(
        {"get": "get_filter_form"},
        excel_io_class=DRFSerializerExcelIO,
        excel_io_template_class=DRFSerializerExcelIOTemplate,
        queryset=Facility.objects.mycarehub_facilities(),
        serializer_class=FacilitySerializer,
    )(request=request)

    assert response.status_code == status.HTTP_200_OK


def test_graphql_view_initialization(user_with_all_permissions, client):
    client.force_login(user_with_all_permissions)
    url = reverse("graphql")
    response = client.post(
        url,
        data={"query": "query { hello }"},
        content_type="application/json",
        accept="application/json",
    )

    print(response.content)
    assert response.status_code == status.HTTP_200_OK
