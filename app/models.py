from django.db import models



class UniversityProgram(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    teaching_language = models.CharField(max_length=100)
    languages = models.TextField(blank=True)
    full_time_part_time = models.CharField(max_length=100)
    program_duration = models.CharField(max_length=100)
    beginning = models.CharField(max_length=100)
    application_deadline = models.TextField()
    tuition_fees = models.CharField(max_length=100)
    combined_phd = models.CharField(max_length=100)
    joint_degree = models.CharField(max_length=100)
    description = models.TextField()
    course_organisation = models.TextField(blank=True)
    diploma_supplement = models.CharField(max_length=100, blank=True)
    international_elements = models.TextField(blank=True)
    german_language_courses = models.CharField(max_length=100, blank=True)
    english_language_courses = models.CharField(max_length=100, blank=True)
    semester_contribution = models.TextField(blank=True)
    costs_of_living = models.TextField(blank=True)
    funding_opportunities = models.TextField(blank=True)
    academic_requirements = models.TextField()
    language_requirements = models.TextField()
    submit_application_to = models.TextField()
    part_time_employment = models.TextField(blank=True)
    accommodation = models.TextField(blank=True)
    career_advisory_service = models.TextField(blank=True)
    support_for_international_students = models.TextField(blank=True)
    supervisor_student_ratio = models.CharField(max_length=100, blank=True)
    about_university = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.university}"