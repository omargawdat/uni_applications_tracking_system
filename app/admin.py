from django.contrib import admin
from unfold.admin import StackedInline, ModelAdmin

from .models import UniversityProgram, ApplicationTracking


class ApplicationTrackingInline(StackedInline):
    model = ApplicationTracking
    extra = 0
    fields = ('status', 'priority', 'application_submission_date', 'decision_date', 'notes')
    classes = ['collapse']


@admin.register(UniversityProgram)
class UniversityProgramAdmin(ModelAdmin):
    list_fullwidth = True
    list_horizontal_scrollbar_top = True
    compressed_fields = True

    list_display = (
        'name', 'university', 'field', 'degree', 'teaching_language', 'application_deadline_display',
        'is_checked',
        'is_sufficient', 'application_status')
    list_filter = ('field', 'degree', 'teaching_language', 'is_checked', 'is_sufficient', 'applicationtracking__status')
    search_fields = ('name', 'university', 'description', 'personal_note')
    inlines = [ApplicationTrackingInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('link', 'name', 'university', 'field', 'degree', 'teaching_language', 'languages',
                       'full_time_part_time', 'program_duration', 'beginning'),
            'classes': ['tab']
        }),
        ('Application Details', {
            'fields': ('application_start_date', 'application_end_date', 'application_deadline',
                       'tuition_fees', 'ielts_score', 'gpa_score'),
            'classes': ['tab']
        }),
        ('Requirements', {
            'fields': ('academic_requirements', 'language_requirements'),
            'classes': ['tab']
        }),
        ('Program Details', {
            'fields': ('description', 'course_organisation', 'international_elements'),
            'classes': ['tab']
        }),
        ('Language Courses', {
            'fields': ('german_language_courses', 'english_language_courses'),
            'classes': ['tab']
        }),
        ('Costs and Funding', {
            'fields': ('semester_contribution', 'costs_of_living', 'funding_opportunities'),
            'classes': ['tab']
        }),
        ('Personal Assessment', {
            'fields': ('is_checked', 'is_sufficient', 'personal_note'),
            'classes': ['tab']
        }),
        ('Additional Information', {
            'fields': ('combined_phd', 'joint_degree', 'diploma_supplement',
                       'part_time_employment', 'accommodation', 'career_advisory_service',
                       'support_for_international_students', 'supervisor_student_ratio',
                       'about_university', 'submit_application_to'),
            'classes': ['tab']
        }),
    )

    def application_deadline_display(self, obj):
        return f"{obj.application_start_date} - {obj.application_end_date}"

    application_deadline_display.short_description = "Application Period"

    def application_status(self, obj):
        try:
            return obj.applicationtracking.get_status_display()
        except ApplicationTracking.DoesNotExist:
            return "Not Started"

    application_status.short_description = "Application Status"


@admin.register(ApplicationTracking)
class ApplicationTrackingAdmin(ModelAdmin):
    list_fullwidth = True
    list_horizontal_scrollbar_top = True
    compressed_fields = True

    list_display = ('university_program', 'status', 'priority', 'application_submission_date', 'decision_date')
    list_filter = ('status', 'priority')
    search_fields = ('university_program__name', 'university_program__university', 'notes')

    fieldsets = (
        ('Program Information', {
            'fields': ('university_program',)
        }),
        ('Application Status', {
            'fields': ('status', 'priority', 'application_submission_date', 'decision_date')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('university_program',)
        return self.readonly_fields
