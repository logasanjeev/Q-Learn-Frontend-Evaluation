# Q-Learn-Frontend-Evaluation

# Website Screenshot Capture:
* Utilizes Selenium to load a specified HTML file in a headless Chrome browser.
* Captures a screenshot of the loaded webpage.
* Saves the screenshot as "website_screenshot.png".

# Image Similarity Checking:
* Defines a class ImageSimilarityChecker to compare two images based on their similarity.
* Uses OpenCV to perform image comparison by resizing, extracting keypoints and descriptors, and calculating similarity score.
* Determines if the images are similar or dissimilar based on a predefined threshold.

# Integration:
* Combines both functionalities into a single script.
* Invokes take_website_screenshot function to capture the website screenshot.
* Invokes compare_images method of ImageSimilarityChecker to compare the captured website screenshot with a provided screenshot.
* Prints the result indicating whether the images are similar or dissimilar, along with the similarity percentage.

# Usage:
* Requires specifying the paths to the HTML file, Chrome driver executable, and the screenshot for comparison.
* The code automatically captures a screenshot of the specified webpage and compares it with the provided screenshot, providing the result and similarity score.

# Jupyter Notebook:
The Jupyter Notebook imports the functionalities from Q_Learn_Frontend_Evaluation.py and utilizes them to capture a screenshot of a webpage, compare it with a reference image ("goal_image.png"), and print the result. It dynamically determines the paths to the HTML file and Chrome driver executable based on the current working directory using the os.getcwd() function. This ensures that the paths are correctly constructed regardless of the directory from which the notebook is executed.

Overall, the code allows for automated website screenshot capture and comparison with another image to determine similarity, useful for various applications such as testing, monitoring, or content verification.
