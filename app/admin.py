from django.contrib import admin
from django.db.models import Case, When, Value
from unfold.admin import ModelAdmin, TabularInline

from .models import ApplicationTracking, ApplicationStatus, University
from .models import UniversityProgram


@admin.register(UniversityProgram)
class UniversityProgramAdmin(ModelAdmin):
    list_fullwidth = True
    list_horizontal_scrollbar_top = True
    compressed_fields = True

    # Display the most important fields in the list view of the admin panel
    list_display = (
        'university', 'name', 'status'
    )

    # Filters for the list view
    list_filter = ('degree', 'status')

    # Searchable fields
    search_fields = ('university',)

    ordering = ('university',)

    # display 10 records per page
    list_per_page = 200

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


    def get_ordering(self, request):
        return (
            Case(
                When(status=ApplicationStatus.ACCEPTED, then=Value(1)),
                When(status=ApplicationStatus.IN_PROGRESS, then=Value(2)),
                When(status=ApplicationStatus.NOT_STARTED, then=Value(3)),
                When(status=ApplicationStatus.REJECTED, then=Value(4)),
                default=Value(5),
            ),
        )


class ApplicationTrackingInline(TabularInline):
    model = ApplicationTracking
    extra = 0
    classes = ['collapse']
    # exclude = ["notes", ]
    can_delete = False
    show_change_link = True

    def get_ordering(self, request):
        return (
            Case(
                When(status=ApplicationStatus.ACCEPTED, then=Value(1)),
                When(status=ApplicationStatus.IN_PROGRESS, then=Value(2)),
                When(status=ApplicationStatus.NOT_STARTED, then=Value(3)),
                When(status=ApplicationStatus.REQUIREMENTS_BARELY_MET, then=Value(4)),
                When(status=ApplicationStatus.REJECTED, then=Value(5)),
                default=Value(5),
            ),
        )

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(University)
class UniversityAdmin(ModelAdmin):
    list_filter = ('status',)
    list_display = ('name', 'status', 'display_applied_programs',)
    inlines = [ApplicationTrackingInline]

    def get_ordering(self, request):
        return (
            Case(
                When(status=University.Status.NOT_CHECKED, then=Value(0)),
                When(status=University.Status.WAITING_FOR_APPLICATION, then=Value(1)),
                When(status=University.Status.PARTIALLY_CHECKED, then=Value(2)),
                When(status=University.Status.FULLY_CHECKED, then=Value(3)),
                default=Value(4),
            ),
        )

    # display count of applied programs
    @admin.display(description='Applied Programs')
    def display_applied_programs(self, obj):
        return obj.applications.count()
