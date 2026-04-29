from django.urls import path

from apps.api import views

app_name = "api"

urlpatterns = [
    path("home/", views.HomeContractAPIView.as_view(), name="home"),
    path("organization/profile/", views.OrganizationProfileAPIView.as_view(), name="organization_profile"),
    path("organization/management/", views.ManagementMemberListAPIView.as_view(), name="management_list"),
    path("organization/chairmen/", views.ChairmanHistoryListAPIView.as_view(), name="chairman_list"),
    path("programs/", views.ProgramListAPIView.as_view(), name="program_list"),
    path("programs/<slug:slug>/", views.ProgramDetailAPIView.as_view(), name="program_detail"),
    path("events/", views.EventListAPIView.as_view(), name="event_list"),
    path("events/<slug:slug>/", views.EventDetailAPIView.as_view(), name="event_detail"),
    path("news/categories/", views.NewsCategoryListAPIView.as_view(), name="news_category_list"),
    path("news/", views.NewsPostListAPIView.as_view(), name="news_list"),
    path("news/<slug:slug>/", views.NewsPostDetailAPIView.as_view(), name="news_detail"),
    path("gallery/categories/", views.GalleryCategoryListAPIView.as_view(), name="gallery_category_list"),
    path("gallery/", views.GalleryImageListAPIView.as_view(), name="gallery_list"),
    path("registration-forms/", views.RegistrationFormListAPIView.as_view(), name="registration_form_list"),
    path("contact-messages/", views.ContactMessageCreateAPIView.as_view(), name="contact_message_create"),
    path("news-requests/", views.NewsUploadRequestCreateAPIView.as_view(), name="news_request_create"),
    path(
        "news-requests/track/<uuid:tracking_code>/",
        views.NewsUploadRequestTrackingAPIView.as_view(),
        name="news_request_tracking",
    ),
    path(
        "news-requests/<int:request_id>/payment/",
        views.NewsRequestPaymentUploadAPIView.as_view(),
        name="news_request_payment_upload",
    ),
]
