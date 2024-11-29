import requests
from bs4 import BeautifulSoup


def main():
    url = "https://mebel-v-koroleve.ru/stulya_i_taburetyi"
    response = requests.get(url)
    print(response.status_code)
    #print(response.text)


    soup = BeautifulSoup(response.text, 'html.parser')
    spoon = soup.find("div", class_="products-list__body")
    print([i.text for i in spoon])

    with open('page.txt', 'a', encoding='UTF-8') as file:
        file.write(''.join([i.text for i in spoon]))

    #soup = BeautifulSoup(response.text, 'html.parser') 
    #part = soup.find('div', class_='text-container')
    #with open('page.txt', 'a', encoding='UTF-8') as file:
        #file.write(part.text)

#    with open('output.html', 'a', encoding='UTF-8') as file:
#        file.write(response.text)


if __name__ == "__main__":
    main()