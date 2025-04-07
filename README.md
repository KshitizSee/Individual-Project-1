Walmart Retail Sales Analysis

Project Overview:
This comprehensive data analysis project processes, cleans, and analyzes Walmart retail sales data from 2001 to 2015. The project demonstrates advanced data cleaning techniques, MySQL database operations, and data visualization to extract meaningful business insights from retail sales data.

Table of Contents:
- Project Overview
- Features
- Project Structure
- Technologies Used
- Getting Started
  - Prerequisites
  - Installation
  - Usage
    - Data Cleaning
    - Database Operations
    - Data Analysis
- Key Insights
- Deployment
- Future Enhancements
- Author
- License
- Acknowledgements

Features:
- Data Cleaning: Processes raw Excel data, handles special characters, and formats dates.
- Database Integration: Connects to MySQL database for efficient data storage and retrieval.
- Sales Growth Analysis: Calculates year-over-year sales growth rates by state.
- Profitability Analysis: Identifies most profitable product categories by region.
- Data Visualization: Creates insightful visualizations of sales trends and profitability.
- SQL Optimization: Utilizes advanced SQL queries including window functions and CTEs.

Project Structure:
Walmart-Sales-Analysis/
├── Data/
│   └── WalmartRetailSales.csv
├── data_cleaning.py
├── database_operations.py
├── data_analysis.py
├── Visualtions/
│   └── create_visualization.py
│   └── profit_vs_orders.png
│   └── state_sales_growth.png
│   └── top_subcategories_by_region.png
│   └── yearly_sales_trend.png
├── requirements.txt
├── README.txt
├── LICENSE.md
└── .gitignore

Technologies Used:
- Python 3.XX: Core programming language
- pandas: Data manipulation and analysis
- pymysql: MySQL database connector
- sqlalchemy: SQL toolkit and Object-Relational Mapping
- matplotlib & seaborn: Data visualization
- MySQL: Database management system

Getting Started:
Prerequisites:
- Python 3.9 or higher
- MySQL Server 5.7 or higher
- Git (for version control)

Installation:
1. Clone the repository
   git clone git@github.com:bajegaha/Walmart_analysis.git

2. Install required Python packages
   pip install pandas pymysql sqlalchemy matplotlib seaborn

3. Set Up MySQL Database:
   i. Install MySQL:
      sudo apt install mysql-server

   ii. Secure MySQL Installation:
      sudo mysql_secure_installation

   iii. Check MySQL Status:
      sudo systemctl status mysql

   iv. Set up MySQL database:
      mysql -u root -p

   Run the following SQL commands:
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

4. Prepare your data:
   Place WalmartRetailSales.csv in the project root directory.

Once these steps are completed, you can run the analysis scripts in sequence: data cleaning → database operations → analysis → visualization.

Usage:
Data Cleaning:
Run the data cleaning module to preprocess the raw data:
   python data_cleaning.py
This script will:
- Load the raw Excel data
- Remove special characters from product names
- Convert dates to proper format
- Export cleaned data to CSV format

Database Operations:
Run the database operations module to interact with MySQL:
   python database_operations.py
This script will:
- Connect to the MySQL database
- Execute sample queries
- Display table information
- Update data types as needed

Data Analysis:
Run the data analysis module to generate insights:
   python data_analysis.py
This script will:
- Analyze yearly sales trends
- Calculate state-by-state sales growth
- Identify most profitable product categories by region
- Generate visualizations of key findings

Key Insights:
- Regional Performance: Office Machines are the most profitable product category in both South and Central regions, while Binders and Binder Accessories lead in the East region.
- Sales Growth Patterns: Several states show significant sales volatility, with Wyoming experiencing 687% growth in 2013 followed by an 87% decline in 2015.
- Yearly Trends: Order volume increased dramatically in 2012-2015 compared to earlier years, with 2012 showing the highest number of orders.

Deployment:
This project is designed for flexible deployment but still not deployed. It can be done using GitHub CI/CD pipelines, Flask/Django frameworks, FastAPI, and AWS or Heroku servers.

Local Analysis:
Follow the installation instructions to run locally for data analysis.

Server Deployment:
For server deployment:
- Set up a server with Python and MySQL.
- Configure database connection parameters in the scripts.
- Schedule regular runs using cron or similar tools.

Dashboard Integration:
The visualization components can be integrated with web frameworks:
- Use Flask or Django to create a web interface.
- Embed visualizations in HTML templates.
- Deploy to a web server for team access.

Future Enhancements:
- Implement machine learning for sales prediction
- Add interactive dashboards using Plotly or Dash
- Integrate with real-time data sources
- Expand analysis to include customer demographics
- Add automated reporting functionality

Author:
Ghan Bahadur Gaha

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements:
- Walmart for providing the retail sales dataset
- All contributors who have helped improve this project, especially my teammates @Kapil Choudhary, @Ramsharan Pokharel, @Iris Russell, and @Anshul Sharma
