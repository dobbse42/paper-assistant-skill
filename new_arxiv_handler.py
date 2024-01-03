import requests
import feedparser

def example_request(url):
  data = requests.get(url)
  return data.text

def get_feed(id):
  url = 'http://export.arxiv.org/api/query?id_list=' + str(id)
  data = requests.get(url)
  return data.text

def get_pdf(my_xml):
  feed = feedparser.parse(my_xml)
  for link in feed['entries'][0]['links']:
    if link['rel'] == 'related' and link['title'] == 'pdf':
      pdf_url = link['href']
  pdf = requests.get(pdf_url)
  return pdf.content


# url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
# data = example_request(url)
# get_pdf(data)
