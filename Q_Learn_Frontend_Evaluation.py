import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import cv2

class ImageSimilarityChecker:
    def __init__(self, threshold=0.7):
        self.threshold = threshold
        self.orb = cv2.ORB_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        self.width = 224  
        self.height = 224  

    def compare_images(self, image_path1, image_path2):
        image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
        image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

        image1_resized = cv2.resize(image1, (self.width, self.height))
        image2_resized = cv2.resize(image2, (self.width, self.height))

        keypoints1, descriptors1 = self.orb.detectAndCompute(image1_resized, None)
        keypoints2, descriptors2 = self.orb.detectAndCompute(image2_resized, None)

        matches = self.bf.match(descriptors1, descriptors2)
        similarity_score = len(matches) / max(len(keypoints1), len(keypoints2))

        similarity_percentage = similarity_score * 100

        if similarity_score >= self.threshold:
            result = "Images are similar"
        else:
            result = "Images are dissimilar"
        
        return result, similarity_percentage

def take_website_screenshot(html_file, chrome_driver_path):
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

    # Start the WebDriver service
    service = Service(chrome_driver_path)
    service.start()

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Load the HTML file
    driver.get("file://" + html_file)

    # Wait for a few seconds to ensure that all content is loaded
    time.sleep(5)

    # Take a screenshot of the webpage
    driver.save_screenshot("website_screenshot.png")

    # Close the browser
    driver.quit()

    # Stop the WebDriver service
    service.stop()

if __name__ == "__main__":
    # Path to your HTML file
    html_file = "index.html"

    # Path to your Chrome driver executable
    chrome_driver_path = "chromedriver.exe"  # Change this path based on your system

    # Take website screenshot
    take_website_screenshot(html_file, chrome_driver_path)

    # Compare screenshots
    similarity_checker = ImageSimilarityChecker(threshold=0.7)
    result, similarity_percentage = similarity_checker.compare_images("website_screenshot.png", "goal_image.png")
    print(result)
    print("Similarity Score (100%):", similarity_percentage)