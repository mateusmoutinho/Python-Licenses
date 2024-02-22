import hashlib
import os
from datetime import datetime
import base64
from typing import Union
import  pickle
class Licenses:
    def __init__(self,root_secret:str):
        self.root_secret = root_secret
       


    def convert_sha256(self, texto):
        sha256 = hashlib.sha256()
        sha256.update(texto.encode('utf-8'))
        hash_resultado = sha256.hexdigest()
        return hash_resultado

    def create_license(self, license_key:str, expiration_date:str) -> str:
        
        license_hash = self.convert_sha256(license_key)
        generated_code = self.convert_sha256(license_hash + expiration_date + self.root_secret)
        data = {
            'hash':license_hash,
            'generated_code': generated_code,
            'expiration':expiration_date
        }
        transformed_in_bytes = pickle.dumps(data)
        
        return base64.encodebytes(transformed_in_bytes).decode('utf-8')

        


    def check_license(self, license_key:str,now:Union[str,datetime]=None) -> bool:
        reconverted = base64.decodebytes(license_key.encode('utf-8'))
        retransformed  = pickle.loads(reconverted)
        INVALID_FORMATATION = False 
        INVALID_KEY = False 
        EXPIRED_KEY = False
        VALID = True

        required_keys = ['hash','expiration','generated_code']
        for key in required_keys:
            value = retransformed.get(key)
            if value.__class__ != str:
                return INVALID_FORMATATION
        
            
        hash = str(retransformed['hash'])
        expiration = str(retransformed['expiration'])
        generated_code = str(retransformed['generated_code'])

        expected_code = self.convert_sha256(hash + expiration + self.root_secret)

        if generated_code !=expected_code:
            return INVALID_KEY

        expiration_date = datetime.strptime(expiration, '%Y-%m-%d')
        
        if now:
            if now.__class__ == str:
                now = datetime.strptime(now, '%Y-%m-%d')
        if not now:
            now = datetime.now()
        
        if expiration_date > now:
                return VALID
        
        return EXPIRED_KEY
        