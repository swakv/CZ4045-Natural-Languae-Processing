CZ4045-Natural-Languae-ProcessingPython Version - 3.7 is used throughout our projectDownload or Clone the repository before running any fileTask 3.1 Domain Specific Dataset AnalysisWeb Scraping for Domain 1 Analysis - Scrapy StackOverflow QuestionsScrapy is an efficient framework to crawl websites which uses a spider to crawl through websites. Firstly, we install scrapy. pip install scrapy (https://docs.scrapy.org/en/latest/intro/install.html)We then create a scrapy project directory. The syntax is shown below - scrapy startproject stackcd stack (Then we navigate to the directory we want to work on)Then, a scrapy field is created to act as a placeholder for the scraped data. This is done in stack/items.py as shown below - # items.pyimport scrapyclass StackItem(scrapy.Item):    # define the fields for your item here like:    # name = scrapy.Field()    content = scrapy.Field()    question = scrapy.Field()    passThe script Assignment_1_3.1_WebScraping.py is the python script used to scrape from the website. This file is created as stack/spiders/stackoverflow.pyThe results are stored in csv file which is done by modifying stack/settings.py as seen below. # settings.pyFEED_FORMAT="csv"FEED_URI="./domain1_dataset.csv"Finally, To scrawl the data, we scrawl 'dataset' as we name out class dataset as seen in Assignment_1_3.1_WebScraping.pyscrapy crawl datasetThe results of scraping is shown in domain1_dataset.csvDomain Specific Dataset AnalysisThe requirements required for 3.1 are shown below.  pip install numpy (https://numpy.org/install/) pip install pandas (https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html) pip install nltk (https://www.nltk.org/install.html) pip install matplotlib (https://pypi.org/project/matplotlib/)The Domain Specifc Analysis for Stack Overflow Domain is in Assignment_1_3.1_D1.ipynb, Medical Papers Domain is in Assignment_1_3.1_D2.ipynb and 3D Printers Domain is in Assignment_1_3.1_D3.ipynb. To use and run our files, we use Jupyter Notebook (any other platform that supports the ipynb files). To execute the file, we hence Navigate to the file in Jupyter Notebook and run it. Task 3.2 Development of a <Noun - Adjective> Pair RankerThe first step performed under this task is coreferencing. Coreferencing is to find all expressions that refer to the same person/thing in a text. NeuralCoref is a pipeline extension for spaCy 2.1+ which annotates and resolves coreference clusters using a neural network. The requirements for coreferencing is installed as follows - pip install spacy (https://spacy.io/usage)pip install neuralcoref (https://huggingface.co/coref/)(We assume pandas is already installed)To run the file for coreferencing, python3 Assignment_1_3.2_Coreferencing.pyAfter coreferencing is performed, we develop a program to common noun (phrase) - adjective (phrase) pairs and rank them in order. Before running the file, certain requirements are installed. pip install textblob (https://pypi.org/project/textblobConference )python -m spacy download en_core_web_smTo run the file, navigate to Jupyter Notebook and run Assignment _1_3.2.ipynbTask 3.3 ApplicationFor this task, we create a basic sentiment analysis model and plot multiple graphs and anayze them in detail. To run and see the analysis, we need to first install the requirements. pip install scipy (https://www.scipy.org/install.html)pip install plotly (https://plotly.com/python/getting-started/)pip install scikit-learn (https://scikit-learn.org/stable/install.html)pip install chart-studio (https://pypi.org/project/chart-studio/)pip install wordcloud (https://pypi.org/project/wordcloud/)pip install cufflinks (https://pypi.org/project/cufflinks/)(Assuming previous dependencies are installed)After installing all the required dependencies, the final task is run by naviagting to Assignment_1_3.3_Application.ipynb in Jupyter Notebook and running it


References 

Domain 1 - Technical Questions on Stack Overflow
1. https://stackoverflow.com/questions (scraped questions from here)

Domain 2 - 3D Printer Patents
1. https://patents.google.com/patent/US20150066178A1/en
2. https://patents.google.com/patent/US7291002B2/en
3. https://patents.google.com/patent/US20150375451A1/en
4. https://patents.justia.com/patent/20200171811
5. https://uspto.report/patent/app/20180169894
6. https://www.researchgate.net/publication/333534928_Research_and_implementation_of_a_non-supporting_3D_printing_method_based_on_5-axis_dynamic_slice_algorithm
7. https://www.hindawi.com/journals/complexity/2017/7849670/
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4189697/
9. https://www.researchgate.net/publication/295241769_Analysis_of_Energy_Utilization_in_3D_Printing_Processes
10. https://patents.google.com/patent/US20160067740A1/en
11. https://patents.google.com/patent/US10232603B2/en?oq=10232603
12. https://patents.google.com/patent/US9434838B2/en?oq=9.434%2c838
13. https://patents.google.com/patent/US10761497B2/en?oq=10%2c761%2c497
14. https://patents.google.com/patent/US20170297262A1/en?oq=15515955
15. https://patents.google.com/patent/US20160349738A1/en?oq=15116871
16. https://patents.google.com/patent/US10016929B2/en?oq=10016929
17. https://patents.google.com/patent/US10073424B2/en?oq=+10073424
18. https://patents.google.com/patent/US10730232B2/en?oq=10730232
19. https://patents.google.com/patent/US9314970B2/en?oq=9314970
20. https://patents.google.com/patent/US9950465B2/en?oq=9950465

Domain 3 - Meidical Papers
1. https://www.sciencedirect.com/science/article/abs/pii/S0168365920301681
2. https://www.sciencedirect.com/science/article/abs/pii/S1359029417300845
3. https://www.researchgate.net/publication/338232357_Novel_pHreduction_responsive_graphene_oxide_nanoparticles_based_hydrogel_for_targeted_combination_chemotherapy
4. https://www.sciencedirect.com/science/article/pii/S0142961217300029
5. https://www.researchgate.net/publication/330493372_Development_of_hollow_ferrogadolinium_nanonetworks_for_dual-modal_MRI_guided_cancer_chemotherapy
6. https://www.sciencedirect.com/science/article/abs/pii/S0168365920301681
7. https://www.researchgate.net/publication/316993307_The_Normal_Fetal_Pancreas
8. https://www.researchgate.net/publication/267407539_Presence_of_Magnetic_Fluids_Leads_to_the_Inhibition_of_Insulin_Amyloid_Aggregation
9. https://pubmed.ncbi.nlm.nih.gov/30394887/
10. https://pubs.rsc.org/en/content/articlelanding/2017/RA/C7RA08957K#!divAbstract
11. https://www.researchgate.net/publication/333738227_The_effect_of_turn_residues_on_the_folding_and_cell-penetrating_activity_of_b-hairpin_peptides_and_applications_toward_protein_delivery
12. https://www.researchgate.net/publication/285276676_Automated_Acquisition_of_Proximal_Femur_Morphological_Characteristics
13. https://www.researchgate.net/publication/323964968_Urinary_glicosaminoglycans_levels_in_women_with_urinary_tract_infection_and_non_urinary_tract_infection
14. https://www.researchgate.net/publication/337736816_Superhydrophobic_Coatings_for_Urinary_Catheters_To_Delay_Bacterial_Biofilm_Formation_and_Catheter-Associated_Urinary_Tract_Infection
15. https://www.researchgate.net/publication/6380348_Liver_Fatty_Acid-binding_Protein_Initiates_Budding_of_Pre-chylomicron_Transport_Vesicles_from_Intestinal_Endoplasmic_Reticulum
16. https://www.researchgate.net/publication/26569083_Study_of_the_effects_of_dietary_polyunsaturated_fatty_acids_Molecular_mechanisms_involved_in_intestinal_inflammation
17. https://www.researchgate.net/publication/323949582_Portal_hypertensive_gastropathy_association_with_Child-Pugh_score_in_liver_cirrhosis
18. https://www.sciencedirect.com/science/article/pii/S1549963419300012
19. https://advances.sciencemag.org/content/5/8/eaaw9336
20. https://www.researchgate.net/publication/327618502_GLK-IKK_signaling_induces_dimerization_and_translocation_of_the_AhR-RORt_complex_in_IL-17A_induction_and_autoimmune_disease