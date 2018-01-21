from tqdm import tqdm
import requests

chunk_size = 1024

url = 'http://file.allitebooks.com/20170728/Data%20Science%20with%20Java%20Practical%20Methods%20for%20Scientists%20and%20Engineers.pdf'

r = requests.get(url, stream=True)
total_size = int(r.headers['content-length'])

with open('pdffile.pdf', 'wb') as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=total_size//chunk_size, unit='KB'):
        f.write(data)

print("Download completed !!")
