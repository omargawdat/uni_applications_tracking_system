from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, StackedInline

from .models import ApplicationTracking
from .models import Document
from .models import UniversityProgram


@admin.register(UniversityProgram)
class UniversityProgramAdmin(ModelAdmin):
    list_fullwidth = True
    list_horizontal_scrollbar_top = True
    compressed_fields = True

    # Display the most important fields in the list view of the admin panel
    list_display = (
        'name', 'university','status'
    )

    # Filters for the list view
    list_filter = ('degree', 'status')

    # Searchable fields
    search_fields = ('name', 'university', 'description', 'personal_note')


    # Fieldsets to group fields in the form view
    fieldsets = (
        ('Overview', {
            'fields': ('status', 'link', 'name', 'degree', 'languages', 'description',),
            'classes': ['tab']
        }),
        ('Costs and Funding', {
            'fields': ('tuition_fees', 'costs_of_living', 'semester_contribution', 'funding_opportunities'),
            'classes': ['tab']
        }),
        ('Details', {
            'fields': ('course_organisation',
                       'about_university',
                       'full_time_part_time', 'supervisor_student_ratio'),
            'classes': ['tab']
        }),
        ('Requirements', {
            'fields': (
                'academic_requirements', 'language_requirements', 'application_deadline', 'submit_application_to'),
            'classes': ['tab']
        }),
        ('Services', {
            'fields': ('part_time_employment', 'accommodation', 'career_advisory_service',
                       'support_for_international_students'),
            'classes': ['tab']
        }),
        ('Other', {
            'fields': (
                "personal_note", 'combined_phd', 'joint_degree', 'diploma_supplement', 'international_elements', "program_duration"),
            'classes': ['tab']
        }),
    )


@admin.register(ApplicationTracking)
class ApplicationTrackingAdmin(ModelAdmin):
    list_fullwidth = True
    list_horizontal_scrollbar_top = True
    compressed_fields = True

    list_display = ('university', 'field', 'notes', 'application_submission_date', 'status', )

    list_filter = ('status', 'field')

    search_fields = ('university', 'notes')



@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display = ('name', 'is_available')
    search_fields = ('name',)
    list_filter = ('is_available',)
    ordering = ('-is_available', 'name',)
    list_editable = ('is_available',)
