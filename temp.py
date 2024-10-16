import requests
from bs4 import BeautifulSoup


class ProgramScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.content_div = None

    def fetch_page(self):
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.content, 'html.parser')
        self.content_div = self.soup.find('div', class_='js-detail-course')
        if not self.content_div:
            raise ValueError("Main content div not found. The page structure might have changed.")

    def get_info(self, label):
        dt = self.content_div.find('dt', class_='c-description-list__content',
                                   string=lambda text: label in text if text else False)
        if dt:
            dd = dt.find_next('dd', class_='c-description-list__content')
            return dd.get_text(strip=True) if dd else None
        return None

    def get_university_info(self):
        university_tab = self.soup.find('div', {'id': 'university', 'role': 'tabpanel'})
        if university_tab:
            # Get the main content
            content = university_tab.find('div', class_='c-profile__content')
            main_info = ' '.join(p.text.strip() for p in content.find_all('p')) if content else ''

            # Get the location information
            location_header = university_tab.find('h3',
                                                  string=lambda text: 'University location' in text if text else False)
            location_content = location_header.find_next('div',
                                                         class_='c-profile__content') if location_header else None
            location_info = ' '.join(p.text.strip() for p in location_content.find_all('p')) if location_content else ''

            # Combine main info and location info
            return f"{main_info}\n\nUniversity location:\n{location_info}"
        return None

    def scrape_program_info(self):
        self.fetch_page()

        return {
            'name': self.soup.find('h2', class_='c-detail-header__title').text.strip(),
            'university': self.soup.find('h3', class_='c-detail-header__subtitle').text.strip(),
            'degree': self.get_info('Degree'),
            'teaching_language': self.get_info('Teaching language'),
            'languages': self.get_info('Languages'),
            'full_time_part_time': self.get_info('Full-time / part-time'),
            'program_duration': self.get_info('Programme duration'),
            'beginning': self.get_info('Beginning'),
            'application_deadline': self.get_info('Application deadline'),
            'tuition_fees': self.get_info('Tuition fees per semester in EUR'),
            'combined_phd': self.get_info("Combined Master's degree / PhD programme"),
            'joint_degree': self.get_info('Joint degree / double degree programme'),
            'description': self.get_info('Description/content'),
            'course_organisation': self.get_info('Course organisation'),
            'diploma_supplement': self.get_info('A Diploma supplement will be issued'),
            'international_elements': self.get_info('International elements'),
            'german_language_courses': self.get_info('Course-specific, integrated German language courses'),
            'english_language_courses': self.get_info('Course-specific, integrated English language courses'),
            'semester_contribution': self.get_info('Semester contribution'),
            'costs_of_living': self.get_info('Costs of living'),
            'funding_opportunities': self.get_info('Funding opportunities within the university'),
            'academic_requirements': self.get_info('Academic admission requirements'),
            'language_requirements': self.get_info('Language requirements'),
            'submit_application_to': self.get_info('Submit application to'),
            'part_time_employment': self.get_info('Possibility of finding part-time employment'),
            'accommodation': self.get_info('Accommodation'),
            'career_advisory_service': self.get_info('Career advisory service'),
            'support_for_international_students': self.get_info('Support for international students'),
            'supervisor_student_ratio': self.get_info('Supervisor-student ratio'),
            'about_university': self.get_university_info()
        }


def main():
    url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4238/"
    scraper = ProgramScraper(url)

    try:
        program_info = scraper.scrape_program_info()
        print("Program Information:")
        for key, value in program_info.items():
            print(f"{key}:")
            print(value)
            print("-" * 50)
    except Exception as e:
        print(f"Failed to scrape program information: {str(e)}")


if __name__ == "__main__":
    main()
