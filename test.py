import requests

TOKEN = 'b12405d016c00cd60967bf8d'


class CurrencyConverter:
    def __init__(self, token, currency = None, url = None):
        self.token = token
        self._currency = currency
        self._url = url
        
        
    @property
    def url(self) -> str:
        if not self._url:
            self._url = f'https://v6.exchangerate-api.com/v6/{self.token}/latest/{self.currency}'
        return self._url
    @property
    
    def currency(self):
        if not self._currency:
            self._currency = input('number value value').split()
        return self._currency[1]
    

    
    
#10000 pln usd
    def convert(self):   
        response = requests.get(self.url)
        data = response.json()
        print("Exchange Rates:")
        for rate in data['conversion_rates']:
            if self._currency[0] == rate:
                print(f"1 {self._currency[1]} its {data['conversion_rates'][rate]} {rate} ")

if __name__ == '__main__':
    try:        
        while True:
            converter = CurrencyConverter(token= TOKEN)
            converter.convert()
                
    except Exception as e:
        print(f'Closing')
