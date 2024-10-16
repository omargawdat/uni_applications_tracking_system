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
    is_checked = models.BooleanField(default=False, help_text="Have you reviewed this program?")
    is_sufficient = models.BooleanField(default=True, help_text="Does this program meet your requirements?")
    personal_note = models.TextField(blank=True, help_text="Your personal notes about this program")
    application_start_date = models.DateField(
        null=True,
        blank=True,
        help_text="The date when the application process opens"
    )
    application_end_date = models.DateField(
        null=True,
        blank=True,
        help_text="The final deadline for submitting the application"
    )

    # New fields as requested
    IELTS_SCORES = [
        (5.5, '5.5'), (6.0, '6.0'), (6.5, '6.5'),
        (7.0, '7.0'), (7.5, '7.5'), (8.0, '8.0'),
        (8.5, '8.5'), (9.0, '9.0')
    ]
    ielts_score = models.FloatField(
        choices=IELTS_SCORES,
        null=True,
        blank=True,
        help_text="Required IELTS score for this program"
    )

    gpa_score = models.FloatField(
        null=True,
        blank=True,
        help_text="Required GPA score (0-4 scale)"
    )

    FIELD_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('CS', 'Computer Science'),
        ('CYB', 'Cyber Security'),
        ('DS', 'Data Science')
    ]
    field = models.CharField(
        max_length=3,
        choices=FIELD_CHOICES,
        help_text="Main field of study",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} at {self.university}"

    class Meta:
        ordering = ['university', 'name']


class ApplicationStatus(models.TextChoices):
    NOT_STARTED = 'NS', 'Not Started'
    IN_PROGRESS = 'IP', 'In Progress'
    SUBMITTED = 'SU', 'Submitted'
    UNDER_REVIEW = 'UR', 'Under Review'
    ACCEPTED = 'AC', 'Accepted'
    REJECTED = 'RE', 'Rejected'
    WAITLISTED = 'WL', 'Waitlisted'


class ApplicationTracking(models.Model):
    university_program = models.OneToOneField(UniversityProgram, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.NOT_STARTED,
    )
    application_submission_date = models.DateField(null=True, blank=True)
    decision_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    priority = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"Application for {self.university_program.name}"

    class Meta:
        ordering = ['priority',]
