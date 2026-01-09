schoolCRM/                       ← репозиторий / продукт
├─ base_platform/                      ← Django project
│   ├─ base_platform/                  ← Django project настройки
│   │   ├─ settings.py           ← dev/prod/ base settings
│   │   ├─ urls.py               ← основной urls.py проекта
│   │   ├─ wsgi.py
│   │   └─ asgi.py
│   ├─ users/                    ← Django app: пользователи
│   │   ├─ models.py             ← User, Profile
│   │   ├─ admin.py
│   │   ├─ views.py              ← dashboard, профили
│   │   ├─ urls.py
│   │   ├─ decorators.py         ← role_required
│   │   └─ templates/users/      ← login.html, dashboard.html
│   ├─ crm/                      ← Django app: клиенты, сделки
│   │   ├─ models.py             ← Lead, Client, Deal, Status
│   │   ├─ views.py
│   │   ├─ urls.py
│   │   └─ templates/crm/
│   ├─ education/                ← Django app: курсы и уроки
│   │   ├─ models.py             ← Course, Lesson
│   │   ├─ views.py
│   │   ├─ urls.py
│   │   └─ templates/education/
│   ├─ schedule/                 ← Django app: расписание уроков
│   │   ├─ models.py             ← ScheduleEntry
│   │   ├─ views.py
│   │   ├─ urls.py
│   │   └─ templates/schedule/
│   ├─ finance/                  ← Django app: платежи и счета
│   │   ├─ models.py             ← Payment, Invoice
│   │   ├─ views.py
│   │   ├─ urls.py
│   │   └─ templates/finance/
│   ├─ tasks/                    ← Django app: задачи, напоминания
│   │   ├─ models.py             ← Task
│   │   ├─ views.py
│   │   ├─ urls.py
│   │   └─ templates/tasks/
│   └─ manage.py
├─ core/                         ← бизнес-логика, чистый Python
│   ├─ domain/                   ← сущности (entities)
│   │   ├─ user_entity.py        ← UserEntity
│   │   ├─ organization.py       ← Organization
│   │   ├─ course_entity.py      ← CourseEntity, LessonEntity
│   │   └─ task_entity.py        ← TaskEntity
│   ├─ application/              ← сценарии / use cases
│   │   ├─ use_cases/
│   │   │   ├─ create_organization.py
│   │   │   ├─ assign_role.py
│   │   │   └─ create_course.py
│   │   └─ services/             ← валидаторы, бизнес-сервисы
│   └─ interfaces/
│       └─ repositories.py       ← абстрактные интерфейсы репозиториев
├─ requirements.txt
└─ README.md


# Django apps

users → авторизация, кастомный User, роли, профили

crm → клиенты, сделки, статусы

education → курсы и уроки

schedule → расписание занятий

finance → платежи, счета, инвойсы

tasks → внутренние задачи, напоминания

В apps живут Django модели, views, urls, templates

# Core

domain/ → бизнес-сущности, чистые Python-классы, без Django (например, Organization, Course)

application/use_cases/ → сценарии (use cases), которые выполняют бизнес-логику через интерфейсы

interfaces/repositories.py → абстрактные репозитории, которые потом реализуются в Django apps

Важно: core не знает про HTTP, ORM, templates — его можно тестировать отдельно.


# Взаимодействие
views Django apps → вызывают use cases из core/application

use cases → работают с interfaces/repositories.py

Django ORM модели → реализуют репозитории (например, DjangoOrganizationRepository)

Такой подход позволяет менять инфраструктуру, но не ломать бизнес-логику.

сущности

Сущности

User (роль + права)

Organization / School

Student

Client / Lead

Course

Lesson

ScheduleEntry

Payment

Deal

Task

Analytics (будет позже)

Subscri