from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, StackedInline

from .models import ApplicationTracking
from .models import Document
from .models import UniversityProgram


class ApplicationTrackingInline(StackedInline):
    model = ApplicationTracking
    extra = 0
    fields = ('status', 'priority', 'application_submission_date', 'start_date', 'end_date', 'notes')
    classes = ['collapse']


@admin.register(UniversityProgram)
class UniversityProgramAdmin(ModelAdmin):
    list_fullwidth = True
    list_horizontal_scrollbar_top = True
    compressed_fields = True

    # Display the most important fields in the list view of the admin panel
    list_display = (
        'name', 'university', 'field', 'degree', 'teaching_language', 'application_deadline',
        'status'
    )

    # Filters for the list view
    list_filter = ('field', 'degree', 'teaching_language', 'status')

    # Searchable fields
    search_fields = ('name', 'university', 'description', 'personal_note')

    # Inline model (assuming ApplicationTracking is related)
    inlines = [ApplicationTrackingInline]

    # Fieldsets to group fields in the form view
    fieldsets = (
        ('Overview', {
            'fields': ('link', 'name', 'university', 'field', 'degree', 'teaching_language', 'languages',
                       'program_duration', 'beginning', 'combined_phd', 'joint_degree', 'description'),
            'classes': ['tab']
        }),
        ('Details', {
            'fields': ('course_organisation', 'diploma_supplement', 'international_elements',
                       'german_language_courses', 'english_language_courses', 'about_university',
                       'full_time_part_time', 'supervisor_student_ratio'),
            'classes': ['tab']
        }),
        ('Costs and Funding', {
            'fields': ('tuition_fees', 'costs_of_living', 'semester_contribution', 'funding_opportunities'),
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
        ('Tracking', {
            'fields': ('status', 'personal_note'),
            'classes': ['tab']
        }),
    )


@admin.register(ApplicationTracking)
class ApplicationTrackingAdmin(ModelAdmin):
    list_fullwidth = True
    list_horizontal_scrollbar_top = True
    compressed_fields = True

    # Display more relevant fields in the list view
    list_display = (
        'university_program', 'status', 'priority', 'application_submission_date', 'start_date', 'end_date',
        'get_needed_docs'
    )

    # Filter options to easily narrow down by status and priority
    list_filter = ('status', 'priority', 'start_date', 'end_date')

    # Search across more fields for improved admin usability
    search_fields = ('university_program__name', 'university_program__university', 'notes')

    # Group related fields in the form using fieldsets
    fieldsets = (
        ('Program Information', {
            'fields': ('university_program',)
        }),
        ('Application Tracking', {
            'fields': ('status', 'priority', 'application_submission_date', 'start_date', 'end_date',)
        }),
        ('Documents', {
            'fields': ('required_docs',)
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
    )

    filter_horizontal = ('required_docs',)

    # Method to display needed documents in the list display
    def get_needed_docs(self, obj):
        # Return a formatted list of required documents
        needed_docs = obj.required_docs.all()
        if needed_docs.exists():
            return format_html("<br>".join([doc.name for doc in needed_docs]))
        return "No documents required"

    # Customize the column name in the admin interface
    get_needed_docs.short_description = 'Needed Documents'


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display = ('name', 'is_available')
    search_fields = ('name',)
    list_filter = ('is_available',)
    ordering = ('-is_available', 'name',)
    list_editable = ('is_available',)
