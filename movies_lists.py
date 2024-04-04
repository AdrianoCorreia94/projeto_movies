import requests
from abc import abstractmethod, ABC
import os
from dotenv import load_dotenv
import json


class Movies(ABC):
    def __init__(self, lang: str, page: int) -> None:
        self.url_base = 'https://api.themoviedb.org/3/movie/'
        self.key = self._getKey()
        self.lang = lang
        self.page = page

    def _getKey(self) -> str:
        load_dotenv()
        return os.getenv('key_api')

    @abstractmethod
    def _getEndpoint(self) -> str:
        pass

    def getData(self):
        headers = {"accept": "application/json"}
        response = requests.get(self._getEndpoint(), headers=headers)
        print(response.text)
        return response.json()

    def saves(self, local: str):
        self.local = local
        data = self.getData()
        with open(self.local, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)


class now_playing(Movies):
    def _getEndpoint(self) -> str:
        type = 'now_playing'
        return f'{self.url_base}{type}?api_key={self.key}&language={self.lang}&page={self.page}'


class popular(Movies):
    def _getEndpoint(self) -> str:
        return f'{self.url_base}popular?api_key={self.key}&language={self.lang}&page={self.page}'


class top_rated(Movies):
    def _getEndpoint(self) -> str:
        return f'{self.url_base}top_rated?api_key={self.key}&language={self.lang}&page={self.page}'


class upComing(Movies):
    def _getEndpoint(self) -> str:
        return f'{self.url_base}upcoming?api_key={self.key}&language={self.lang}&page={self.page}'


populares = now_playing(lang='pt', page=198).saves('datalake/pagina198.json')


'''
for x in range(1, 5):
    pop = now_playing(lang='pt', page=x).getData()
    with open('testeAppend.json', 'a') as file:
        json.dump(pop, file, indent=4)

j# with open('datalake/popular.json', 'w', encoding='utf-8') as file:
#    json.dump(populares, file, indent=4)
'''
