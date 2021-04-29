import json


def json_reader(file):
    with open(file) as f:
        links = json.load(f)
    return links


class Itercountries:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            txt_writer(input_file, output_file, counter=self.counter)
            self.counter += 1
        except IndexError:
            raise StopIteration


def txt_writer(input_file, output_file, counter):
    with open(output_file, 'a+', encoding='utf-8') as output:
        country = input_file[counter]['name']['official'].replace(' ', '_').replace(',', '')
        output.write(f'{country}: {wiki_link}{country}\n')


input_file = json_reader('countries.json')
output_file = 'countries_new.txt'
wiki_link = 'https://en.wikipedia.org/wiki/'
wiki_countries = Itercountries()
countries_list = [c for c in wiki_countries]




