from urllib.error import URLError
from urllib.request import urlopen

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.content.models import Event, GalleryImage, NewsCategory, NewsPost, Program
from apps.core.utils import generate_unique_slug
from apps.organization.models import ManagementMember, OrganizationProfile
from apps.registration.models import RegistrationForm


class Command(BaseCommand):
    help = "Seed konten awal dari desain static HMI Pekanbaru."

    def handle(self, *args, **options):
        profile, _ = OrganizationProfile.objects.update_or_create(
            name="Himpunan Mahasiswa Islam Pekanbaru",
            defaults={
                "short_name": "HMI Pekanbaru",
                "description": "Wadah perjuangan intelektual, kepemimpinan, dan pengabdian kader muda Islam dalam mewujudkan masyarakat adil makmur.",
                "history": "Himpunan Mahasiswa Islam (HMI) Cabang Pekanbaru merupakan bagian integral dari perjuangan HMI di tingkat nasional. Berfokus pada pembinaan kepribadian kader yang memiliki kualitas insan cita.",
                "vision": "Terbinanya insan akademis, pencipta, pengabdi yang bernafaskan Islam, dan bertangung jawab atas terwujudnya masyarakat adil makmur.",
                "mission": "Melaksanakan perkaderan yang berkualitas, mengembangkan potensi intelektual mahasiswa, dan aktif dalam pengabdian.",
                "founded_year": 1947,
                "address": "Jl. Melayu No. 12, Marpoyan Damai, Pekanbaru, Riau 28282",
                "email": "sekretariat@hmipekanbaru.or.id",
                "phone": "(0761) 123 4567",
            },
        )

        members = [
            ("Ahmad Fauzi", "Ketua Umum", 1),
            ("Rizky Ramadhan", "Sekretaris Umum", 2),
            ("Dedi Kurniawan", "Bendahara Umum", 3),
        ]
        for name, position, order in members:
            ManagementMember.objects.update_or_create(
                name=name,
                defaults={
                    "position": position,
                    "period": "2026-2027",
                    "sort_order": order,
                    "status": ManagementMember.STATUS_ACTIVE,
                },
            )

        programs = [
            ("Perkaderan Latihan Kader I", "Gerbang utama pembinaan karakter dan ideologi mahasiswa Islam untuk menjadi kader berkualitas.", "school", True, 1),
            ("Kajian Intelektual", "Diskusi rutin mingguan membedah isu kontemporer.", "menu_book", True, 2),
            ("HMI Mengabdi", "Program aksi sosial dan pemberdayaan masyarakat.", "volunteer_activism", True, 3),
            ("Advokasi Kampus", "Pendampingan aspirasi mahasiswa di lingkungan kampus.", "public", True, 4),
            ("Penerbitan Jurnal", "Publikasi karya ilmiah dan opini kader HMI.", "edit_note", False, 5),
        ]
        for title, description, icon, featured, order in programs:
            Program.objects.update_or_create(
                title=title,
                defaults={
                    "slug": self._slug_for(Program, title),
                    "category": "Program Strategis",
                    "description": description,
                    "content": description,
                    "icon": icon,
                    "is_featured": featured,
                    "button_text": "Info Pendaftaran",
                    "sort_order": order,
                    "status": Program.STATUS_PUBLISHED,
                },
            )

        categories = {}
        for name in ["Berita", "Opini", "Kegiatan"]:
            categories[name], _ = NewsCategory.objects.update_or_create(
                name=name,
                defaults={"slug": self._slug_for(NewsCategory, name)},
            )

        news_posts = [
            ("Pelantikan Pengurus Baru HMI Pekanbaru", "Berita", "Himpunan Mahasiswa Islam Cabang Pekanbaru resmi melantik jajaran pengurus baru untuk masa khidmat satu tahun ke depan."),
            ("Digitalisasi Dakwah: Tantangan Kader di Era Modern", "Opini", "Menghadapi pesatnya arus informasi, kader HMI dituntut untuk cakap dalam memanfaatkan teknologi sebagai medium perjuangan."),
            ("Seminar Nasional: Peran Pemuda dalam Pemilu", "Kegiatan", "Seminar yang menghadirkan tokoh nasional ini bertujuan membekali mahasiswa dengan pemahaman politik yang sehat dan inklusif."),
        ]
        for title, category, excerpt in news_posts:
            NewsPost.objects.update_or_create(
                title=title,
                defaults={
                    "category": categories[category],
                    "slug": self._slug_for(NewsPost, title),
                    "excerpt": excerpt,
                    "content": excerpt,
                    "author_name": "HMI Pekanbaru",
                    "published_at": timezone.now(),
                    "status": NewsPost.STATUS_PUBLISHED,
                },
            )

        events = [
            ("Intermediate Training (LK II) Nasional", "Pekanbaru akan menjadi tuan rumah pelatihan kepemimpinan tingkat menengah yang diikuti utusan cabang se-Indonesia.", "Hotel Grand Elite", "2026-12-15", "2026-12-22", True),
            ("Diskusi Pahlawan", "Diskusi refleksi kepahlawanan dan kontribusi pemuda.", "Sekretariat HMI Pekanbaru", "2026-11-10", None, False),
            ("Latihan Kader 1 (LK1)", "Latihan dasar perkaderan HMI Cabang Pekanbaru.", "Wisma Haji Riau", "2026-11-18", None, False),
            ("Malam Keakraban", "Forum silaturahmi dan penguatan solidaritas kader.", "Ballroom Pangeran Hotel", "2026-12-02", None, False),
        ]
        for title, description, location, start_date, end_date, featured in events:
            Event.objects.update_or_create(
                title=title,
                defaults={
                    "slug": self._slug_for(Event, title),
                    "description": description,
                    "content": description,
                    "location": location,
                    "start_date": start_date,
                    "end_date": end_date,
                    "is_featured": featured,
                    "status": Event.STATUS_PUBLISHED,
                },
            )

        RegistrationForm.objects.update_or_create(
            title="Daftar Jadi Kader",
            defaults={
                "type": RegistrationForm.TYPE_KADER,
                "google_form_url": "https://forms.gle/example",
                "description": "Form pendaftaran kader HMI Cabang Pekanbaru.",
                "status": RegistrationForm.STATUS_ACTIVE,
            },
        )

        gallery_urls = [
            "https://lh3.googleusercontent.com/aida-public/AB6AXuDwXK1kMnT1GzzJr016cwDYPTG96Y4VPcma7LtHqhEjmfdU7dOShTzrv_T1qCQfIys8kZJEMgG8eUctCLg1aRLGhpvHB_BdTHwNZ3e9wY17QlylpXhPoYRVUj7_3dVVwpOiuweFph5hpZ7_f9rs3FBkJfi5dJSFCntUH4Yitky_64-E06GwAXX__lFkcD4lDS7Io30LNvEd2frx2QO0kcyo5NehoO4ODLcFXMxOa5PdC2SH6vFwRK4gGYfWgPMWU_-h_Pv5agtW5pw2",
            "https://lh3.googleusercontent.com/aida-public/AB6AXuBhQg4RgIQ8kIFUMMGsOSFhZCL7D0dTtioOPtooMe-Qhe7jDqBOZD_JgJrreBF7fZ7vySY02v5RlkvWd1kbOcxnYVe5T4Q29vcXMPmOb9cj0u8NIA498hF6VofVxwm5u3dyLc_jnO-NJpIE1b2SiUSpsPDFU8ZBI7Wu1E--4PC3s8aGhM0pS9ibSBFbn0oC5UQx9T2vqdufolPNd44CI17yYE-_4OsGwZe5R410HKZcfjzmg_8Xk_wczJS06EKCDABzBP0sAnUIn8Eb",
            "https://lh3.googleusercontent.com/aida-public/AB6AXuDEzqPcUE5o01Ga70KFi8P1qDAYshvnPjsaTelOlA_Q2OiJGLYPAXwriPXR8a2wNa_Uhqlj_v8eDl2AoOa6Ne9R-iwE54Mj7ablfVyx_G-C8dZv3k-cZYjPHMuojZcB-IfYdbm0r0oPDVZ6DHojvGkJnYtiyGrst_rk8rhqOG1NFjXPdQNDqa1gOFaFlDxm05gkaU6ZLnUvwQPLj7X2y_GraxY36XFGTlgOGGovNxcEBnHhcOy2V5IDX-eEGgtfHZDbL01Mh3-pFO4_",
            "https://lh3.googleusercontent.com/aida-public/AB6AXuAz9B6Zfu1fKGEJzQnYNdJICC_9z4ZIJYptWfFcUjzp3lM1nWnjc2IY_E0UwCboVZWXE-4eLw6zgCobp8HIe4aL1822uZ0NbEafsBTi5LHJ86rxvAe3WeiTVy2YX4lUUvPtk795h_uUF6VIRldkW9g1n_qRx0-IKDqw7O8Xaj6C-6uwiJUG9IatiSaUMpr17KqbVw8YDt_uNlhxKcIrA4TbDZ-WvOtc073VOcZqTO4BGx2IRGNctYBPzdfguzFbiwskoZFaTwUURVWm",
        ]
        for index, image_url in enumerate(gallery_urls, start=1):
            gallery, created = GalleryImage.objects.get_or_create(
                title=f"Jejak Langkah {index}",
                defaults={
                    "alt_text": f"Galeri {index}",
                    "sort_order": index,
                    "status": GalleryImage.STATUS_SHOW,
                },
            )
            if created or not gallery.image:
                self._attach_remote_image(gallery.image, image_url, f"jejak-langkah-{index}.jpg")
                if gallery.image:
                    gallery.save(update_fields=["image", "updated_at"])

        self.stdout.write(self.style.SUCCESS(f"Static site seed selesai: {profile.name}"))

    def _slug_for(self, model_class, title):
        existing = model_class.objects.filter(title=title).first() if hasattr(model_class, "title") else None
        if existing:
            return existing.slug
        return generate_unique_slug(model_class, title)

    def _attach_remote_image(self, image_field, url, filename):
        try:
            with urlopen(url, timeout=15) as response:
                image_field.save(filename, ContentFile(response.read()), save=False)
        except (URLError, TimeoutError, OSError) as exc:
            self.stderr.write(f"Gagal download gambar {filename}: {exc}")
