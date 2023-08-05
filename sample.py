from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    # Replace "chromedriver_path" with the actual path to your downloaded ChromeDriver
    driver = webdriver.Chrome(executable_path="C://browserdrivers/chromedriver.exe")

    try:
        # Open the website
        driver.get("https://www.example.com")  # Replace with the URL of the website you want to automate

        # Wait for the page to load (you can adjust the waiting time based on your website's loading speed)
        time.sleep(5)

        # Find and interact with elements on the page
        search_box = driver.find_element_by_name("q")  # Replace "q" with the name of the search box on your website
        search_box.send_keys("Python automation with Selenium")
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to load
        time.sleep(5)

        # Perform more interactions as needed...

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser when done
        driver.quit()

if __name__ == "__main__":
    main()
