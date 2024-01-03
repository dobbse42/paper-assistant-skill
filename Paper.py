import nltk
nltk.download('punkt')

#from gtts import gTTS
import pypdf
#import arxiv_handler
from nltk.tokenize import sent_tokenize
from io import BytesIO
#import pygame
import new_arxiv_handler

class Paper:

  def __init__(self, id):
    print("init")
    self.page_starts = []
    self.language = 'en'
    self.link = 'placeholder'
    self.name = 'placeholder'
    self.arxiv_id = id

    self.pdf_data = new_arxiv_handler.get_pdf(new_arxiv_handler.get_feed(self.arxiv_id))
    self.processed_sents = self.process_pdf(self.pdf_data)

#    self.filepath = arxiv_handler.get_arxiv(self.arxiv_id)
#    self.processed_sents = self.process_pdf_file(self.filepath)

#    self.filepath = arxiv_handler.get_pdf(self.link)
#    self.processed_sents = process_text(self.raw_text)
    return

# Note: This does not handle sentences which begin on one page and end on the next. In that case the current behavior
#  is to split into two sentences, one part for each page.
  def process_pdf_file(self, filepath):
    path = open(filepath, 'rb')
    pdfReader = pypdf.PdfReader(path)
    texts = []
    text = ''
    sents = []
    for page in pdfReader.pages:
      texts.append(page.extract_text())
    for page in texts:
      self.page_starts.append(len(sents))
      sents = sents + self.process_text(page)
    return sents

  def process_pdf(self, pdf_data):
    with BytesIO(pdf_data) as open_pdf_file:
      pdfReader = pypdf.PdfReader(open_pdf_file)
      texts = []
      text = ''
      sents = []
      for page in pdfReader.pages:
        texts.append(page.extract_text())
      for page in texts:
        self.page_starts.append(len(sents))
        sents = sents + self.process_text(page)
      return sents

  def process_text(self, text):
    text = text.replace('-\n', '') # handles word interrupt hyphens
    text = text.replace('\n', '') # remove newlines
    sents = sent_tokenize(text)
    return sents

