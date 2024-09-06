#!/usr/bin/env python


class Product:
    def __init__(self, name, weight, categiry):
        self.name = name
        self.weight = weight
        self.categiry = categiry

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.categiry}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products()
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_products:
                    file.write(str(product) + '\n')
                else:
                    print(f'Product {product.name} is already in the store.')
