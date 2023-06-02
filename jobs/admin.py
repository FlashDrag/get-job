from django.contrib import admin

from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    '''Define admin model for custom Vacancy model.'''

    # The fields which displayed in the list of vacancies in admin panel
    list_display = (
        "status",
        "title",
        # "employer",
        # "company",
        "area",
        "job_location",
        "job_type",
        "salary",
        "created_on",
        "experience",
    )
    # list of fields to generate filters in the right sidebar of admin panel
    list_filter = (
        "status",
        "area",
        # "employer",
        # "company",
        "job_type",
        "job_location",
        "salary",
    )
    search_fields = ("title", "body")

    # Sorted by vacancies that are in review and with the oldest created date
    ordering = ("status", "created_on")
