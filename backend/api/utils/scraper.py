import time
from time import sleep
from random import randint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Locate elements on page and throw error if they do not exist
from selenium.common.exceptions import NoSuchElementException

# Starting/Stopping Driver: can specify ports or location but not remote access
from selenium.webdriver.chrome.service import Service as ChromeService


def find_jobs(job, location):
    # Allows you to cusotmize: ingonito mode, maximize window size, headless browser, disable certain features, etc
    option = webdriver.ChromeOptions()

    # Going undercover:
    option.add_argument("--incognito")

    # # Consider this if the application works and you know how it works for speed ups and rendering!

    # option.add_argument('--headless=chrome')

    # Define job and location search keywords
    job_search_keyword = ['Data+Scientist', 'Business+Analyst', 'Data+Engineer',
                          'Python+Developer', 'Full+Stack+Developer',
                          'Machine+Learning+Engineer']

    # Define Locations of Interest
    # location_search_keyword = ['New+York', 'California', 'Washington']

    # Finding location, position, radius=35 miles, sort by date and starting page
    pagination_url = 'https://ar.indeed.com/jobs?q={}&l={}&radius=35&filter=0&sort=date&start={}'

    # print(paginaton_url)
    start = time.time()

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=option)
    sleep(randint(2, 6))

    driver.get(pagination_url.format(job, location, 0))

    sleep(randint(2, 6))

    p = driver.find_element(
        By.CLASS_NAME, 'jobsearch-JobCountAndSortPane-jobCount').text

    # Max number of pages for this search! There is a caveat described soon
    max_iter_pgs = int(p.split(' ')[0])//15

    job_lst = []
    job_description_list_href = []
    salary_list = []

    for i in range(0, max_iter_pgs):
        driver.get(pagination_url.format(job, location, i*10))

        sleep(randint(2, 4))

        job_page = driver.find_element(By.ID, "mosaic-jobResults")
        jobs = job_page.find_elements(
            By.CLASS_NAME, "job_seen_beacon")  # return a list

        for jj in jobs:
            job_title = jj.find_element(By.CLASS_NAME, "jobTitle")

            try:
                date = jj.find_element(
                    By.CLASS_NAME, "myJobsState").get_attribute("innerText")
            except:
                date = jj.find_element(
                    By.CLASS_NAME, "date").get_attribute("innerText")
            job_lst.append({
                "title": job_title.get_attribute("innerText"),
                "job_url": job_title.find_element(By.CSS_SELECTOR, "a").get_attribute("href"),
                "job_id": job_title.find_element(By.CSS_SELECTOR, "a").get_attribute("id"),
                "company": jj.find_element(By.CLASS_NAME, "css-1x7z1ps.eu4oa1w0").get_attribute("innerText"),
                "location": jj.find_element(By.CLASS_NAME, "css-t4u72d.eu4oa1w0").get_attribute("innerText"),
                "date": date
            })

            # except NoSuchElementException:
            #     salary_list.append(None)

    #         # Click the job element to get the description
    #         job_title.click()

    #         # Help to load page so we can find and extract data
    #         sleep(randint(3, 5))

    #         try:
    #             job_description_list.append(driver.find_element(By.ID,"jobDescriptionText").text)

    #         except:

    #             job_description_list.append(None)

    driver.quit()

    end = time.time()

    print(end - start, 'seconds to complete action!')
    print('-----------------------')
    print('Max Iterable Pages for this search:', max_iter_pgs)

    return job_lst
