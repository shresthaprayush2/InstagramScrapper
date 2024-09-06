# InstagramScrapper
This project is a Python-based web scraper that uses Selenium to extract restaurant-related details, such as location and parking space information, from food blogger posts on Instagram. It's designed to automate the process of gathering useful data from public Instagram accounts, saving time and effort.

Features

    Login to Instagram: Automates the process of logging into an Instagram account.
    Scrape Post Details: Extracts descriptions from Instagram posts containing keywords like "Location" or "Parking Space."
    Optimized for Speed: Uses headless browsing and disables unnecessary elements to improve performance.
    Handles Dynamic Content: Scrolls through the Instagram page to load more posts and fetch details dynamically.

Setup and Installation
Requirements

    Python 3.x
    Selenium
    Google Chrome and ChromeDriver

  Running the Scraper

    Open the scraper.py file.
    Modify the following variables with your Instagram account credentials and the Instagram handle you wish to scrape:


username = 'your_username'
password = 'your_password'
usernameToCrawl = 'food.lovers.nepal'

Run the script:

bash

    python scraper.py

Note:

    Ensure that the Instagram account you're scraping from is public.
    Scraping large datasets from Instagram might result in rate limiting or temporary IP blocks.

