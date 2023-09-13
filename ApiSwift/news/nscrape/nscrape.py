import requests
from bs4 import BeautifulSoup


class Nscrape:

    BASE_URL = 'https://www.graphic.com.gh/'


    CATEGORIES = {
        'news':'news.html',
        'politics': 'politics.html',
        'showbiz': 'entertainment.html',
        'sports': 'sports.html',
        'business': 'business.html',
        'lifestyle': 'lifestyle.html'
    }

    
    def __init__(self, category):
        if category not in Nscrape.CATEGORIES:
            raise ValueError('Invalid category')
        else:
            self.category_url = Nscrape.BASE_URL + Nscrape.CATEGORIES[category]

    
    def make_soup(self):
        try:
            content = requests.get(self.category_url).text
        except:
            raise 'Network Error'
        return BeautifulSoup(content, 'html.parser')
    
    def _extract_content(self):
        data = []
        soup = self.make_soup().find_all('tr')
        for id, each in enumerate(soup):
            _element_dict = {
                'id':id,
                'content':each.get_text(strip=True)
            }
            data.append(_element_dict)

        return data
        

    def _extract_cardlike_pages(self):
        results_list = []
        content_soup = self.make_soup()
        try:
            divs = content_soup.find('div', class_='com-content-category-card mb-4').find_all('h3')
        except:
            raise ConnectionError

        for id, each in enumerate(divs):
            each_dict = {
                "id": id,
                "content": each.a.get_text(strip=True)
            }
            results_list.append(each_dict)
        
        return results_list

    def get_news(self):
        if not self._extract_content():
            return self._extract_cardlike_pages()
        else:
            return self._extract_content()

x = Nscrape('genz')
print(x.get_news())