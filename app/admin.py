from django.contrib import admin

from app.models import UniversityProgram


@admin.register(UniversityProgram)
class UniversityProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'degree', 'teaching_language', 'program_duration', 'beginning')
    search_fields = ('name', 'university', 'description', 'degree', 'teaching_language')
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name', 'university', 'degree', 'teaching_language', 'languages', 'full_time_part_time',
                'program_duration', 'beginning'
            )
        }),
        ('Application and Fees', {
            'fields': ('application_deadline', 'tuition_fees', 'academic_requirements', 'language_requirements',
                       'submit_application_to')
        }),
        ('Program Details', {
            'fields': ('description', 'course_organisation', 'diploma_supplement', 'international_elements',
                       'german_language_courses', 'english_language_courses')
        }),
        ('Additional Information', {
            'fields': (
                'combined_phd', 'joint_degree', 'semester_contribution', 'costs_of_living',
                'funding_opportunities', 'part_time_employment', 'accommodation', 'career_advisory_service',
                'support_for_international_students', 'supervisor_student_ratio'
            )
        }),
        ('University Information', {
            'fields': ('about_university',)
        }),
    )
