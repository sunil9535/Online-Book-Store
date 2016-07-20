'''
Created on 17-Mar-2016

@author: parkar_s
'''
from bookstore.src.models.core.business.category import Category
from bookstore.src.models.core.business.tree import Tree


class CategoryService(object):
    '''
    classdocs
    '''

    categoryTree = Tree(Category('root', 0))

    def __init__(self):
        pass

    def getCategoriesById(self, data):
        return self.categoryTree.getAllChildren(Category(data[1], data[0]))

    def constructTree(self, categoryData):
        for cat in categoryData:
            if cat['subcategory'] != None:

                parent = Category(cat['main_category'], cat['cat_id'])
                child = Category(cat['subcategory'], cat['subcategory_id'])

            self.categoryTree.add(child, parent)
        return self.categoryTree

    def prepare_categories(self, raw_categories):
        return self.constructTree(raw_categories)
        categories = list()
        for item in list(filter(lambda x: x['subcategory'] is not None, raw_categories)):
            found = False
            for cat in categories:
                if cat['id'] == item['cat_id']:
                    cat['submenu'].append(
                        {"name": item['subcategory'], "id": item['subcategory_id']})
                    found = True
                    break
            if not found:
                categories.append({"name": item['main_category'], "id": item['cat_id'], "submenu": [
                                  {"name": item['subcategory'], "id":item['subcategory_id']}]})
        return categories
