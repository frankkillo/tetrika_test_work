# PLEASE INSTALL PACKAGES FROM requirements.txt 
import requests
from bs4 import BeautifulSoup


def get_animals_count():
    """
    Func return dict with the number of animals for each letter of the russian alphabet
    """
    PAGE = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
    data = {}
    stop = False

    while True:
        response = requests.get(PAGE)
        soup = BeautifulSoup(response.content, 'html.parser')

        animals = soup.find(id="mw-pages")
        next_page = soup.find_all(title="Категория:Животные по алфавиту")[-1].get('href')
        PAGE = "https://ru.wikipedia.org" + next_page

        for animal in animals.text.strip().split('\n')[3:]:
            if animal[:1] == 'A':
                stop = True
                break
            data[animal[:1]] = data.get(animal[:1], 0) + 1

            if animal[:1] == 'H':
                # Не переведенно название существа в Wiki
                # Helobdella nununununojensis - Двуглазая клепсина
                data['Д'] += 1
                del data['H']

        if stop:
            break
    
    return data


if __name__ == "__main__":
    get_animals_count()


