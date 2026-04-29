from django.shortcuts import get_object_or_404
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.content import selectors as content_selectors
from apps.content.models import Event, GalleryCategory, NewsCategory, NewsPost, Program
from apps.news_request.models import NewsRequestPayment, NewsUploadRequest
from apps.news_request.services import create_news_request, upload_payment_proof
from apps.organization import selectors as organization_selectors
from apps.registration import selectors as registration_selectors
from apps.website import selectors as website_selectors
from apps.api.serializers import (
    ChairmanHistorySerializer,
    ContactMessageCreateSerializer,
    EventSerializer,
    GalleryCategorySerializer,
    GalleryImageSerializer,
    HomeContractSerializer,
    ManagementMemberSerializer,
    NewsCategorySerializer,
    NewsPostSerializer,
    NewsRequestPaymentUploadSerializer,
    NewsUploadRequestCreateSerializer,
    NewsUploadRequestTrackingSerializer,
    OrganizationProfileSerializer,
    ProgramSerializer,
    RegistrationFormSerializer,
)
from apps.website.models import ContactMessage


class HomeContractAPIView(APIView):
    @extend_schema(responses=HomeContractSerializer)
    def get(self, request):
        data = {
            "settings": website_selectors.site_settings_map(),
            "navigation": website_selectors.active_navigation(),
            "profile": organization_selectors.organization_profile(),
            "featured_programs": content_selectors.featured_programs(limit=6),
            "latest_news": content_selectors.latest_news(limit=6),
            "upcoming_events": content_selectors.upcoming_events(limit=6),
            "gallery": content_selectors.visible_gallery_images()[:8],
        }
        return Response(HomeContractSerializer(data, context={"request": request}).data)


class OrganizationProfileAPIView(APIView):
    @extend_schema(responses=OrganizationProfileSerializer)
    def get(self, request):
        profile = organization_selectors.organization_profile()
        return Response(OrganizationProfileSerializer(profile, context={"request": request}).data)


class ManagementMemberListAPIView(generics.ListAPIView):
    serializer_class = ManagementMemberSerializer

    def get_queryset(self):
        return organization_selectors.active_management_members()


class ChairmanHistoryListAPIView(generics.ListAPIView):
    serializer_class = ChairmanHistorySerializer

    def get_queryset(self):
        return organization_selectors.visible_chairmen()


class ProgramListAPIView(generics.ListAPIView):
    serializer_class = ProgramSerializer
    search_fields = ("title", "category", "description")
    ordering_fields = ("sort_order", "created_at")

    def get_queryset(self):
        return content_selectors.published_programs()


class ProgramDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProgramSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Program.objects.filter(status=Program.STATUS_PUBLISHED)


class EventListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    search_fields = ("title", "location", "description")
    ordering_fields = ("start_date", "created_at")

    def get_queryset(self):
        return content_selectors.published_events()


class EventDetailAPIView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Event.objects.filter(status=Event.STATUS_PUBLISHED)


class NewsPostListAPIView(generics.ListAPIView):
    serializer_class = NewsPostSerializer
    search_fields = ("title", "excerpt", "content", "author_name")
    ordering_fields = ("published_at", "created_at")

    def get_queryset(self):
        queryset = content_selectors.published_news()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset


class NewsCategoryListAPIView(generics.ListAPIView):
    serializer_class = NewsCategorySerializer
    pagination_class = None

    def get_queryset(self):
        return NewsCategory.objects.order_by("name")


class NewsPostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = NewsPostSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return NewsPost.objects.select_related("category", "created_by").filter(status=NewsPost.STATUS_PUBLISHED)


class GalleryImageListAPIView(generics.ListAPIView):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        queryset = content_selectors.visible_gallery_images()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset


class GalleryCategoryListAPIView(generics.ListAPIView):
    serializer_class = GalleryCategorySerializer
    pagination_class = None

    def get_queryset(self):
        return GalleryCategory.objects.order_by("name")


class RegistrationFormListAPIView(generics.ListAPIView):
    serializer_class = RegistrationFormSerializer

    def get_queryset(self):
        queryset = registration_selectors.active_registration_forms()
        form_type = self.request.query_params.get("type")
        if form_type:
            queryset = queryset.filter(type=form_type)
        return queryset


class NewsUploadRequestCreateAPIView(generics.CreateAPIView):
    serializer_class = NewsUploadRequestCreateSerializer
    queryset = NewsUploadRequest.objects.all()

    @extend_schema(
        request=NewsUploadRequestCreateSerializer,
        responses={201: NewsUploadRequestCreateSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        news_request = create_news_request(serializer)
        output = self.get_serializer(news_request)
        return Response(output.data, status=status.HTTP_201_CREATED)


class NewsUploadRequestTrackingAPIView(generics.RetrieveAPIView):
    serializer_class = NewsUploadRequestTrackingSerializer
    lookup_field = "tracking_code"
    queryset = NewsUploadRequest.objects.select_related("payment")


class NewsRequestPaymentUploadAPIView(APIView):
    @extend_schema(
        request=NewsRequestPaymentUploadSerializer,
        responses={
            200: NewsRequestPaymentUploadSerializer,
            404: OpenApiResponse(description="Request berita tidak ditemukan."),
        },
    )
    def post(self, request, request_id):
        news_request = get_object_or_404(NewsUploadRequest, pk=request_id)
        serializer = NewsRequestPaymentUploadSerializer(
            news_request.payment,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        payment = upload_payment_proof(serializer)
        return Response(NewsRequestPaymentUploadSerializer(payment).data)


class ContactMessageCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactMessageCreateSerializer
    queryset = ContactMessage.objects.all()
