# This  file contains the url for websites
# that are to be scraped
import requests
from bs4 import BeautifulSoup


def generate_pbtech_gpu_url():
    print("Finding pages for PBTech...")
    page = requests.get("https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=1#sort_group_form")
    soup = BeautifulSoup(page.content, "html.parser")
    page_nums_scrape = soup.find(class_="pagination").find_all("b")
    max = None
    pbtech_gpu_url = []
    # Find max page when 24 items are displayed
    # on each page
    for page_num in page_nums_scrape:
        if page_num.text.isdigit():
            num = int(page_num.text)
            if max == None:
                max = num
            elif num > max:
                max = num
    for i in range(1, max+1):
        pbtech_gpu_url.append(f"https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg={i}#sort_group_form")
    return pbtech_gpu_url

# This is the hardcoded pbtech url, which is no longer used.
pbtech_gpu_url_hard = ["https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=1#sort_group_form",
                  "https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=2#sort_group_form",
                  "https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=3#sort_group_form",
                  "https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=4#sort_group_form"]

computerlounge_gpu_url = ["https://www.computerlounge.co.nz/shop/components/graphics-cards/desktop#!categoryId=470&page=1&q=&scid=-1&isListMode=false&lastPage=2&Filters%5B0%5D.Key=Sort&Filters%5B0%5D.Value=5",
                          "https://www.computerlounge.co.nz/shop/components/graphics-cards/amd-radeon#!categoryId=803&page=1&q=&scid=-1&isListMode=false&Filters%5B0%5D.Key=Sort&Filters%5B0%5D.Value=5"]
