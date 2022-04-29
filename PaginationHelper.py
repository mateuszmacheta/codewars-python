# 5 kyu PaginationHelper
# https://www.codewars.com/kata/515bb423de843ea99400000a/train/python

import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        print(f'col: {collection} items {items_per_page}')
        self.collection = collection
        self.items_per_page = items_per_page
        self.total_pages = math.ceil(len(collection)/items_per_page)
        pass

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return self.total_pages

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.total_pages - 1:
            return -1
        if page_index == self.total_pages - 1:
            return len(self.collection) % self.items_per_page
        return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        print(f'page_index() item_index: {item_index}')
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        return (item_index // self.items_per_page)

collection = range(1,25)
helper = PaginationHelper(collection, 10)

print(helper.page_index(0))