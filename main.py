import requests
from bs4 import BeautifulSoup

def get_amazon_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    page = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    
    # Encontrar o elemento que contém o preço
    price_element = soup.find('span', class_='a-offscreen') # Pode variar dependendo da estrutura da página

    
    if price_element is not None:
        return price_element.text.strip()
    else:
        return "Preço não encontrado"


# Exemplo de uso
amazon_url = "https://www.amazon.com.br/dp/B0C2RXH9BJ"
price = get_amazon_price(amazon_url)
print("Preço do produto na Amazon:", price)