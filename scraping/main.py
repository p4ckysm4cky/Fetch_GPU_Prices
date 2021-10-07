import requests
from bs4 import BeautifulSoup

def pbtech_scrape(url_array):
    """
    Takes in an array of url's and returns an array of tuples containing
    Name and Price for each pbtech item in the url.
    """
    pbtech_items = []
    for url in url_array:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # finding item names
        item_names = soup.find_all("div", class_="item_short_name")
        # finding item prices
        prices = soup.find_all("span", class_="price_full")
        # this needs to be done, because there are multiple prices:
        # odd index = GST included, even index = GST not included
        prices_formatted = [prices[i] for i in range(len(prices)) if i % 2 != 0]
        for i in range(len(item_names)):
            item_name = (item_names[i].span.text).split(",")[0]
            price = prices_formatted[i].text
            pbtech_items.append((item_name, price))
        return pbtech_items


# url = "https://www.pbtech.co.nz/category/components/video-cards/nvidia-desktop-graphics-cards?o=lowest_price"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')
# nvidia_gpus = soup.find_all("div", class_="item_short_name")

# prices = soup.find_all("span", class_="price_full")
# prices_formatted = [prices[i] for i in range(len(prices)) if i % 2 != 0]

# for i in range(len(nvidia_gpus)):
#     gpu_name = (nvidia_gpus[i].span.text).split(",")[0]
#     # print(f"{(nvidia_gpus[i].span.text).split(",")[0] :30} {prices_formatted[i].text}")
#     print(f"{gpu_name:80}| {prices_formatted[i].text}")
if __name__ == "__main__":
    url = ["https://www.pbtech.co.nz/category/components/video-cards/nvidia-desktop-graphics-cards?o=lowest_price"]
    gpu_array = pbtech_scrape(url)
    print(gpu_array)