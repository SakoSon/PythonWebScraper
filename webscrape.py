from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.edge.service import Service

# Specify the path to the Microsoft Edge WebDriver executable
edge_driver_path = r"E:/MOD 3/CIS 403/Wk 17/msedgedriver.exe"

# Set up the Edge WebDriver with the correct executable path
service = Service(executable_path=edge_driver_path)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.get('https://oxylabs.io/blog')

results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

blog_posts = soup.find_all(attrs='css-16nzj3b e1qkxeay1')
for post in blog_posts:
    title = post.find(attrs='css-rmqaiq e1dscegp1').text
    date = post.find(attrs='css-weczbu e1ymydvc2').text
    if title and date and title not in results:
        results.append(title)
        other_results.append(date)

df = pd.DataFrame({'Blog Post Titles': results,
                   'Dates': other_results})
df.to_csv('blog_post_titles.csv', index=False, encoding='utf-8')