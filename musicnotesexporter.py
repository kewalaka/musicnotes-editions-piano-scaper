import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode, unquote

def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to retrieve page: {url}")
        return None

def extract_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    result_rows = soup.find_all('tr', class_='result-row')

    data_list = []

    for row in result_rows:
        data_block = row.find('div', {'style': 'display:none'})
        title = data_block['data-prod-title'].strip()
        artist = data_block['data-prod-artist'].strip()
        scoring = data_block['data-prod-scoring'].strip()
        instruments = data_block['data-prod-instruments'].strip()
        music_key = data_block['data-prod-key'].strip()

        # Extract and decode the URL parameter
        url = unquote(data_block['data-prod-url'].split('url=')[-1])

        # find the rating div and extract the rating from the image url
        rating_div = row.find('div', id=lambda x: x and x.startswith('modal-info-rating-'))
        if rating_div is not None:
            rating_img = rating_div.find('img')
            if rating_img is not None:
                rating_img_url = rating_img['src']
                rating = int(rating_img_url.split('/')[-1].replace('.gif', '')) / 10
            else:
                rating = None
        else:
            rating = None

        data_list.append([title, artist, scoring, instruments, music_key, url, rating])

    return data_list

def write_to_csv(data_list, filename='output.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write header
        csv_writer.writerow(['Title', 'Artist', 'Scoring', 'Instruments', 'Key', 'URL', 'Rating'])

        # Write data
        csv_writer.writerows(data_list)

def main():
    base_url = "https://www.musicnotes.com/search/go?"
    parameters = {
        'p': 'Q',
        'srid': 'S1-8SYD-AWSP',
        'lbc': 'musicnotes',
        'ts': 'custom-v2',
        'w': '*',
        'uid': '862253951',
        'method': 'and',
        'af': 'inst2:keyboard_piano inst1:keyboard producttype:lilnotemned',
        'isort': 'globalpop',
        'view': 'list',
        'srt': 0
    }

    data_list = []
    i = 0
    items_per_page = 30

    while True:
        parameters['srt'] = i
        query_string = urlencode(parameters)
        full_url = f"{base_url}{query_string}"
        page_content = get_page_content(full_url)

        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            no_results_tag = soup.find('div', class_='sli_bold sli_heading', string='No Results')

            if no_results_tag:
                print("No Results found. Exiting.")
                break

            data_list += extract_data(page_content)
            print(f"Finished page {int(i/items_per_page)}, we now have {len(data_list)} items.")
            i += items_per_page
        else:
            print(f"Failed to retrieve page {i}. Exiting.")
            break

    write_to_csv(data_list, filename='music-notes-output.csv')

if __name__ == "__main__":
    main()