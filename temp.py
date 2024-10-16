import time

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
        if not university_tab:
            return None

        content = university_tab.find('div', class_='c-profile__content')
        main_info = ' '.join(p.text.strip() for p in content.find_all('p')) if content else ''

        location_header = university_tab.find('h3',
                                              string=lambda text: 'University location' in text if text else False)
        location_content = location_header.find_next('div', class_='c-profile__content') if location_header else None
        location_info = ' '.join(p.text.strip() for p in location_content.find_all('p')) if location_content else ''

        return f"{main_info}\n\nUniversity location:\n{location_info}"

    def scrape_program_info(self):
        self.fetch_page()
        info_fields = [
            'Degree', 'Teaching language', 'Languages', 'Full-time / part-time', 'Programme duration',
            'Beginning', 'Application deadline', 'Tuition fees per semester in EUR',
            "Combined Master's degree / PhD programme", 'Joint degree / double degree programme',
            'Description/content', 'Course organisation', 'A Diploma supplement will be issued',
            'International elements', 'Course-specific, integrated German language courses',
            'Course-specific, integrated English language courses', 'Semester contribution',
            'Costs of living', 'Funding opportunities within the university', 'Academic admission requirements',
            'Language requirements', 'Submit application to', 'Possibility of finding part-time employment',
            'Accommodation', 'Career advisory service', 'Support for international students',
            'Supervisor-student ratio'
        ]

        program_info = {field.lower().replace(' ', '_').replace('/', '_'): self.get_info(field) for field in
                        info_fields}
        program_info.update({
            'name': self.soup.find('h2', class_='c-detail-header__title').text.strip(),
            'university': self.soup.find('h3', class_='c-detail-header__subtitle').text.strip(),
            'about_university': self.get_university_info()
        })
        return program_info


def get_program_links(api_url):
    response = requests.get(api_url)
    data = response.json()
    base_url = "https://www2.daad.de"
    return [f"{base_url}{course.get('link', '')}" for course in data.get('courses', [])]


def scrape_all_programs(api_url):
    program_links = get_program_links(api_url)
    all_program_info = []

    for i, link in enumerate(program_links, 1):
        print(f"Scraping program {i}/{len(program_links)}: {link}")
        scraper = ProgramScraper(link)
        try:
            program_info = scraper.scrape_program_info()
            all_program_info.append(program_info)
        except Exception as e:
            print(f"Failed to scrape program information: {str(e)}")
        time.sleep(1)  # Be polite to the server

    return all_program_info


def main():
    api_url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/api/solr/en/search.json?cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&degree%5B%5D=2&fos=6&langDeAvailable=&langEnAvailable=&fee=3&bgn%5B%5D=2&sort=4&dur=&subjects%5B%5D=49&q=&limit=3&offset=&display=grid&isElearning=&isSep="
    return {"universities": scrape_all_programs(api_url)}


if __name__ == "__main__":
    result = main()
    print(f"Total programs scraped: {len(result['universities'])}")
    print(result['universities'])
