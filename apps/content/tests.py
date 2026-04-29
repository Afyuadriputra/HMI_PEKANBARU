from datetime import date

from django.test import TestCase

from apps.content.forms import EventForm, NewsPostForm, ProgramForm
from apps.content.models import Event, NewsPost, Program
from apps.content.selectors import latest_news, published_programs, upcoming_events
from apps.content.services import save_event_form, save_news_form, save_program_form
from apps.core.test_factories import create_news_category, create_user


class ContentServiceTests(TestCase):
    def setUp(self):
        self.user = create_user()
        self.category = create_news_category()

    def test_program_can_be_created_without_manual_slug_and_gets_unique_slug(self):
        first_form = ProgramForm(
            data={
                "title": "Basic Training",
                "category": "Kaderisasi",
                "description": "Program LK",
                "content": "Konten program",
                "status": Program.STATUS_PUBLISHED,
                "sort_order": 1,
            }
        )
        second_form = ProgramForm(
            data={
                "title": "Basic Training",
                "category": "Kaderisasi",
                "description": "Program LK kedua",
                "content": "Konten program kedua",
                "status": Program.STATUS_PUBLISHED,
                "sort_order": 2,
            }
        )

        self.assertTrue(first_form.is_valid(), first_form.errors)
        self.assertTrue(second_form.is_valid(), second_form.errors)
        first = save_program_form(first_form, self.user)
        second = save_program_form(second_form, self.user)

        self.assertEqual(first.slug, "basic-training")
        self.assertEqual(second.slug, "basic-training-2")
        self.assertEqual(first.created_by, self.user)

    def test_published_program_selector_hides_drafts(self):
        Program.objects.create(title="Published", slug="published", status=Program.STATUS_PUBLISHED)
        Program.objects.create(title="Draft", slug="draft", status=Program.STATUS_DRAFT)

        self.assertEqual(list(published_programs().values_list("title", flat=True)), ["Published"])

    def test_publishing_news_sets_published_timestamp_and_latest_news_hides_drafts(self):
        published_form = NewsPostForm(
            data={
                "category": self.category.id,
                "title": "Berita LK",
                "excerpt": "Ringkasan",
                "content": "Isi berita",
                "author_name": "HMI Pekanbaru",
                "status": NewsPost.STATUS_PUBLISHED,
            }
        )
        draft_form = NewsPostForm(
            data={
                "category": self.category.id,
                "title": "Draft Berita",
                "excerpt": "Ringkasan",
                "content": "Isi draft",
                "author_name": "HMI Pekanbaru",
                "status": NewsPost.STATUS_DRAFT,
            }
        )

        self.assertTrue(published_form.is_valid(), published_form.errors)
        self.assertTrue(draft_form.is_valid(), draft_form.errors)
        post = save_news_form(published_form, self.user)
        draft = save_news_form(draft_form, self.user)

        self.assertIsNotNone(post.published_at)
        self.assertIsNone(draft.published_at)
        self.assertEqual(list(latest_news().values_list("title", flat=True)), ["Berita LK"])

    def test_upcoming_events_only_returns_published_future_events(self):
        future_form = EventForm(
            data={
                "title": "Agenda Publik",
                "description": "Agenda",
                "content": "Konten",
                "location": "Pekanbaru",
                "start_date": date(2099, 1, 1),
                "status": Event.STATUS_PUBLISHED,
            }
        )
        draft_form = EventForm(
            data={
                "title": "Agenda Draft",
                "description": "Agenda",
                "content": "Konten",
                "location": "Pekanbaru",
                "start_date": date(2099, 1, 2),
                "status": Event.STATUS_DRAFT,
            }
        )

        self.assertTrue(future_form.is_valid(), future_form.errors)
        self.assertTrue(draft_form.is_valid(), draft_form.errors)
        save_event_form(future_form, self.user)
        save_event_form(draft_form, self.user)

        self.assertEqual(list(upcoming_events().values_list("title", flat=True)), ["Agenda Publik"])
