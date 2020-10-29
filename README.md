# CZ4045-Natural-Languae-Processing

Python Version - 3.7 is used throughout our project
Download or Clone the repository before running any file


# Task 3.1 Domain Specific Dataset Analysis

# Web Scraping for Domain 1 Analysis - Scrape StackOverflow Questions
Scrapy is an efficient framework to crawl websites which uses a spider to crawl through websites. 
Firstly, we install scrapy. 
```bash
   $ pip install scrapy
```
We then create a scrapy project directory.
```bash
$ scrapy startproject stack
$ cd stack
```
Then, a scrapy field is created to act as a placeholder for the scraped data. This is done in stack/items.py
```python
# items.py
import scrapy
class StackItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    question = scrapy.Field()
    pass
```
The script Assignment_1_3.1_WebScraping.py is the python script used to scrape from the website. This file is created as stack/spiders/stackoverflow.py
The results are stored in csv file which is done by modifying stack/settings.py
```python
# settings.py
FEED_FORMAT="csv"
FEED_URI="./domain1_dataset.csv"
```
Finally, To scrawl the data, we scrawl 'dataset' as we name out class dataset as seen in Assignment_1_3.1_WebScraping.py
```bash
$ scrapy crawl dataset
```
The results of scraping is shown in domain1_dataset.csv


# Domain Specific Dataset Analysis
The requirements required for 3.1 are shown below. 
```bash
   $ pip install numpy
   $ pip install pandas
   $ pip install nltk
   $ pip install matplotlib
```
The Domain Specifc Analysis for Stack Overflow Domain is in Assignment_1_3.1_D1.ipynb, Medical Papers Domain is in Assignment_1_3.1_D2.ipynb and 3D Printers Domain is in Assignment_1_3.1_D3.ipynb. To use and run our files, we use Jupyter Notebook (any other platform that supports the ipynb files). To execute the file, we hence Navigate to the file in Jupyter Notebook and run it. 



# Task 3.2 Development of a h Noun - Adjective i Pair Ranker
The first step performed under this task is coreferencing. Coreferencing is to find all expressions that refer to the same person/thing in a text. NeuralCoref is a pipeline extension for spaCy 2.1+ which annotates and resolves coreference clusters using a neural network. 
The requirements for coreferencing is installed as follows - 
```bash
   $ pip install spacy
   $ pip install neuralcoref 
```
(We assume pandas is already installed)
To run the file for coreferencing, 
```bash
   $ python3 Assignment_1_3.2_Coreferencing.py
```

After coreferencing is performed, we develop a program to common noun (phrase) - adjective (phrase) pairs and rank them in order. Before running the file, certain requirements are installed. 
```bash
   $ pip install textblob
   $ python -m spacy download en_core_web_sm
```
To run the file, navigate to Jupyter Notebook and run Assignment _1_3.2.ipynb



# Task 3.3 Application
For this task, we create a basic sentiment analysis model and plot multiple graphs and anayze them in detail. To run and see the analysis, we need to first install the requirements. 
```bash
   $ pip install scipy
   $ pip install plotly
   $ pip install scikit-learn
   $ pip install chart-studio
   $ pip install wordcloud
   $ pip install cufflinks
```
(Assuming previous dependencies are installed)

After installing all the required dependencies, the final task is run by naviagting to Assignment_1_3.3_Application.ipynb in Jupyter Notebook and running it

