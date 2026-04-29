# Backend Diagrams - SI-HMI Pekanbaru

Dokumen ini berisi diagram utama yang diperlukan untuk dokumentasi backend Django SI-HMI Pekanbaru. Format diagram memakai Mermaid agar bisa dirender di GitHub, GitLab, Obsidian, Notion tertentu, atau Mermaid Live Editor.

## Diagram Yang Diperlukan

1. **System Context Diagram**: menunjukkan aktor eksternal dan batas sistem.
2. **Container Diagram**: menunjukkan frontend, backend Django, database, media storage, dan layanan eksternal.
3. **Django Layered Architecture Diagram**: menunjukkan pola 4 layer dari PRD.
4. **Application Module Diagram**: menunjukkan pembagian app Django per domain.
5. **Public API Contract Diagram**: menunjukkan endpoint API publik untuk React.
6. **ERD Domain Diagram**: menunjukkan relasi tabel utama.
7. **Request Upload Berita Flow**: menunjukkan flow request berita berbayar.
8. **LK Assessment & Certificate Flow**: menunjukkan flow penilaian LK dan upload sertifikat.
9. **Deployment Diagram**: menunjukkan topologi production.

---

## 1. System Context Diagram

```mermaid
flowchart LR
    visitor[Pengunjung Website]
    adminWeb[Admin Website]
    adminAdm[Admin Administrasi]
    superAdmin[Super Admin]
    react[Frontend Publik React]
    django[SI-HMI Pekanbaru Backend Django]
    gform[Google Form]
    gmail[Gmail API - tahap lanjutan]

    visitor --> react
    react -->|Public REST API| django
    visitor -->|Pendaftaran| gform

    adminWeb -->|Django Admin Panel / Backend Administration| django
    adminAdm -->|Django Admin Panel / Backend Administration| django
    superAdmin -->|Full Admin Access| django

    django -.->|Future email integration| gmail
```

---

## 2. Container Diagram

```mermaid
flowchart TB
    subgraph Client
        react[React Public Frontend]
        browser[Browser]
    end

    subgraph Backend["Django Backend"]
        urls[config.urls]
        api[apps.api - Public REST API]
        templates[Django Templates Admin/Public Legacy]
        services[services.py]
        selectors[selectors.py]
        models[models.py]
    end

    subgraph Data
        postgres[(PostgreSQL)]
        media[(Django Media Storage)]
        static[Static Files / WhiteNoise]
    end

    subgraph External
        googleForms[Google Form]
        gmail[Gmail API - Future]
    end

    browser --> react
    react -->|JSON / multipart| urls
    urls --> api
    urls --> templates
    api --> selectors
    api --> services
    templates --> selectors
    templates --> services
    selectors --> models
    services --> models
    models --> postgres
    models --> media
    urls --> static
    react --> googleForms
    services -.-> gmail
```

---

## 3. Django Layered Architecture Diagram

```mermaid
flowchart TB
    presentation[Presentation Layer<br/>views.py, urls.py, templates, forms.py, api/views.py, api/serializers.py]
    business[Business Logic Layer<br/>services.py]
    dataAccess[Data Access Layer<br/>selectors.py]
    data[Data Layer<br/>models.py, migrations]
    db[(PostgreSQL)]
    media[(Media Files)]

    presentation -->|commands / mutations| business
    presentation -->|queries / lists / details| dataAccess
    business --> data
    dataAccess --> data
    data --> db
    data --> media
```

Rules:

- Views/API tidak berisi query kompleks.
- Services menangani create/update/delete dan validasi bisnis.
- Selectors menangani query, filter, `select_related`, `prefetch_related`.
- Models hanya representasi schema, choices, constraints, indexes.

---

## 4. Application Module Diagram

```mermaid
flowchart LR
    core[core<br/>base model, utils, permissions]
    accounts[accounts<br/>roles, users]
    website[website<br/>settings, menus, contact]
    organization[organization<br/>profile, management, chairmen]
    content[content<br/>program, event, news, gallery]
    registration[registration<br/>Google Form links]
    cadre[cadre<br/>commissariat, cadres, alumni]
    training[training<br/>LK, assessment, certificate]
    administration[administration<br/>archives, letters, invitations, gmail]
    newsRequest[news_request<br/>paid news request, payment]
    api[api<br/>public REST contract]

    api --> website
    api --> organization
    api --> content
    api --> registration
    api --> newsRequest

    accounts --> core
    website --> core
    organization --> core
    content --> core
    registration --> core
    cadre --> core
    training --> core
    administration --> core
    newsRequest --> core

    content --> accounts
    registration --> accounts
    training --> accounts
    administration --> accounts
    newsRequest --> accounts
    training --> cadre
    cadre --> training
    administration --> content
    newsRequest --> content
```

---

## 5. Public API Contract Diagram

```mermaid
flowchart TB
    react[React Public Frontend]

    subgraph API["/api/v1"]
        home[GET /home/]
        profile[GET /organization/profile/]
        management[GET /organization/management/]
        chairmen[GET /organization/chairmen/]
        programs[GET /programs/<br/>GET /programs/:slug/]
        events[GET /events/<br/>GET /events/:slug/]
        news[GET /news/<br/>GET /news/:slug/<br/>GET /news/categories/]
        gallery[GET /gallery/<br/>GET /gallery/categories/]
        forms[GET /registration-forms/]
        contact[POST /contact-messages/]
        requestNews[POST /news-requests/]
        payment[POST /news-requests/:id/payment/]
        tracking[GET /news-requests/track/:tracking_code/]
    end

    react --> home
    react --> profile
    react --> management
    react --> chairmen
    react --> programs
    react --> events
    react --> news
    react --> gallery
    react --> forms
    react --> contact
    react --> requestNews
    react --> payment
    react --> tracking
```

OpenAPI:

```text
GET /api/schema/
GET /api/docs/
```

---

## 6. ERD Domain Diagram

```mermaid
erDiagram
    roles ||--o{ users : has

    users ||--o{ programs : creates
    users ||--o{ events : creates
    users ||--o{ news_posts : creates
    users ||--o{ gallery_images : uploads
    users ||--o{ registration_forms : creates
    users ||--o{ lk_batches : creates
    users ||--o{ lk_assessments : assesses
    users ||--o{ document_archives : uploads
    users ||--o{ incoming_letters : creates
    users ||--o{ outgoing_letters : creates
    users ||--o{ invitations : creates
    users ||--o{ news_upload_requests : reviews

    news_categories ||--o{ news_posts : categorizes
    news_categories ||--o{ news_upload_requests : categorizes
    news_upload_requests ||--o{ news_posts : publishes_to
    news_upload_requests ||--|| news_request_payments : has

    gallery_categories ||--o{ gallery_images : categorizes

    commissariats ||--o{ cadres : has
    commissariats ||--o{ alumni : has
    cadres ||--o{ alumni : may_become
    cadres ||--o{ cadre_lk_histories : has

    lk_levels ||--o{ lk_batches : has
    lk_levels ||--o{ lk_materials : has
    lk_levels ||--o{ cadre_lk_histories : referenced_by
    lk_batches ||--o{ lk_participants : has
    lk_batches ||--o{ lk_materials : may_have
    lk_batches ||--o{ lk_assessments : has
    lk_batches ||--o{ cadre_lk_histories : referenced_by
    lk_participants ||--o{ lk_assessments : assessed_by
    lk_assessments ||--o{ lk_assessment_details : has
    lk_materials ||--o{ lk_assessment_details : scored_by
    lk_participants ||--o{ lk_certificates : receives
    lk_assessments ||--o{ lk_certificates : supports
    signatures ||--o{ lk_certificates : signs

    events ||--o{ invitations : may_link
    gmail_integrations ||--o{ email_logs : records
```

---

## 7. Request Upload Berita Flow

```mermaid
sequenceDiagram
    actor Visitor as Pengunjung
    participant React as React Frontend
    participant API as Django Public API
    participant Service as news_request.services
    participant DB as PostgreSQL
    participant Admin as Admin Website

    Visitor->>React: Isi form request berita
    React->>API: POST /api/v1/news-requests/
    API->>Service: create_news_request()
    Service->>DB: Simpan request status=pending + payment unpaid + tracking_code
    API-->>React: id, tracking_code, price, status

    Visitor->>React: Upload bukti pembayaran
    React->>API: POST /api/v1/news-requests/:id/payment/
    API->>Service: upload_payment_proof()
    Service->>DB: payment=paid, request=paid
    API-->>React: payment_status=paid

    Admin->>API: Review via backend/admin panel
    API->>Service: verify_payment(), approve_request(), publish_news_request_as_post()
    Service->>DB: Update status dan create news_posts

    Visitor->>React: Cek tracking code
    React->>API: GET /api/v1/news-requests/track/:tracking_code/
    API-->>React: request status + payment status
```

---

## 8. LK Assessment & Certificate Flow

```mermaid
sequenceDiagram
    actor Admin as Admin Administrasi
    participant Django as Django Admin Panel
    participant TrainingService as training.services
    participant DB as PostgreSQL
    participant Media as Media Storage

    Admin->>Django: Buat LK Level dan LK Batch
    Django->>DB: Simpan lk_levels, lk_batches

    Admin->>Django: Input peserta LK dari rekap Google Form
    Django->>DB: Simpan lk_participants

    Admin->>Django: Input materi dan nilai peserta
    Django->>TrainingService: create_lk_assessment()
    TrainingService->>DB: Simpan lk_assessments + lk_assessment_details
    TrainingService->>DB: Update graduation_status peserta

    Admin->>Django: Upload sertifikat manual
    Django->>TrainingService: upload_lk_certificate()
    TrainingService->>DB: Simpan lk_certificates
    TrainingService->>Media: Simpan file sertifikat
```

---

## 9. Deployment Diagram

```mermaid
flowchart TB
    user[User Browser]
    cdn[Static CDN / Browser Cache]
    react[React Frontend Hosting]
    nginx[Nginx / Reverse Proxy]
    gunicorn[Gunicorn]
    django[Django App]
    postgres[(PostgreSQL)]
    media[(Media Storage)]
    static[WhiteNoise Static Files]

    user --> react
    react -->|HTTPS REST API| nginx
    nginx --> gunicorn
    gunicorn --> django
    django --> postgres
    django --> media
    django --> static
    user --> cdn
```

Production notes:

- `DEBUG=False`
- `SECRET_KEY` dari environment
- `ALLOWED_HOSTS` domain production
- `CORS_ALLOWED_ORIGINS` domain frontend React
- Static via WhiteNoise atau CDN
- Media via local mounted volume atau object storage
- PostgreSQL wajib backup rutin

