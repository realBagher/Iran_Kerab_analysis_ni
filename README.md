# Iranketab Analysis Project

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Usage](#usage)
   - [Scraper](#scraper)
   - [Streamlit Interface](#streamlit-interface)
5. [Charts and Visualizations](#charts-and-visualizations)
6. [Advanced Search](#advanced-search)
7. [License](#license)

## Introduction

The **Iranketab Analysis Project** is a bot designed to scrape data from the iranketab book e-commerce website. It gathers information on over 100,000 books, including their title, author, translator, category, and publisher, and then stores this data in a MySQL database. Additionally, the project includes a Streamlit-based interface that provides various charts and visualizations for analyzing the scraped data, as well as an advanced search feature for users to find specific books.

## Features

- **Web Scraper**: Automatically collects data from iranketab, including book details like title, author, translator, category, and publisher.

- **Data Storage**: Stores the scraped data in a MySQL database for easy retrieval and analysis.

- **Streamlit Interface**: Provides a user-friendly interface for interacting with the data, including various charts and visualizations.

- **Charts and Visualizations**: Includes a variety of charts such as Top 10 publishers, books by year of publication, Top 10 authors, books by top 10 translators, scatter plots for pages vs. publication year, undiscounted price vs. publication year, and more.

- **Advanced Search**: Allows users to perform advanced searches to find specific books based on various criteria.

## Getting Started

### Prerequisites

- Python 3.x
- MySQL Database
- Required Python libraries (specified in requirements.txt)

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/realBagher/Iran_Kerab_analysis_ni.git
   cd Iran_Kerab_analysis_ni
   ```
2. Install the required Python libraries:

   ```shell
   pip install -r requirements.txt
    ```
   
3. Set up your MySQL database and configure the database connection in the code.

## Usage
### Streamlit Interface
Run the following command to start the Streamlit interface:

   ```shell
   streamlit run static_chart.py
   ```

## Charts and Visualizations
The Streamlit interface provides the following charts and visualizations:

- **Top 10 Publishers**: Displays the top 10 publishers based on the number of books they have published.
- **Books by Year of Publication**: Displays the number of books published each year.
- **Top 10 Authors**: Displays the top 10 authors based on the number of books they have written.
- **Books by Top 10 Translators**: Displays the number of books translated by the top 10 translators.
- **Pages vs. Publication Year**: Displays a scatter plot of the number of pages vs. the year of publication.
- **Undiscounted Price vs. Publication Year**: Displays a scatter plot of the undiscounted price vs. the year of publication.
- **Price vs. Book Score**: Displays a scatter plot of the price vs. the book score.

## Advanced Search
The Streamlit interface also provides an advanced search feature that allows users to find specific books based on various criteria. The following criteria are supported:

- **Title**: The title of the book.
- **Author**: The author of the book.
- **Translator**: The translator of the book.
- **Publisher**: The publisher of the book.
- **Category**: The category of the book.
- **ISBN**: The ISBN of the book.
- and more...

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.