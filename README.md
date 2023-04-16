## Exploratory Data Analysis of TripAdvisor restaurants in Valencia

In this repository I present the results of an exploratory data analysis on restaurants in Valencia. This work is one of the project which I carried out during the Data Science bootcamp at "The Bridge" school in Valencia (Spain).

### 1. Goals of the project
#### 1.1 Main objective

I will analyse data about all restaurants in Valencia (Spain) which appear on the [TripAdvisor webpage](https://www.tripadvisor.com/Restaurants-g187529-Valencia_Province_of_Valencia_Valencian_Community.html). The main purpose of this exploratory data analysis project is to investigate how restaurants are distributed around the city and identify the best types of restaurants on which a possible investor should focus his/her target. Moreover I will explore how the chosen types of restaurants are distributed in the different neighbourhoods to suggest the best places where to open a new restaurant of that type. 

#### 1.2 Secondary objectives

Furthermore I want to check the following hypotheses, based on my own experience, or on my ideas:

- The most popular type of restaurant is spanish restaurants (as Valencia is in Spain);
- Among the most popular foreign cuisine I would expect to find Italian, Japanese and Chinese ;
- The neighbourhoods with more restaurant per 10k residents are Ciutat Vella (City center), l'Eixample; 
- The position in the ranking depends on the number of reviews and average vote;
- The position in the ranking should not depend on the price level of the restaurant, or on the income/population of the neighbourhood.


### 2. Structure of the repository

#### 2.1 data folder

In this folder you can find the csv files which have been used to carry out the analysis:
- "boroughs.csv" is a csv file with population and income of the various neighbourhoods of Valencia;
- "postal_codes.csv" is a csv file which map the postal codes of Valencia with the corresponding neighbourhoods;
- "df_TripAdvisor_total_boroughs.csv" is the total csv file which is used in the analysis; it comes from the information obtained webscraping from TripAdvisor webpage, combined with the other two csv files.

The columns of the "df_TripAdvisor_total_boroughs.csv" DataFrame are:

- **Restaurant name**: The name of the restaurant (*string*)
- **Rankin**: The position in the TripAdvisor ranking (*int*)
- **Number of reviews**: Total number of reviews (*int*)
- **Average vote**: Average vote given by the users who left the reviews (*float*)
- **Price range**: Price range as found on TripAdvisor with "\$" symbols (*string*)
- **Price level**: Conversion of price range into a numerical scale from 1 to 7 (*float*)
- **address**: Complete address of the restaurant (*string*)
- **Postal code**: Postal code extracted from the address (*string*)
- **Restaurant type 1**: Main type of the restaurant (*string*)
- **Restaurant type 2**: Secondary type of the restaurant (*string*)
- **Boroughs**: Borough where the restaurant is located (*string*)
- **Population**: Number of residents in the borough (*int*)
- **Income**: Mean income of the borough (*float*)

#### 2.2 src folder

This folder only contains a python script "functions.py", where I implemented a couple functions and classes for visualization with widgets.

#### 2.3 notebooks folder

This folder contains two notebooks:

- **Scraping_TripAdvisor.ipynb**: In this notebook I use BeautifulSoup and Selenium libraries to navigate through the TripAdvisor webpage and extract the information about the restaurants in Valencia. Once all the information is extracted I save them into a pandas DataFrame, I perform some cleaning of the data, and I merge it with the DataFrames containing the information about the neighbourhoods. Finally I save the resulting DataFrame into the csv file in "data/df_TripAdvisor_total_boroughs.csv", which is the csv which is going to be used for the analysis;
- **Analysis.ipynb**: In this notebook I read the main csv and I perform the exploratory data analysis.