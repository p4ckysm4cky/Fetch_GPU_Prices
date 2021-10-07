import requests
from bs4 import BeautifulSoup

url = "https://www.pbtech.co.nz/category/components/video-cards/nvidia-desktop-graphics-cards?o=lowest_price"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
nvidia_gpus = soup.find_all("div",class_="item_short_name")

prices = soup.find_all("span", class_="price_full")
prices_formatted = [prices[i] for i in range(len(prices)) if i % 2 != 0]

for i in range(len(nvidia_gpus)):
    gpu_name = (nvidia_gpus[i].span.text).split(",")[0]
    # print(f"{(nvidia_gpus[i].span.text).split(",")[0] :30} {prices_formatted[i].text}")
    print(f"{gpu_name:80}| {prices_formatted[i].text}")

