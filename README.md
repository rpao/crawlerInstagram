# crawlerInstagram

IF818 - ANÁLISE E MINERAÇÃO DE REDES COMPLEXAS - Projeto 2018.1

DEPENDENCIAS:
  - python3 or python27, scrapy, selenium, pypiwin32

  OBS: 
  instalação scrapy: pip install scrapy
  instalação selenium: pip install selenium
  instalação pypiwin32: pip install pypiwin32
  
  Crie a pasta "data" dentro da pasta "instagramcrawler2" e crie o arquivo "data.json" contendo:
{
    "USERNAME"  :   "your_user_name",
    "PASSWORD"  :   "your password"
}

EXECUTAR SPIDER:
  scrapy crawl instaspider

ESTRUTURA DO PROJETO:
	crawlerInstagram
	|	README.md
	|	instagramcrawler2
	|	|	debug.txt
	|	|	geckodriver
	|	|	scrapy.cfg
	|	|	data
	|	|	|	data.json
	|	|	instagramcrawler
	|	|	|	__init__.py
	|	|	|	items.py
	|	|	|	pipelines.py
	|	|	|	settings.py
	|	|	|	__pycache__
	|	|	|	spiders
	|	|	|	|	__init__
	|	|	|	|	instaspider
	|	|	|	|	seleniumscraper
	|	|	|	|	__pycache__
