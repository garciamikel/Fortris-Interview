import logging
import pandas as pd
import json

# Configure logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



x = '''{ "_id": "ObjectId('60b8d295f1a7f2355e9f1d8c')", 
"Date": "2024-06-20T15:30:00Z", 
"Amount": 250.75, 
"txHash": "0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890" }'''

try:

    xjson = json.loads(x)
    dfOrder = pd.DataFrame(xjson,index=[0])

    print(dfOrder)
        # Save DataFrame to CSV file
    dfOrder.to_csv('OrderFile.csv')
    logging.info("DataFrame successfully saved to 'OrderFile.csv'.")

except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
    print(f"An unexpected error occurred: {e}")
