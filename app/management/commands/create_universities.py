from django.core.management.base import BaseCommand
from django.db import transaction
from app.models import UniversityProgram, University


class Command(BaseCommand):
    help = 'Creates University objects from existing UniversityProgram entries'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Run the command without creating universities',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']

        # Get all unique university names from UniversityProgram
        unique_universities = UniversityProgram.objects.values_list(
            'university', flat=True).distinct()

        self.stdout.write(f"Found {len(unique_universities)} unique universities")

        if dry_run:
            self.stdout.write("Dry run - no universities will be created")
            for uni_name in unique_universities:
                if uni_name:
                    self.stdout.write(f"Would create university: {uni_name}")
            return

        universities_created = 0
        universities_existing = 0

        with transaction.atomic():
            for uni_name in unique_universities:
                if uni_name:  # Check if university name is not empty
                    university, created = University.objects.get_or_create(
                        name=uni_name,
                    )

                    if created:
                        universities_created += 1
                        self.stdout.write(
                            self.style.SUCCESS(f"Created university: {university.name}")
                        )
                    else:
                        universities_existing += 1
                        self.stdout.write(
                            self.style.WARNING(f"University already exists: {university.name}")
                        )

        # Print summary
        self.stdout.write("\nSummary:")
        self.stdout.write(f"Total unique universities found: {len(unique_universities)}")
        self.stdout.write(f"Universities created: {universities_created}")
        self.stdout.write(f"Universities already existing: {universities_existing}")