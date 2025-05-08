from bs4 import BeautifulSoup
import requests

def get_operator_page(soup: BeautifulSoup):
    page = soup.find('a', class_="elementor-post__thumbnail__link")
    link = page['href']
    return link

def get_next_article(row: BeautifulSoup):
    yield row
    while True:
        next_line = row.find_next_sibling('article')
        assert next_line, 'No more operators'
        yield next_line

def get_weapon_name(link:str):
    head = 'https://arknightsendfield.gg/weapons/'
    weapon_name = link.removeprefix(head).removesuffix('/')
    if '-' in weapon_name:
        weapon_name = weapon_name.replace('-', '_')
    return weapon_name

def main_character_page(link: str, file):
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    rows: BeautifulSoup = soup.find_all('div', class_='elementor-widget-container')

    # Goes through contents in the character page then store on 'output.txt'
    for row in rows:
        text = row.text.strip()
        if text and len(text) > 2:
            file.write(text + "\n")

def main():
    res = requests.get('https://arknightsendfield.gg/')
    soup = BeautifulSoup(res.text, 'html.parser')
    rows: BeautifulSoup = soup.find_all('article')

    # Open the file in write mode
    with open('test.txt', 'w', encoding='utf-8') as file:
        # Goes through the list of characters
        for row in rows:
            article = next(get_next_article(row))
            new_page = get_operator_page(article)
            main_character_page(new_page, file)  # Pass file to save data

if __name__ == '__main__':
    main()
