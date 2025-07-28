import requests
from bs4 import BeautifulSoup
from lxml import html
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ewz():
    url = "https://br.investing.com/etfs/ishares-msci-brazil-capped-etf"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        valor = soup.find('span', {'data-test': 'instrument-price-last'}).text.strip()
        percentual = soup.find('span', {'data-test': 'instrument-price-change-percent'}).text.strip()
        return valor, percentual
    except Exception as e:
        return None, None

def get_ewz_xpath():
    url = "https://br.investing.com/etfs/ishares-brazil-index"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.content)
    valor = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/text()")
    percentual = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/span[2]/text()")
    if percentual:
        perc = ''.join(percentual).replace('Variação:', '').strip()
    else:
        perc = None
    return (valor[0].strip() if valor else None, perc)

def get_vxbr_xpath():
    url = "https://br.investing.com/indices/s-p-b3-ibovespa-vix"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.content)
    valor = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/text()")
    percentual = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/span[2]/text()")
    if percentual:
        perc = ''.join(percentual).replace('Variação:', '').strip()
    else:
        perc = None
    return (valor[0].strip() if valor else None, perc)

def get_petax_xpath():
    import requests
    from lxml import html
    url = "https://br.investing.com/funds/pimco-real-estate-real-return-straa"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.content)
    valor = tree.xpath("/html/body/div[7]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/text()")
    percentual = tree.xpath("/html/body/div[7]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[4]/text()")
    val = valor[0].strip() if valor else None
    perc = percentual[0].strip() if percentual else None
    return (val, perc)

def get_eua2_xpath():
    import requests
    from lxml import html
    url = "https://br.investing.com/rates-bonds/u.s.-2-year-bond-yield"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.content)
    valor = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/text()")
    spans = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]//span/text()")
    percentual = spans[0].strip().replace('(', '').replace(')', '') if spans else None
    val = valor[0].strip() if valor else None
    return (val, percentual)

def get_eua5_xpath():
    import requests
    from lxml import html
    url = "https://br.investing.com/rates-bonds/u.s.-5-year-bond-yield"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.content)
    valor = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/text()")
    spans = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]//span/text()")
    percentual = (spans[0].strip() + spans[1].strip()).replace('(', '').replace(')', '') if len(spans) > 1 else (spans[0].strip().replace('(', '').replace(')', '') if spans else None)
    val = valor[0].strip() if valor else None
    return (val, percentual)

def get_eua10_xpath():
    import requests
    from lxml import html
    url = "https://br.investing.com/rates-bonds/u.s.-10-year-bond-yield"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.content)
    valor = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/text()")
    spans = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]//span/text()")
    percentual = (spans[0].strip() + spans[1].strip()).replace('(', '').replace(')', '') if len(spans) > 1 else (spans[0].strip().replace('(', '').replace(')', '') if spans else None)
    val = valor[0].strip() if valor else None
    return (val, percentual)

def get_eua30_xpath():
    import requests
    from lxml import html
    url = "https://br.investing.com/rates-bonds/u.s.-30-year-bond-yield"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.content)
    valor = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/text()")
    spans = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]//span/text()")
    percentual = (spans[0].strip() + spans[1].strip()).replace('(', '').replace(')', '') if len(spans) > 1 else (spans[0].strip().replace('(', '').replace(')', '') if spans else None)
    val = valor[0].strip() if valor else None
    return (val, percentual)

def monitorar():
    while True:
        clear()
        print("Monitoramento Online - EWZ e VXBR (Investing.com)\n")
        ewz_valor, ewz_perc = get_ewz_xpath()
        vxbr_valor, vxbr_perc = get_vxbr_xpath()

        if ewz_valor and ewz_perc:
            print(f"EWZ  - Valor: {ewz_valor} | Variação: {ewz_perc}")
        else:
            print("EWZ  - Não foi possível obter os dados.")

        if vxbr_valor and vxbr_perc:
            print(f"VXBR - Valor: {vxbr_valor} | Variação: {vxbr_perc}")
        else:
            print("VXBR - Não foi possível obter os dados.")

        print("\nAtualizando em 30 segundos...")
        time.sleep(30)

if __name__ == "__main__":
    monitorar()
