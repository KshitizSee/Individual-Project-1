# Individual-Project-1
# Project Title: Walmart Retail Sales Analysis

## Description
This project analyzes Walmart retail sales data from 2012 to 2015 using Python and SQLite. The script processes sales data, calculates the sales growth rate per state, and identifies the most profitable products by state and region.

## Getting Started
### Prerequisites
- Python 3.x
- Required Python libraries:
  ```sh
  pip install pandas sqlite3 openpyxl
  ```

### Installing
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/walmart-sales-analysis.git
   ```
2. Navigate to the project folder:
   ```sh
   cd walmart-sales-analysis
   ```
3. Ensure the `WalmartRetailSales.xlsx` file is in the project directory.

## Running the Script
- Execute the Python script:
  ```sh
  python script.py
  ```
- The script will:
  - Load and process the dataset from an Excel file.
  - Store the data in an in-memory SQLite database.
  - Calculate the sales growth rate per state.
  - Identify the most profitable products in each region and state.
  - Print results to the console.

## SQL Queries Used
1. **Sales Growth Rate per State**
   - Calculates yearly sales growth per state and determines if sales are decreasing in most states.
2. **Most Profitable Products**
   - Finds the most profitable products for each region and state.

## Deployment
This project is intended for local analysis and data exploration.

## Author
- **Your Name**
- GitHub: [Your GitHub Profile](https://github.com/yourusername)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Data source: Walmart Retail Sales Dataset
- Libraries used: Pandas, SQLite, OpenPyxl
