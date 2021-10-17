import requests
import argparse
import csv
from bs4 import BeautifulSoup
from source import pbtech_gpu_url, computerlounge_gpu_url


def pbtech_scrape(url_array):
    """
    Takes in an array of url's and returns an array of tuples containing
    Name and Price for each PBtech item in the url.
    """
    print("Fetching data from PBtech...")
    pbtech_items = []
    for url in url_array:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
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
            # converts string price to float price
            price = price_to_float(prices_formatted[i].text)
            pbtech_items.append((item_name, price, "PBtech"))
    return pbtech_items


def computerlounge_scrape(url_array):
    """
    Takes in an array of url's and returns an array of tuples containing
    Name and Price for each ComputerLounge item in the url.
    """
    computerlounge_items = []
    print("Fetching data from ComputerLounge...")
    for url in url_array:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        # finding name of items
        item_names = soup.find_all("p", class_="productName")
        # finding price of items
        prices = soup.find_all("div", class_="priceMain")
        prices_formatted = ["".join(prices[i].text.split())
                            for i in range(len(prices))]
        for i in range(len(item_names)):
            item_name = item_names[i].text
            # converts string price to float price
            price = price_to_float(prices_formatted[i])
            computerlounge_items.append((item_name, price, "ComputerLounge"))
    return computerlounge_items


def print_items(item_array):
    """
    Takes in an array of (item_name, price) tuple
    and prints a formatted text of the item. 
    """
    for name, price, retailer in item_array:
        if len(name) > 70:
            name = name[:70] + "..."
        price = f"${price:,.2f}"
        print(f"{name:80}\t{price:>12}\t{retailer:<15}|")


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
    print("-"*120)


def price_to_float(str_price):
    """
    Takes in the raw string price, and converts it to a float
    so that operations are easily able to be done to it
    """
    return float("".join(str_price.lstrip("$").split(",")))


def sort_by_price(item_array):
    """
    item_array takes in arrays of (item_name, price)
    and sorts them by price from lowest to largest
    """
    item_array.sort(key=lambda item: item[1])


def parse_main():
    """
    Function responsible for the option arguments provided when main.py
    is ran
    """
    parser = argparse.ArgumentParser(
        description="Fetches GPU prices from popular retailers")
    parser.add_argument("-f", "--filter", type=str, metavar="",
                        help="Finds item that contains all of the keywords provided")
    parser.add_argument("-s", "--select", type=str, metavar="",
                        help="Finds any item that contains any of the keywords provided")
    parser.add_argument("-r", "--retailer", type=str, metavar="",
                        help="Finds items that match with retailers passed into the string")
    main_args = parser.parse_args()
    return main_args


def prompt_save(item_array):
    """
    Saves the array of (item_name, price, retailer) into a csv file
    named by the user
    """
    is_save = None
    while is_save == None:
        is_save = input("Would you like to save Y / N: ")
        if is_save.lower() == 'y' or is_save.lower() == 'yes':
            is_save = True
        elif is_save.lower() == 'n' or is_save.lower == 'no':
            is_save = False
        else:
            print("Unknown input\n")
            is_save = None
    if is_save:
        filename = input(
            "Please enter the filename you would live to save your .csv as: ")
        with open(f"{filename}.csv", 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerow(("GPU Name", "Price", "Retailer"))
            for item in item_array:
                csv_writer.writerow(item)
            print(f"\nSaved as '{filename}.csv'")
    else:
        return


def main():
    main_args = parse_main()
    gpu_array = []
    if main_args.retailer != None:
        retailers_list = main_args.retailer.split()
        run_pbtech = False
        run_computerlounge = False
        for retail in retailers_list:
            if retail.lower() in "pbtech":
                run_pbtech = True
            elif retail.lower() in "computerlounge":
                run_computerlounge = True
        if run_pbtech:
            gpu_array.extend(pbtech_scrape(pbtech_gpu_url))
        if run_computerlounge:
            gpu_array.extend(computerlounge_scrape(computerlounge_gpu_url))
        if len(gpu_array) == 0:
            print("Unable to find store provided")
            return
    else:
        gpu_array.extend(pbtech_scrape(pbtech_gpu_url))
        gpu_array.extend(computerlounge_scrape(computerlounge_gpu_url))
    sort_by_price(gpu_array)
    if main_args.filter != None:
        try:
            filter_items(gpu_array, *main_args.filter.split())
        except Exception as error:
            print(f"An error occurred while filtering items:\n{error}")
    if main_args.select != None:
        try:
            select_items(gpu_array, *main_args.select.split())
        except Exception as error:
            print(f"An error occurred while selecting items:\n{error}")
    display_items(gpu_array)
    prompt_save(gpu_array)


if __name__ == "__main__":
    main()
