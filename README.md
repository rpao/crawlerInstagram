# crawlerInstagram

IF818 - ANÁLISE E MINERAÇÃO DE REDES COMPLEXAS - Projeto 2018.1

Dependencias:
  - python3 or python27, scrapy, selenium, pypiwin32

  OBS: 
  instalação scrapy: pip install scrapy
  instalação selenium: pip install selenium
  instalação pypiwin32: pip install pypiwin32

Usage - executar spider:
  scrapy crawl instaspider
  
Also, the crawler instaspider.py requires a path to json file. The JSON format is:

{
    "USERNAME"  :   "your_user_name",
    "PASSWORD"  :   "your password"
}
