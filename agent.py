import os
import argparse
from dotenv import load_dotenv
from openbb_agents.agent import openbb_agent

from prompts import fintel

# Load environment variables
load_dotenv()
openbb_pat = os.getenv("OPENBB_PAT")

def main():
    parser = argparse.ArgumentParser(description="Leverage AI for macroeconomic and quantitative analysis of stocks and cryptocurrencies.")
    parser.add_argument('-t', '--ticker', type=str, help="Input a ticker symbol of the stock or cryptocurrency (e.g., PLTR or BTC)")
    parser.add_argument('-m', '--macro', action='store_true', help="Generate a macroeconomic intelligence report on latest econometrics")   
    args = parser.parse_args()
    
    if args.ticker:
        ticker = args.ticker
        quant_prompt = fintel.generate_quant_sma_analysis_prompt(ticker)
        quant_result = openbb_agent(quant_prompt, openbb_pat=openbb_pat, verbose=False)
        print(quant_result)
    if args.macro:
        macro_prompt = fintel.macroeconomic_analysis_prompt
        macro_result = openbb_agent(macro_prompt, openbb_pat=openbb_pat, verbose=False)
        print(macro_result)
    

if __name__ == "__main__":
    main()
    ## Example of how to call the agent directly
    #openbb_agent("Perform an day analysis on the Nasdaq", openbb_pat=openbb_pat, verbose=False) 


