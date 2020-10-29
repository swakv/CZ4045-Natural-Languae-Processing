# CZ4045-Natural-Language-Processing

Python Version - 3.7 is used throughout our project

Download or Clone the repository before running any file


# Task 3.1 Domain Specific Dataset Analysis

# Web Scraping for Domain 1 Analysis - Scrapy StackOverflow Questions
Scrapy is an efficient framework to crawl websites which uses a spider to crawl through websites. This has been used to scrape technical questions from StackOverflow to form our first dataset. 
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
The requirements required for 3.1 are shown below. We use numpy and pandas to access and process different parts of the dataframe. NLTK was used to carry out tokenization, stemming and such other functions. Matplotlib was used to plot the output graphs.
```bash
   $ pip install numpy
   $ pip install pandas
   $ pip install nltk
   $ pip install matplotlib
```
The Domain Specifc Analysis for Stack Overflow Domain is in Assignment_1_3.1_D1.ipynb, Medical Papers Domain is in Assignment_1_3.1_D2.ipynb and 3D Printers Domain is in Assignment_1_3.1_D3.ipynb. To use and run our files, we use Jupyter Notebook (or any other platform that supports the ipynb files). To execute the file, we simply navigate to the file in Jupyter Notebook and run it. 

In each .ipynb file, the resulting dataframes and explanations after each NLP process and the specified plots can be found. In depth analysis of these results can be found in the report.


# Task 3.2 Development of a <Noun - Adjective> Pair Ranker
The first step performed under this task is coreferencing. Coreferencing is to find all expressions that refer to the same person/thing in a text. NeuralCoref is a pipeline extension for spaCy 2.1+ which annotates and resolves coreference clusters using a neural network. 
SpaCy was used for POS tagging to identify the nouns and adjectives. NeuralCoref was used for coreferencing to replace the pronouns with the associated noun. The requirements for coreferencing are installed as follows - 
```bash
   $ pip install spacy
   $ pip install neuralcoref 
```
(We assume pandas is already installed)
   
The file below contains the code to do the coreferencing on our dataframe and saves it as a new .csv file called "resolved.csv". To run the file for coreferencing, 
```bash
   $ python3 Assignment_1_3.2_Coreferencing.py
```

After coreferencing is performed, we develop a program to common noun (phrase) - adjective (phrase) pairs and rank them in order. Before running the file, certain requirements are installed. TextBlob was used to rank the noun adjective pairs of a single noun in terms of the frequency of appearance. The ranking was done based on their sentiment polarity scores. 
```bash
   $ pip install textblob
   $ python -m spacy download en_core_web_sm
```
To run the file, navigate to Jupyter Notebook and run Assignment _1_3.2.ipynb. 

The result of the above file gives us the most common noun adjective pairs which convey the most meaning according to our TextBlob algorithm. Comparison between manual and code output is discussed in the report.

# Task 3.3 Application
For this task, we create a basic sentiment analysis model and plot multiple graphs and anayze them in detail. To run and see the analysis, we need to first install the requirements. Plotly and WordCloud were used for visualisation while all other libraries were used for processing the outputs.
```bash
   $ pip install scipy
   $ pip install plotly
   $ pip install scikit-learn
   $ pip install chart-studio
   $ pip install wordcloud
   $ pip install cufflinks
```
(Assuming previous dependencies are installed)

After installing all the required dependencies, the final task is run by naviagting to Assignment_1_3.3_Application.ipynb in Jupyter Notebook and running it. All plots can be found in this notebook and extra analysis can be found in the report. The output of this part involves sentiment classification of our data into positive, negative and neutral with respective polarity scores. 

