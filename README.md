# Finanical Analyst Agent
This is a simple agent that can be used to perform day analysis on a stock or cryptocurrency. It can also be used to generate a macroeconomic intelligence report on the latest econometrics.

OpenBB is a powerful tool for building and deploying agents. It provides a simple and intuitive interface for creating, testing, and deploying AI-powered agents. OpenBB is a platform akin to an open-source version of Bloomberg Terminal.

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
python agent.py -t PLTR
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

## Customizing the Agent

The agent can be customized by modifying the `prompts/fintel.py` file. This file contains functions that generate different types of prompts for the agent. You can modify these functions to generate prompts that are specific to your needs.