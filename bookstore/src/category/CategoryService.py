'''
Created on 17-Mar-2016

@author: parkar_s
'''

class CategoryService(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def prepare_categories(self, raw_categories):
        categories= list()
        for item in list(filter(lambda x:x['subcategory'] is not None,raw_categories )):
            found = False
            for cat in categories:
                if cat['id'] == item['cat_id']:
                    cat['submenu'].append({"name":item['subcategory'], "id":item['subcategory_id']})
                    found = True
                    break
            if not found :categories.append({"name":item['main_category'],"id":item['cat_id'], "submenu": [{"name":item['subcategory'],"id":item['subcategory_id']}]})
        return categories        
            