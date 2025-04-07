# Individual Project 1 - Walmart Retail Sales Analysis

## Project Overview
This detailed data analysis project involves processing, cleaning, and analyzing Walmart retail sales data spanning from 2001 to 2015. It showcases advanced techniques for data cleaning, MySQL database operations, and data visualization to derive valuable business insights from the retail sales data.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
 - [Prerequisites](#prerequisites)
 - [Installation](#installation)
- [Usage](#usage)
 - [Data Cleaning](#data-cleaning)
 - [Database Operations](#database-operations)
 - [Data Analysis](#data-analysis)
- [Key Insights](#key-insights)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Author](#author)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Data Cleaning**: Processes raw Excel data, handles special characters, and formats dates
- **Database Integration**: Connects to MySQL database for efficient data storage and retrieval
- **Sales Growth Analysis**: Calculates year-over-year sales growth rates by state
- **Profitability Analysis**: Identifies most profitable product categories by region
- **Data Visualization**: Creates insightful visualizations of sales trends and profitability
- **SQL Optimization**: Utilizes advanced SQL queries including window functions and CTEs

## Project Structure

```
Walmart-Sales-Analysis/
├── Data/
│   └── WalmartRetailSales.csv
├── data_cleaning.py
├── database_operations.py
├── Data_analysis.py
├── Visualtions/
│   └── create_visualization.py
│   └── profit_vs_orders.png
    └── state_sales_growth.png
    └── top_subcategories_by_region.png
    └── yearly_sales_trend.png
├── requirements.txt
├── README.md
├── LICENSE.md
└── .gitignore

                 
```

## Technologies Used

- **Python 3.9**: Core programming language
- **pandas**: Data manipulation and analysis
- **pymysql**: MySQL database connector
- **sqlalchemy**: SQL toolkit and Object-Relational Mapping
- **matplotlib & seaborn**: Data visualization
- **MySQL**: Database management system

## Getting Started

### Prerequisites

- Python 3.9 or higher
- MySQL Server 5.7 or higher
- Git (for version control)

### Installation
  - Follow these clear steps to set up the Walmart Retail Sales Analysis Poject on your system:

   1. **Clone the repository**
  ```bash
  git clone https://github.com/KshitizSee/Individual-Project-1.git
  ```

   2. **Install required Python packages**
  ```bash
  pip install pandas pymysql sqlalchemy matplotlib seaborn
  ```
  - These packages provide essential functionality for data manipulation, database connections, and visualization.


   3. **Step 3: Set Up MySQL Database**
    i. **Install MySQL**
  ```bash
  sudo apt install mysql-server
  ```
   ii. **Secure MySQL Installation**
  ```bash
  sudo mysql_secure_installation
  ```
   - Follow the prompts to set a root password and secure your installation.
    
   iii. **Check MySQL Status**
  ```bash
  sudo systemctl status mysql
  ```
   - Ensure that MySQL is running (look for "active (running)")
    
   iv. **Set up MySQL database**
  ```bash
  mysql -u root -p
  ```
   - Enter your password when prompted, then run these SQL commands:
     
     
  ```sql
  CREATE DATABASE walmart;
  USE walmart;
  
  CREATE TABLE sales (
    `Row ID` INT,
    `Order ID` INT,
    `Order Date` DATE,
    `Order Priority` TEXT,
    `Order Quantity` INT,
    `Sales` DOUBLE,
    `Discount` DOUBLE,
    `Ship Mode` TEXT,
    `Profit` DOUBLE,
    `Unit Price` DOUBLE,
    `Shipping Cost` DOUBLE,
    `Customer Name` TEXT,
    `Customer Age` TEXT,
    `City` TEXT,
    `Zip Code` INT,
    `State` TEXT,
    `Region` TEXT,
    `Customer Segment` TEXT,
    `Product Category` TEXT,
    `Product Sub-Category` TEXT,
    `Product Name` TEXT,
    `Product Container` TEXT,
    `Product Base Margin` TEXT,
    `Ship Date` TEXT
  );
  ```

4. **Prepare your data**
  - Place  WalmartRetailSales.csv in the project root directory.
    Once these steps are completed, you can run the analysis scripts in sequence (cleaning → database operations 
    → analysis → visualization) to process the data and generate insights

## Usage

### Data Cleaning

Run the data cleaning module to preprocess the raw data:

```bash
python data_cleaning.py
```

This script will:
1. Import the raw Excel data
2. Eliminate special characters from product names
3. Convert dates into the correct format
4. Save the cleaned data as a CSV file

### Database Operations
Run the database operations module to interact with MySQL:

```bash
python database_operations.py
```

This script will:
1. Establish a connection to the MySQL database
2. Run sample queries
3. Show table details
4. Modify data types as required

### Data Analysis
Run the data analysis module to generate insights:

```bash
python data_analysis.py
```

This script will:
1. Examine annual sales trends
2. Compute sales growth by state
3. Identify the most profitable product categories across regions
4. Create visualizations to highlight key insights

## Key Insights
The analysis uncovers several key business insights:

1. **Regional Performance:** Office Machines are the top-performing product category in both the South and Central regions, while Binders and Binder Accessories dominate in the East.
2. **Sales Growth Trends:** Some states show notable fluctuations in sales, with Wyoming seeing a 687% increase in 2013, followed by an 87% decrease in 2015.
3. **Annual Trends:** There was a significant rise in order volume from 2012 to 2015 compared to earlier years, with 2012 recording the highest number of orders.


### Data Cleaning Tests

```bash
python data_cleaning.py
```
Verifies data loading, cleaning, and export functions.

### Database Operations Tests

```bash
python database_operations.py
```
Tests database connectivity, query execution, and data type handling.

### Data Analysis Tests

```bash
python data_analysis.py
```
Validates analysis functions and visualization generation.

## Deployment
This project is designed for flexible deployment but still not deployed but can done by using GitHub CI/CD pipeline, flask/django framework, fastapi and aws server or heruko:

### Local Analysis
Follow the installation instructions to run locally for data analysis.

### Server Deployment
1. Install a server with Python and MySQL
2. Adjust the database connection settings in the scripts
3. Set up scheduled executions using cron or similar tools

### Dashboard Integration
The visualization elements can be incorporated into web frameworks by:
1. Using Flask or Django to build a web interface
2. Embedding visualizations within HTML templates
3. Deploying the interface on a web server for team access

## Future Enhancements
Potential improvements for future versions:
1. Incorporating machine learning models for sales forecasting
2. Creating interactive dashboards with Plotly or Dash
3. Connecting to real-time data sources
4. Broadening the analysis to include customer demographic information
5. Introducing automated reporting features

## Author
**Kshitij Chaudhary**

## License

## Acknowledgements
- Walmart for providing the retail sales dataset
