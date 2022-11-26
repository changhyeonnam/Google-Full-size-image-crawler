# Google Full size image crawler
This repo is for crawling full size image in the google search.

### Development Environment
- WEB : Chrome Version 106.0.5249.91 (Official Build) (x86_64)
- OS : MAC
- IDE : Pycharm

### Dependency
```
selenium == 4.4.3
```
### How to use crawler
1. Download suitable chrome driver. <p>Follow this [link](https://chromedriver.chromium.org/downloads).</p>
2. You should specify PATH in `webdriver.Chrome()`
   ```python
    PATH="./chromedriver"
    driver = webdriver.Chrome(executable_path=PATH)
    ```
3. You should specify full size image xpath in chorme.
   1. Do search
   ![img.png](img/img.png)
   2. Go to inspect, and click upper left mouse icon.
   ![img_1.png](img/img_1.png)
   3. click full size image, and go to inspect.
   ![img_2.png](img/img_2.png)
   4. copy xpath.
   ![img_3.png](img/img_3.png)

4. replace copied xpath with copied variable.
   ```python
    copied_xpath='//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img'
   ```
5. Run the code!. <p>Follow command like this.</p>
   ```python
   python main.py
   
   Please enter a search term: jordon white white
   Enter the total number: 50
   ```

### Example
```python
Please enter a search term: pikachu
Enter the total number: 5
**************************************************Crawlling started.**************************************************
Image saved: pikachu_1.jpg
Image saved: pikachu_2.jpg
Image saved: pikachu_3.jpg
Image saved: pikachu_4.jpg
Image saved: pikachu_5.jpg
**************************************************Crawlling Completed.**************************************************
```

### Output 
![pikachu.png](pikachu/pikachu_1.png)

### Info
- I'm not sure but copied xpath can be reused for different search term.
- I guess that when chrome is updated or google updated their search engine, we should copy again.
