# Apkpure Scraper
This Scraper will scrap apps data from apkpure website given a link to a particular category and will save the data in a json file. This Scraper Works as of 2021.

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![pythonbadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This scraper will extract data about each app or game: 

- **Category of the app**

- **Icon URL of the app**

- **Name of the app**

- **Publisher Name**

- **Download Link**

- **Any Video and Images URL**

- **Text Description**

## Getting started
Just copy any category link of apps or games from apkpure website and past it in the scraper.

Specify the number of pages you want to scrap from within that category. Each page has 20 apps.

You will have to have little patience when using the scraper. It does not just scrap all apps instantly. It takes 1 
and half minute for the scraper to scrap each page(20 apps) from the website. Therefore, this means if you are going to 
scrap 100 app's info from a particular category, it will take almost 10 minutes for the scraper to scrap the information 
of 100 apps.

When you run the scraper it will open up a browser window (You will have to have Chrome browser installed on your 
PC to run the scraper). Window will be minimized, you do not have to look at the chrome window just keep it running in
background. It will go to every app in that category and scrap the every info we require and save the info into json file
at the end.

# How to Run 
Executable script is provided in the attachment. You just have to run the executable file in order to run the scraper.

Source code file is provided as well. If you want to have a look at the code you can open script.py file. But to run 
it you will have to have python and dependencies (requirements.txt file) installed.

- Clone the repository
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/Source/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
-  Past the link to a particular category of apps and specify the number of pages you wanna get apps upto (each page has 20 apps).

## Contact

For any feedback or queries, please reach out to me at [suwaidaslam@gmail.com](suwaidaslam@gmail.com).
