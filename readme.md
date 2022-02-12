# Fetch_GPU_Price

This tool allows you to scrape graphics card prices of popular PC part retailers in NZ, so that you can quickly see the pricing of certain GPU models. 



## Supported retailers

* [PBtech](https://www.pbtech.co.nz/)
* [ComputerLounge](https://www.computerlounge.co.nz/)
* [Mightyape](https://www.mightyape.co.nz/)



## Installation

* Clone the repository

```bash
git clone https://github.com/p4ckysm4cky/Fetch_GPU_Prices.git
```

* Installing required python packages

```bash
pip install -r ./requirements.txt
```

[Install ChromeDriver used in Selenium](https://chromedriver.chromium.org/)

## Usage example

### All prices

If we wanted to get all the GPU prices we can run it without passing any arguments:

```bash
python ./scraping/main.py
```

### Specific GPU and brand

If we're interested in finding 3080's made by ASUS and EVGA we can pass in some arguments:

```bash
python ./scraping/main.py -s "evga asus" -f "3070"
```

Here's the output:

```
Finding pages for PBTech...
Fetching data from PBTech...
Fetching data from ComputerLounge...
Finding pages for Mightyape...
Fetching data from Mightyape...
========================================================================================================================
ASUS GeForce RTX 3070 Dual OC V2 8GB Graphics Card                                         $1,599.00    ComputerLounge |
EVGA GeForce RTX 3070 FTW3 Ultra LHR Graphics Card 8GB GDDR6                               $1,649.00    PBtech         |
ASUS GeForce RTX 3070 TUF Gaming OC V2 8GB Graphics Card                                   $1,649.00    ComputerLounge |
ASUS GeForce RTX 3070 KO V2 8GB Graphics Card                                              $1,649.00    ComputerLounge |
ASUS GeForce RTX 3070 KO OC V2 8GB Graphics Card                                           $1,669.00    ComputerLounge |
EVGA GeForce RTX 3070 Ti XC3 Ultra Gaming Graphics Card 8GB GDDR6X                         $1,699.00    PBtech         |
ASUS GeForce RTX 3070 Ti TUF Gaming OC 8GB Graphics Card                                   $1,699.00    ComputerLounge |
ASUS GeForce RTX 3070 OC NOCTUA Edition LHR                                                $1,748.99    PBtech         |
EVGA GeForce RTX 3070 Ti FTW3 Ultra Gaming Graphics Card 8GB GDDR6X                        $1,748.99    PBtech         |
ASUS GeForce RTX 3070 Noctua Edition OC 8GB Graphics Card                                  $1,749.00    ComputerLounge |
ASUS TUF GeForce RTX 3070 Ti OC 8GB GDDR6X                                                 $1,798.99    PBtech         |
ASUS ROG STRIX GeForce RTX 3070 Ti OC 8GB GDDR6X                                           $1,848.99    PBtech         |
ASUS GeForce RTX 3070 Ti ROG Strix OC 8GB Graphics Card                                    $1,849.00    ComputerLounge |
ASUS GeForce RTX 3070 ROG Strix OC V2 8GB Graphics Card                                    $1,849.00    ComputerLounge |
ASUS TUF Gaming GeForce RTX 3070 Ti OC Edition 8GB GPU                                     $1,995.00    Mightyape      |
------------------------------------------------------------------------------------------------------------------------
Would you like to save output as .csv Y / N: 
```



## Things to add

- [x] Save output as `.csv`
- [x] Add more retailers
- [ ] Fetch GPU stock info
- [x] Fix docstrings
- [x] Clean up `main()` so it's less cluttered
- [x] Find alternative for PBtech hardcoded pages
- [x] Find a way to scrape webpages rendered with js (Computer Lounge)