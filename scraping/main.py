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
        # finding name of items
        item_names = soup.find_all("div", class_="item_short_name")
        # finding price of items
        prices = soup.find_all("span", class_="price_full")
        # this needs to be done, because there are multiple prices:
        # odd index = GST included, even index = GST not included
        prices_formatted = [prices[i]
                            for i in range(len(prices)) if i % 2 != 0]
        for i in range(len(item_names)):
            item_name = (item_names[i].span.text).split(",")[0]
            price = prices_formatted[i].text
            pbtech_items.append((item_name, price))
    return pbtech_items


def print_items(item_array):
    """
    Takes in an array of (item_name, price) tuple
    and prints a formatted text of the item. 
    """
    for name, price in item_array:
        if len(name) > 70:
            name = name[:70] + "..."
        print(f"{name:80}| {price}")


def select_items(item_array, *args):
    """
    Takes in an array of (item_name, price) tuple
    and modifies the array to select any item that contains
    one of the strings from *args.
    """
    if len(args) == 0:
        return
    for index, item in reversed(list(enumerate(item_array))):
        name = item[0]
        do_remove = True
        for search in args:
            if search.lower() in name.lower():
                do_remove = False
        if do_remove:
            item_array.pop(index)


def filter_items(item_array, *args):
    """
    Takes in an array of (item_name, price) tuple
    and modifies the array so item_name must contain
    all the strings in *args.
    """
    if len(args) == 0:
        return
    for index, item in reversed(list(enumerate(item_array))):
        name = item[0]
        for search in args:
            if search.lower() not in name.lower():
                item_array.pop(index)
                break


def display_items(*args):
    """
    *args takes in arrays of (item_name, price) tuple
    and displays the results formatted to the user
    """
    print("="*120)
    for item in args:
        print_items(item)


def main():
    pbtech_gpu_url = ["https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=1#sort_group_form",
                      "https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=2#sort_group_form",
                      "https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=3#sort_group_form",
                      "https://www.pbtech.co.nz/category/components/video-cards/shop-all?o=lowest_price&pg=4#sort_group_form"]
    pbtech_gpu_array = pbtech_scrape(pbtech_gpu_url)
    filter_items(pbtech_gpu_array, "asus", "3080", "strix")
    display_items(pbtech_gpu_array)


if __name__ == "__main__":
    main()
