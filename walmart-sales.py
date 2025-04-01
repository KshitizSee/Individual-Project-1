import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel('WalmartRetailSales.xlsx')

# Data cleaning steps here...

# Create SQL database connection
conn = sqlite3.connect(':memory:')
df.to_sql('sales', conn, index=False)

# Task 1: Sales Growth Analysis
def analyze_sales_growth(conn):
    query = """
    SELECT 
        State,
        Year,
        SUM(Sales) as TotalSales,
        (SUM(Sales) - LAG(SUM(Sales)) OVER (PARTITION BY State ORDER BY Year)) / 
        LAG(SUM(Sales)) OVER (PARTITION BY State ORDER BY Year) * 100 as GrowthRate
    FROM sales
    GROUP BY State, Year
    ORDER BY State, Year
    """
    growth_df = pd.read_sql(query, conn)
    
    # Visualization
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=growth_df, x='Year', y='GrowthRate', hue='State')
    plt.title('Sales Growth Rate by State')
    plt.ylabel('Growth Rate (%)')
    plt.savefig('sales_growth.png')
    plt.close()
    
    return growth_df

# Task 2: Product Recommendations
def product_recommendations(conn):
    query = """
    SELECT 
        Region,
        State,
        Category,
        Product_Name,
        SUM(Profit) as TotalProfit,
        SUM(Sales) as TotalSales,
        SUM(Profit)/SUM(Sales) as ProfitMargin,
        RANK() OVER (PARTITION BY Region, State ORDER BY SUM(Profit) DESC) as ProfitRank
    FROM sales
    GROUP BY Region, State, Category, Product_Name
    """
    profit_df = pd.read_sql(query, conn)
    
    # Get top 3 products per region/state
    recommendations = profit_df[profit_df['ProfitRank'] <= 3]
    
    return recommendations

# Execute analysis
growth_results = analyze_sales_growth(conn)
product_recs = product_recommendations(conn)

# Save results to Excel for reporting
with pd.ExcelWriter('Walmart_Analysis_Results.xlsx') as writer:
    growth_results.to_excel(writer, sheet_name='Sales Growth', index=False)
    product_recs.to_excel(writer, sheet_name='Product Recommendations', index=False)