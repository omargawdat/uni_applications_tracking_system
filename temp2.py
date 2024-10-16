import requests


def get_program_links(api_url):
    response = requests.get(api_url)
    data = response.json()

    links = []
    base_url = "https://www2.daad.de"

    for course in data.get('courses', []):
        link = base_url + course.get('link', '')
        links.append(link)

    return links


def main():
    api_url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/api/solr/en/search.json?cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&degree%5B%5D=2&fos=6&langDeAvailable=&langEnAvailable=&fee=3&bgn%5B%5D=2&sort=4&dur=&subjects%5B%5D=49&q=&limit=200&offset=&display=grid&isElearning=&isSep="

    program_links = get_program_links(api_url)

    print(f"Total links found: {len(program_links)}")
    for link in program_links:
        print(link)


if __name__ == "__main__":
    main()