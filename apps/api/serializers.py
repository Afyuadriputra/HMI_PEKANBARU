from rest_framework import serializers

from apps.content.models import Event, GalleryCategory, GalleryImage, NewsCategory, NewsPost, Program
from apps.news_request.models import NewsRequestPayment, NewsUploadRequest
from apps.organization.models import ChairmanHistory, ManagementMember, OrganizationProfile
from apps.registration.models import RegistrationForm
from apps.website.models import ContactMessage, NavigationMenu


class NavigationMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationMenu
        fields = ("id", "title", "url", "location", "sort_order")


class OrganizationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProfile
        fields = (
            "id",
            "name",
            "short_name",
            "description",
            "history",
            "vision",
            "mission",
            "logo",
            "profile_image",
            "founded_year",
            "address",
            "email",
            "phone",
            "updated_at",
        )


class ManagementMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementMember
        fields = ("id", "name", "position", "photo", "period", "description", "sort_order")


class ChairmanHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChairmanHistory
        fields = ("id", "name", "period_start", "period_end", "photo", "description", "sort_order")


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            "id",
            "title",
            "slug",
            "category",
            "description",
            "content",
            "image",
            "icon",
            "is_featured",
            "button_text",
            "button_link",
            "registration_form_url",
            "sort_order",
            "created_at",
            "updated_at",
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "image",
            "location",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "is_featured",
            "registration_form_url",
            "created_at",
            "updated_at",
        )


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ("id", "name", "slug", "description")


class NewsPostSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer(read_only=True)

    class Meta:
        model = NewsPost
        fields = (
            "id",
            "category",
            "title",
            "slug",
            "excerpt",
            "content",
            "image",
            "author_name",
            "published_at",
            "created_at",
            "updated_at",
        )


class GalleryImageSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = GalleryImage
        fields = ("id", "category", "title", "image", "alt_text", "description", "sort_order")


class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = ("id", "name", "slug", "description")


class RegistrationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationForm
        fields = ("id", "title", "type", "google_form_url", "description")


class NewsUploadRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsUploadRequest
        fields = (
            "id",
            "tracking_code",
            "requester_name",
            "requester_email",
            "requester_phone",
            "title",
            "category",
            "content",
            "image",
            "attachment",
            "price",
            "status",
        )
        read_only_fields = ("id", "tracking_code", "price", "status")


class NewsRequestPaymentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsRequestPayment
        fields = ("id", "payment_method", "payment_proof", "payment_status")
        read_only_fields = ("id", "payment_status")


class NewsUploadRequestTrackingSerializer(serializers.ModelSerializer):
    payment_status = serializers.CharField(source="payment.payment_status", read_only=True)

    class Meta:
        model = NewsUploadRequest
        fields = (
            "tracking_code",
            "title",
            "price",
            "status",
            "payment_status",
            "reviewed_at",
            "notes",
            "created_at",
            "updated_at",
        )


class ContactMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = (
            "id",
            "sender_name",
            "sender_email",
            "sender_phone",
            "subject",
            "message",
            "status",
            "created_at",
        )
        read_only_fields = ("id", "status", "created_at")


class HomeContractSerializer(serializers.Serializer):
    settings = serializers.DictField(child=serializers.CharField(allow_blank=True))
    navigation = NavigationMenuSerializer(many=True)
    profile = OrganizationProfileSerializer(allow_null=True)
    featured_programs = ProgramSerializer(many=True)
    latest_news = NewsPostSerializer(many=True)
    upcoming_events = EventSerializer(many=True)
    gallery = GalleryImageSerializer(many=True)
