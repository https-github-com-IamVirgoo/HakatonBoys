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
        output = []
        for elm in data:
            output.append(
                {
                    "nm": elm['Наименование'],
                    "am": elm['Объем заказа'],
                    "pr": int(str(elm['Цена, руб']).split(',')[0])
                }
            )
        
        return {
            'eur': int(str(euroActual).split('.')[0]),
            'usd': int(str(dollarActual).split('.')[0]),
            'ctn': output
        }