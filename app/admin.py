from django.contrib import admin
from django.db.models import Case, When, Value
from django.utils import timezone
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
                "personal_note", 'combined_phd', 'joint_degree', 'diploma_supplement', 'international_elements',
                "program_duration"),
            'classes': ['tab']
        }),
    )


@admin.register(ApplicationTracking)
class ApplicationTrackingAdmin(ModelAdmin):
    list_fullwidth = True
    list_horizontal_scrollbar_top = True
    compressed_fields = True
    list_display = ('university', 'field', 'status', "application_portal")
    list_editable = ('status', 'application_portal')
    list_filter = ('status', 'field', 'application_portal')

    def get_ordering(self, request):
        return (
            Case(
                When(application_portal="NOT_PICKED", then=Value(1)),
                When(status=ApplicationStatus.NOT_STARTED, then=Value(2)),
                When(status=ApplicationStatus.IN_PROGRESS, then=Value(3)),
                When(status=ApplicationStatus.NOT_STARTED, then=Value(4)),
                When(status=ApplicationStatus.ACCEPTED, then=Value(5)),

                default=Value(10),
            ),
        )

    def get_readonly_fields(self, request, obj=...):
        if obj.status == ApplicationStatus.IN_PROGRESS:
            return ['status', 'application_portal']


class ApplicationTrackingInline(TabularInline):
    model = ApplicationTracking
    extra = 0
    classes = ['collapse']
    exclude = ["program_url", ]
    can_delete = False
    show_change_link = True

    def get_ordering(self, request):
        return (
            Case(
                When(status=ApplicationStatus.ACCEPTED, then=Value(1)),
                When(status=ApplicationStatus.IN_PROGRESS, then=Value(2)),
                When(status=ApplicationStatus.NOT_STARTED, then=Value(3)),
                default=Value(5),
            ),
        )


@admin.register(University)
class UniversityAdmin(ModelAdmin):
    list_filter = ('status',)
    list_display = ('name', 'status', 'display_applied_programs',)
    inlines = [ApplicationTrackingInline]
    show_facets = admin.ShowFacets.ALWAYS

    def get_ordering(self, request):
        return (
            Case(
                When(
                    status=University.Status.WAITING_FOR_APPLICATION,
                    start_time__lte=timezone.now().date(),
                    then=Value(0)
                ),
                When(status=University.Status.NOT_CHECKED, then=Value(1)),
                When(status=University.Status.WAITING_FOR_APPLICATION, then=Value(2)),
                When(status=University.Status.PARTIALLY_CHECKED, then=Value(3)),
                When(status=University.Status.UNI_ASSIST, then=Value(4)),
                When(status=University.Status.FULLY_CHECKED, then=Value(5)),
                default=Value(5),
            ),
            # Secondary ordering by start time for WAITING status
            'start_time',
            'name'  # Finally order by name if all else is equal
        )

    # display count of applied programs
    @admin.display(description='Applied Programs')
    def display_applied_programs(self, obj):
        return obj.applications.count()
