import pandas as pd
import concurrent.futures
from tqdm import tqdm
import wikipediaapi

def scrape_wikipedia(name_topic, verbose=True):

   def link_to_wikipedia(link):
       try:
           page = api_wikipedia.page(link)
           if page.exists():
               return {'page': link, 'text': page.text, 'link': page.fullurl, 'categories': list(page.categories.keys())}
       except:
           return None
      
   api_wikipedia = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
   name_of_page = api_wikipedia.page(name_topic)
   if not name_of_page.exists():
       print('Page {} is not present'.format(name_of_page))
       return
  
   links_to_page = list(name_of_page.links.keys())
   procceed = tqdm(desc='Scraped links', unit='', total=len(links_to_page)) if verbose else None
   origin = [{'page': name_topic, 'text': name_of_page.text, 'link': name_of_page.fullurl, 'categories': list(name_of_page.categories.keys())}]
  
   with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
       links_future = {executor.submit(link_to_wikipedia, link): link for link in links_to_page}
       for future in concurrent.futures.as_completed(links_future):
           info = future.result()
           origin.append(info) if info else None
           procceed.update(1) if verbose else None
   procceed.close() if verbose else None
  
   namespaces = ('Wikipedia', 'Special', 'Talk', 'LyricWiki', 'File', 'MediaWiki',
                 'Template', 'Help', 'User', 'Category talk', 'Portal talk')
   origin = pd.DataFrame(origin)
   origin = origin[(len(origin['text']) > 20)
                     & ~(origin['page'].str.startswith(namespaces, na=True))]
   origin['categories'] = origin.categories.apply(lambda a: [b[9:] for b in a])

   origin['topic'] = name_topic
   print('Scraped pages', len(origin))
  
   return origin

wiki_data = scrape_wikipedia("Covid 19")