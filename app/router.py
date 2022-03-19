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
                    "pr": str(elm['Цена, руб'])[0:6]
                }
            )
        
        return {
            'eur':euroActual,
            'usd':dollarActual,
            'ctn': output
        }