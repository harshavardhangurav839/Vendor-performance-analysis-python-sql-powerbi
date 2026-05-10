import pandas as pd
import sqlite3
import logging
from ingestion_db import create_engine
logging.basicConfig(filename="logs/get_vendor_summary.log",
                    level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s')",
                    filemode='a')

conn=sqlite3.connect('data1.db') # creating a connection to the database

def ingest_db(df,table_name,engine):
    try:
        df.to_sql(table_name,engine,if_exists='replace',index=False)
        logging.info(f"Data ingested successfully into {table_name} table.")
    except Exception as e:
        logging.error(f"Error ingesting data into {table_name} table: {e}")

        
def create_vendor_summary(conn):
   
   vendor_sales_summary=pd.red_sql_query("""WITH  freight_data AS (SELECT VendorNumber,
                                         sum(Freight) as freight_cost
                                        FROM vendor_invoice GROUP BY VendorNumber),
                                         
                                         PurchaseSummary AS (select p.VendorNumber,
                                         p.VendorName,
                                         p.Brand,
                                         p.PurchasePrice,
                                         pp.Volume,
                                         pp.Price as actual_price,
                                         sum(p.Quantity) as totalPurchasequantity,
                                         Sum(p.Dollars) as Totalpurchasedollars from purchases p JOIN 
                                         purchase_prices pp ON p.Brand=pp.Brand where p.PurchasePrice>0
                                         group by p.VendorNumber,p.VendorName,p.Brand )  ,

                                         SalesSummary AS (Select VendorNo,
                                         Brand,Sum(SalesDollars) as TotalSalesDollars,
                                         Sum(SalesPrice) as TotalSalesPrice,
                                         Sum(SalesQuantity) as TotalSalesQuantity,
                                         Sum(ExciseTax) as TotalExciseTax
                                         from sales group by VendorNo,Brand  ) 
                                          
                                        SELECT 
                                        ps.VendorNumber,
                                        ps.VendorName,
                                        ps.Brand,
                                        ps.PurchasePrice,
                                        ps.actual_price,
                                        ps.Volume,
                                        ps.TotalPurchaseQuantity,
                                        ps.TotalPurchaseDollars,
                                        ss.TotalSalesQuantity,
                                        ss.TotalSalesDollars,
                                        ss.TotalSalesPrice,
                                        ss.TotalExciseTax,
                                        fd.freight_cost
                                        FROM PurchaseSummary ps
                                        LEFT JOIN SalesSummary ss ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
                                       left join freight_data fd
                                       on ps.VendorNumber=fd.VendorNumber
                                       order by ps.TotalPurchaseDollars Desc  """,conn)

    return vendor_sales_summary()

def clean_data(df):
   #this function will clean the data and return the cleaned dataframe
   df['Volume']=df['Volume'].astype('float64')  
   df.fillna(0,inplace=True)
   df['VendorName']=df['VendorName'].str.strip()


   #creating new columns for analysis

   Vendor_sales_summary['GrossProfit']=Vendor_sales_summary['TotalSalesDollars']-Vendor_sales_summary['Totalpurchasedollars']
   Vendor_sales_summary['ProfitMargin']=Vendor_sales_summary['GrossProfit']/Vendor_sales_summary['TotalSalesDollars']*100
   Vendor_sales_summary['StockTurnover']=Vendor_sales_summary['TotalSalesQuantity']/Vendor_sales_summary['totalPurchasequantity']
   Vendor_sales_summary['SalesToPurchaseRatio']=Vendor_sales_summary['TotalSalesDollars']/Vendor_sales_summary['Totalpurchasedollars']
   return df














#checking the tables in the database
tables=pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
tables
for table in tables['name']:
    print( '-'*50,f'{table}','-'*50)
    print('count of records:',pd.read_sql(f'SELECT COUNT(*) as count FROM {table}', conn)['count'].values[0])
    display(pd.read_sql(f'SELECT * FROM {table} LIMIT 5', conn))
    
    # From vendor table we are taking the column frieght to make further analysis
freight_data=pd.read_sql('SELECT VendorNumber,sum(Freight) as freight_cost FROM vendor_invoice GROUP BY VendorNumber', conn)
freight_data
pd.read_sql_query("""select p.VendorNumber,p.VendorName,p.Brand,p.PurchasePrice,pp.Volume,pp.Price as actual_price,sum(p.Quantity) as totalPurchasequantity,
                  Sum(p.Dollars) as Totalpurchasedollars from purchases p JOIN 
                   purchase_prices pp ON p.Brand=pp.Brand where p.PurchasePrice>0
                   group by p.VendorNumber,p.VendorName,p.Brand order by Totalpurchasedollars""",conn)

#Here we join the purchase and Purchase_price table to get the actual price of the product and then we are calculating the total purchase quantity and dollars for each vendor and brand. This will help us to identify

pd.read_sql_query( """Select VendorNo,Brand,Sum(SalesDollars) as TotalSalesDollars,
                  Sum(SalesPrice) as TotalSalesPrice,
                  Sum(SalesQuantity) as TotalSalesQuantity,
                  Sum(ExciseTax) as TotalExciseTax
                  from sales group by VendorNo,Brand  order by TotalSalesDollars """,conn)



                                 
 Vendor_sales_summary
Vendor_sales_summary.dtypes
Vendor_sales_summary.isnull().sum()
Vendor_sales_summary['Volume']=Vendor_sales_summary['Volume'].astype('float64')
Vendor_sales_summary.fillna(0,inplace=True)
Vendor_sales_summary['VendorName']=Vendor_sales_summary['VendorName'].str.strip()
Vendor_sales_summary['VendorName'].unique()
Vendor_sales_summary['GrossProfit']=Vendor_sales_summary['TotalSalesDollars']-Vendor_sales_summary['Totalpurchasedollars']
Vendor_sales_summary['ProfitMargin']=Vendor_sales_summary['GrossProfit']/Vendor_sales_summary['TotalSalesDollars']*100
Vendor_sales_summary['StockTurnover']=Vendor_sales_summary['TotalSalesQuantity']/Vendor_sales_summary['totalPurchasequantity']
Vendor_sales_summary['SalesToPurchaseRatio']=Vendor_sales_summary['TotalSalesDollars']/Vendor_sales_summary['Totalpurchasedollars']
Vendor_sales_summary.columns

# Much simpler approach - just save DataFrame to DB
Vendor_sales_summary.to_sql(
    'Vendor_sales_summary',
    conn,
    if_exists='replace',   # replaces if already exists
    index=False
)
conn.commit()
print("✅ Saved successfully!")
print(Vendor_sales_summary.shape)
Vendor_sales_summary.head()