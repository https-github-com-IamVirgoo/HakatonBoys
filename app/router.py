import os
import json
import codecs

from flask_restful import Resource


from .tools import *


class FilePoint(Resource):
    """ 
    #Endpoint:
    /api/v1/<string:file>
    #Methods
    - Get
    - Post (?)
    
    Provides endpoint for file transfering, especialy google sheets
    """
    
    
    # TODO: implement inteface which can understand what typeof file is 
    # provided
    def get(self, file: str):
        data = get_data(file)
        print(data[0])
        output = []
        for elm in data:
            output.append(
                {
                    "nm": elm['Наименование'],
                    "am": elm['Объем заказа'],
                    "pr": elm['Цена, руб']
                }
            )
        
        with open(f'file-{file}.json', 'x') as f:
            json.dump(elm, f)

        with codecs.open(f'file-{file}.json', 'r', 'utf-8') as f:
            output = json.load(f)
        
        os.remove(f'file-{file}.json')
        
        return {
            'eur':euroActual,
            'usd':dollarActual,
            'ctn': output
        }