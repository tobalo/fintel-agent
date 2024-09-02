# Finanical Analyst Agent
This agent is a simple agent that can be used to perform day analysis on a stock or cryptocurrency. It can also be used to generate a macroeconomic intelligence report on the latest econometrics.

## Directory Structure
```
.
├── agent.py
├── README.md
├── requirements.txt
├── prompts
│   ├── fintel.py
│   └── __init__.py
└── .env.example
```

## Installation

1. Clone the repository
2. Install the required dependencies
3. Create a `.env` file based on the `.env.example` file
4. Run the agent

## Usage

To run the agent, simply execute the `agent.py` script with the desired parameters:

```bash
python agent.py -t PLTR -m
```

This will generate a macroeconomic intelligence report on the latest econometrics for the stock PLTR.

To run the agent with a specific ticker symbol, use the `-t` flag followed by the ticker symbol:

```bash
python agent.py -t PLTR
```

This will generate a day analysis for the stock PLTR.

To generate a macroeconomic intelligence report, use the `-m` flag:

```bash
python agent.py -m
```

This will generate a macroeconomic intelligence report on the latest econometrics.
