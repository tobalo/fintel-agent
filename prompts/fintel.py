
def generate_comparative_analysis_prompt(ticker):
    return f"""
        Check what are {ticker} peers. From those, check which one has the highest market cap. Then, on the ticker that has the highest market cap get the most recent price target estimate from an analyst, and tell me who it was and on what date the estimate was made
    """

def generate_quant_sma_analysis_prompt(ticker):
    return f"""
        Perform a qunatitative analysis of {ticker} based on standard small moving averages and provide a signals intelligence report on BUY / SELL with {ticker} quantiative data."
    """

macroeconomic_analysis_prompt = """
    Provide strategic foresight and intelligence report based on macro-economic and sentiment factors.
    """
