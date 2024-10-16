from django.core.management.base import BaseCommand

from app.models import UniversityProgram
from temp import scrape_all_programs


class Command(BaseCommand):
    help = 'Scrapes university program data and saves it to the database'

    def handle(self, *args, **options):
        api_url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/api/solr/en/search.json?cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&degree%5B%5D=2&fos=6&langDeAvailable=&langEnAvailable=&fee=3&bgn%5B%5D=2&sort=4&dur=&subjects%5B%5D=49&q=&limit=200&offset=&display=grid&isElearning=&isSep="

        programs = scrape_all_programs(api_url)

        for program in programs:
            UniversityProgram.objects.update_or_create(
                name=program['name'],
                university=program['university'],
                defaults={
                    'degree': program.get('degree', ''),
                    'teaching_language': program.get('teaching_language', ''),
                    'languages': program.get('languages', ''),
                    'full_time_part_time': program.get('full_time_part_time', ''),
                    'program_duration': program.get('program_duration', ''),
                    'beginning': program.get('beginning', ''),
                    'application_deadline': program.get('application_deadline', ''),
                    'tuition_fees': program.get('tuition_fees', ''),
                    'combined_phd': program.get('combined_phd', ''),
                    'joint_degree': program.get('joint_degree', ''),
                    'description': program.get('description', ''),
                    'course_organisation': program.get('course_organisation', ''),
                    'diploma_supplement': program.get('diploma_supplement', ''),
                    'international_elements': program.get('international_elements', ''),
                    'german_language_courses': program.get('german_language_courses', ''),
                    'english_language_courses': program.get('english_language_courses', ''),
                    'semester_contribution': program.get('semester_contribution', ''),
                    'costs_of_living': program.get('costs_of_living', ''),
                    'funding_opportunities': program.get('funding_opportunities', ''),
                    'academic_requirements': program.get('academic_requirements', ''),
                    'language_requirements': program.get('language_requirements', ''),
                    'submit_application_to': program.get('submit_application_to', ''),
                    'part_time_employment': program.get('part_time_employment', ''),
                    'accommodation': program.get('accommodation', ''),
                    'career_advisory_service': program.get('career_advisory_service', ''),
                    'support_for_international_students': program.get('support_for_international_students', ''),
                    'supervisor_student_ratio': program.get('supervisor_student_ratio', ''),
                    'about_university': program.get('about_university', ''),
                }
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully scraped and saved {len(programs)} programs'))
