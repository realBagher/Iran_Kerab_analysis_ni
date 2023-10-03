# Irankeab Analysis Project
The **Iranketab Analysis Project** is a bot designed to scrape data from the iranketab book e-commerce website. It gathers information on over 100,000 books, including their title, author, translator, category, and publisher, and then stores this data in a MySQL database. Additionally, the project includes a Streamlit-based interface that provides various charts and visualizations for analyzing the scraped data, as well as an advanced search feature for users to find specific books.

## Components
The project consists of the following components:

- **Data Scraper:** Automatically collects data from iranketab, including book details like title, author, translator, category, and publisher.
- **Data Storage:** Stores the scraped data in a MySQL database for easy retrieval and analysis.
- **Streamlit Interface:** Provides a user-friendly interface for interacting with the data, including various charts and visualizations.

### Data Scraper
**scraing_iranketab.ipynb:** is a Jupyter notebook that contains the code for the data scraper. It uses the BeautifulSoup library to scrape data from the iranketab website, and then stores the data in a MySQL database.

### Data Storage
**database.ipynb:** is a Jupyter notebook that contains the code for create database and tables in MySQL.
You should create a database and tables in MySQL and then run this notebook.

**data_injection.ipynb:** is a Jupyter notebook that contains the code for inject data from csv file to MySQL database.
Csv file link in additional.txt file.

**iranketab_db.sql:** is database file that you can import it in MySQL. Download it from additional.txt file.
You can Import file in MySQL with this command:
```shell 
mysql -u username -p database_name < iranketab_db.sql
```

### Streamlit Interface
**static_chart.py:** is a python file that contains the code for the Streamlit interface. It provides a user-friendly interface for interacting with the data, including various charts and visualizations.
Charts:
1. Most books by category
2. Top 10 publishers
2. books by year of publication
3. Top 10 authors
4. books by top 10 translators
5. scatter plots for pages vs. publication year
6. undiscounted price vs. publication year
7. books by top 10 categories
8. price vs. rating
9. Most books by type of size


**advance_filtesrs.py:** is a python file that contains the code for the Streamlit interface. It provides a user-friendly interface for use advanced search feature for users to find specific books.
You can search by:
1. Book name
2. Author name
3. Translator name
4. Publisher name
5. Category name
6. Book size
7. Price
8. Rating
9. Number of pages
10. Year of publication
11. Category of book

**Dashboard.ipynb:** is a Jupyter notebook that contains the code for the Streamlit interface. It provides a user-friendly interface for interacting with the data, including various charts and visualizations.
