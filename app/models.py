from django.db import models


class UniversityProgram(models.Model):
    # Overview
    link = models.URLField(max_length=500, null=True, blank=True, help_text="URL of the program")
    university = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    teaching_language = models.CharField(max_length=100, null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    program_duration = models.CharField(max_length=100, null=True, blank=True)
    beginning = models.CharField(max_length=100, null=True, blank=True)
    combined_phd = models.CharField(max_length=100, null=True, blank=True)
    joint_degree = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)

    # Details
    course_organisation = models.TextField(null=True, blank=True)
    diploma_supplement = models.CharField(max_length=100, null=True, blank=True)
    international_elements = models.TextField(null=True, blank=True)
    german_language_courses = models.CharField(max_length=100, null=True, blank=True)
    english_language_courses = models.CharField(max_length=100, null=True, blank=True)
    about_university = models.TextField(null=True, blank=True)
    full_time_part_time = models.CharField(max_length=100, null=True, blank=True)
    supervisor_student_ratio = models.CharField(max_length=100, null=True, blank=True)

    # Cost
    tuition_fees = models.CharField(max_length=100, null=True, blank=True)
    costs_of_living = models.TextField(null=True, blank=True)
    semester_contribution = models.TextField(null=True, blank=True)
    funding_opportunities = models.TextField(null=True, blank=True)

    # Requirements
    academic_requirements = models.TextField(null=True, blank=True)
    language_requirements = models.TextField(null=True, blank=True)
    application_deadline = models.TextField(null=True, blank=True)
    submit_application_to = models.TextField(null=True, blank=True)

    # services
    part_time_employment = models.TextField(null=True, blank=True)
    accommodation = models.TextField(null=True, blank=True)
    career_advisory_service = models.TextField(null=True, blank=True)
    support_for_international_students = models.TextField(null=True, blank=True)

    # track
    is_checked = models.BooleanField(default=False, help_text="Have you reviewed this program?")
    STATUS_CHOICES = [
        ('not_checked', 'Not Checked'),
        ('checked', 'Checked'),
        ('insufficient', 'Insufficient Requirements')
    ]
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='not_checked',
        help_text="Status of program review"
    )
    personal_note = models.TextField(null=True, blank=True, help_text="Your personal notes about this program")
    ielts_score = models.FloatField(
        choices=[
            (5.5, '5.5'), (6.0, '6.0'), (6.5, '6.5'),
            (7.0, '7.0'), (7.5, '7.5'), (8.0, '8.0'),
            (8.5, '8.5'), (9.0, '9.0')
        ],
        null=True,
        blank=True,
        help_text="Required IELTS score for this program"
    )

    gpa_score = models.FloatField(
        null=True,
        blank=True,
        help_text="Required GPA score (0-4 scale)"
    )

    def __str__(self):
        return f"{self.name} at {self.university}"

    class Meta:
        ordering = ['university', 'name']


class ApplicationStatus(models.TextChoices):
    NOT_STARTED = 'NS', 'Not Started'
    IN_PROGRESS = 'IP', 'In Progress'
    REQUIREMENTS_BARELY_MET = 'RM', 'Requirements Barely Met'
    ACCEPTED = 'AC', 'Accepted'
    REJECTED = 'RE', 'Rejected'
    STATUS_CHANGE = 'SC', 'Status Change'


class University(models.Model):
    class Status(models.TextChoices):
        FULLY_CHECKED = 'fully_checked', 'Fully Checked'
        PARTIALLY_CHECKED = 'partially_checked', 'Partially Checked'
        NOT_CHECKED = 'not_checked', 'Not Checked'
        WAITING_FOR_APPLICATION = 'waiting_for_application', 'Waiting for Application Time'
        UNI_ASSIST = 'UA', 'Uni Assist Needed'

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.NOT_CHECKED
    )
    name = models.CharField(max_length=255)
    portal_url = models.URLField(max_length=500, null=True, blank=True)
    portal_user_name = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(blank=True)
    start_time = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ApplicationTracking(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='applications',
        null=True,
    )
    status = models.CharField(
        max_length=2,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.NOT_STARTED,
    )

    field = models.CharField(
        max_length=30,
        choices=[
            ('AI', 'Artificial Intelligence'),
            ('CS', 'Computer Science'),
            ('IS', 'Information Systems'),
            ('CYB', 'Cyber Security'),
            ('DS', 'Data Science'),
            ('AUTO', "Autonomy"),
            ('Medical Imaging', 'Medical Imaging'),
            ('bioinformatics', 'Bioinformatics'),
            ('mathematics', 'Mathematics'),
            ('EMBEDDED', 'Embedded Systems'),
        ],
        null=True,
        help_text="Main field of study"
    )
    application_submission_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    program_url = models.URLField(max_length=500, null=True, blank=True)
