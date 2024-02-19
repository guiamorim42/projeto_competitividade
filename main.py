import requests
from bs4 import BeautifulSoup

def get_price_from_mercado_livre(url):
    # Fazendo solicitação GET para a página do produto
    response = requests.get(url)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Parseando o HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrando a tag meta com itemprop="price"
        price_meta_tag = soup.find('meta', itemprop='price')
        
        # Verificando se a tag foi encontrada
        if price_meta_tag:
            # Obtendo o conteúdo do atributo content que contém o preço
            price = price_meta_tag.get('content')
            return price
        else:
            return 'Preço não encontrado.'
    else:
        return 'Erro ao obter a página: ' + str(response.status_code)

# Exemplo de uso
url = "https://produto.mercadolivre.com.br/MLB-3540274439"
price = get_price_from_mercado_livre(url)
print('O preço do produto é:', price)
