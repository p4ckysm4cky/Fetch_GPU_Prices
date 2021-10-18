# Fetch_GPU_Price

This tool allows you to scrape graphics card prices of popular PC part retailers in NZ, so that you can quickly see the pricing of certain GPU models. 



## Supported retailers

* [PBtech](https://www.pbtech.co.nz/)
* [ComputerLounge](https://www.computerlounge.co.nz/)



## Installation

* Clone the repository

```
git clone https://github.com/p4ckysm4cky/Fetch_GPU_Prices.git
```

* Installing required python packages

```
pip install -r ./requirements.txt
```



## Usage example

### All prices

If we wanted to get all the GPU prices we can run it without passing any arguments:

```
python ./scraping/main.py
```

### Specific GPU and brand

If we're interested in finding 3080's made by ASUS and EVGA we can pass in some arguments:

```
python ./scraping/main.py -s "evga asus" -f "3080"
```

Here's the output:

```
Fetching data from PBtech...
Fetching data from ComputerLounge...
========================================================================================================================
ASUS TUF GeForce RTX 3080 V2 LHR 10GB GDDR6X                                               $2,199.00    PBtech         |
ASUS TUF GeForce RTX 3080 OC V2 LHR 10GB GDDR6X                                            $2,249.00    PBtech         |
ASUS ROG STRIX GeForce RTX 3080 OC V2 10G Gaming LHR 10GB GDDR6X                           $2,369.00    PBtech         |
ASUS ROG STRIX GeForce RTX 3080 V2 OC 10G Gaming WHITE LHR 10GB GDDR6X                     $2,398.99    PBtech         |
ASUS GeForce RTX 3080 ROG Strix OC 10GB V2 Graphics Card                                   $2,499.00    ComputerLounge |
ASUS GeForce RTX 3080 TUF Gaming OC V2 10GB Graphics Card                                  $2,499.00    ComputerLounge |
ASUS GeForce RTX 3080 ROG Strix White OC V2 Graphics Card                                  $2,599.00    ComputerLounge |
EVGA GeForce RTX 3080 Ti FTW3 Ultra Gaming Graphics Card 12GB GDDR6X                       $2,698.99    PBtech         |
ASUS TUF OC GeForce RTX 3080 Ti 12GB GDDR6X                                                $2,799.00    PBtech         |
------------------------------------------------------------------------------------------------------------------------
```



## Things to add

- [x] Save output as `.csv`
- [ ] Add more retailers
- [ ] Fetch GPU stock info
- [ ] Fix docstrings
- [ ] Clean up `main()` so it's less cluttered

* [ ] Find alternative for PBtech hardcoded pages