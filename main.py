import asyncio
import nest_asyncio
from manager import PortfolioTradingManager
from dotenv import load_dotenv
import time
from markdown_pdf import MarkdownPdf
from markdown_pdf import Section
import os


# Load environment variables
load_dotenv()
# to allow nested event loops
nest_asyncio.apply()

# Entrypoint for the portfolio trading bot.
# Run this as `python -m main` and enter a
# stock NSE ticker & customer_id
async def main():
    print('\n')
    text = "This program will analyse and recommend whether a stock is fit for buy/sell for a customer."
    for word in text.split(sep=' '):
        print(word, end=' ', flush=True)
        time.sleep(0.1)
    print('\n') # Print a newline at the end of the text
    #print('This program will analyse and recommend whether a stock is fit for buy/sell for a customer.')

    stockname = input("Enter Stock Name: ")
    customer_id = input("Enter Customer Id: ")
    print('')
    
    # Start the clock
    start_time = time.perf_counter()

    mgr = PortfolioTradingManager(customer_id=customer_id, stockname=stockname)

    output = await mgr.run_agents()
    #print(*output, sep='\n')

    # end the clock
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.4f} seconds")
    
    #The following block will save the output in a pdf file
    output_directory_path = "./output"
    # Create the directory if it doesn't exist
    os.makedirs(output_directory_path, exist_ok=True) 
    text = '\n'.join(output)
    pdf = MarkdownPdf(toc_level=1)
    pdf.add_section(Section(text))
    pdf.save(output_directory_path+"/"+stockname+"_Analysis.pdf")
    

if __name__ == "__main__":
    asyncio.run(main())
    