from bs4 import BeautifulSoup
import time
from selenium import webdriver
import json
from tqdm import tqdm


def chrome():
    # support to get response status and headers
    d = webdriver.DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_experimental_option("useAutomationExtension", False)
    opt.add_argument("--disable-extensions")
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--start-maximized")
    opt.add_argument("--disable-gpu")
    opt.add_argument('--window-size=1920x1200')
    opt.add_argument("--proxy-server='direct://'")
    opt.add_argument("--proxy-bypass-list=*")
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_argument("--ignore-certificate-errors")
    browser = webdriver.Chrome(executable_path=r'driver/chromedriver.exe', options=opt,desired_capabilities=d)
    browser.implicitly_wait(5)
    return browser


# returns chrome object
browser = chrome()
browser.minimize_window()

# a particular category
url = str(input("Enter the URL to a Particular category of apps: "))

# Set this to load more apps pages (each page has 20 apps)
load_more_times = int(input("\nEnter number of pages upto you wanna extract the data (each page has 20 apps): "))
browser.get(url)

src = browser.page_source
soup = BeautifulSoup(src, 'lxml')
data = []
apps_count = 0


for load_more in tqdm(range(load_more_times), desc= "Overall Progress"):

    category_template = soup.find('ul', {'class': 'category-template'})
    load_button_link = soup.find('a', {'class' : 'loadmore'})['href']
    all_apps = category_template.find_all('li')

    for app in tqdm(all_apps, desc= "Per Page Progress"):
        try:
            app_page_link = app.find('a')['href']
            app_page_link = 'https://apkpure.com'+app_page_link
            browser.get(app_page_link)
            time.sleep(2)
            appInfo_src = browser.page_source
            app_page = BeautifulSoup(appInfo_src, 'lxml')

            info_box = app_page.find('div', {'class' : 'box'})
            # -------------------------------Section 1-----------------------------------
            # to get category
            category_tag = info_box.find('div', {'class': 'title bread-crumbs'})
            all_categories = category_tag.find_all('a')
            category = ''
            for categ in all_categories:
                cat = categ.get_text().strip()
                if cat != '':
                    category += cat
                    category += ' ->'
            # print(category)
            # -------------------------------Section 2-----------------------------------
            # to get icon url of app
            icon_section = info_box.find('dt')
            icon_url_tag = icon_section.find('div', {'class': 'icon'})
            icon_url = icon_url_tag.find('img')['srcset']
            # print(icon_url)

            # to get name of app
            name_link_section = info_box.find('dd')

            name = name_link_section.find('div', {'class': 'title-like'}).get_text().strip()
            # print(name)

            # to get publisher name
            publisher_name = name_link_section.find('div', {'details-author'}).get_text().strip()
            # print(publisher_name)

            # to get download link of the app
            download_link_section = name_link_section.find('div', {'class': 'ny-down'})
            downloadLink_box = download_link_section.find('div', {'class': 'div-box'})
            downloadLink = downloadLink_box.find('a')['href']
            downloadLink = 'https://apkpure.com'+downloadLink
            # print(downloadLink)
            # -------------------------------Section 3-----------------------------------
            # Description of the App
            description_section = info_box.find('div', {'class': 'describe'})
            # Video and Pictures
            video_pic_links = []
            video_pictures_section = description_section.find('ul', {'class' : 'pa det-pic-list'})
            links_tag = video_pictures_section.find_all('a')
            for link_tag in links_tag:
                try:
                    video = link_tag['data-src']
                    video_pic_links.append(video)
                    # print(video)
                except:
                    picture = link_tag['href']
                    video_pic_links.append(picture)
                    # print(picture)

            text_description = description_section.find('div', {'class': 'description'}).get_text().strip()
            # print(text_description)

            application_description = {
            'Category' : category,
            'iconUrl' : icon_url,
            'AppName' : name,
            'PublisherName' : publisher_name,
            'DownloadLink' : downloadLink,
            'Video_And_Images_URL' : video_pic_links,
            'TextDescription' : text_description,
            }
            data.append(application_description)
            apps_count+=1
        except:
            continue
    
    outputs = []
    outputs.append(data)
    load_button_link = 'https://apkpure.com' + load_button_link
    browser.get(load_button_link)
    time.sleep(2)
    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')

print(f'{apps_count} apps has been scraped.')
with open("output.json", "w") as outfile:
    json.dump(outputs, outfile,  indent = 6)
browser.quit()
