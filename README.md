# Revenue-Recovery-AI-Agent

# Project 

revenue-recovery-ai/
│
├── app/
│   ├── core/
│   │   ├── agent.py
│   │   ├── rules.py
│   │   ├── models.py
│   │   └── scoring.py
│   │
│   ├── services/
│   │   ├── analyzer.py
│   │   ├── reporter.py
│   │   ├── exporter.py
│   │   └── logger.py
│   │
│   ├── api/
│   │   └── main.py
│   │
│   ├── cli.py
│   └── config.py
│
├── data/
│   ├── sample_deals.json
│   ├── sample_invoices.json
│
├── prompts/
│   ├── system_prompt.txt
│   ├── deal_analysis_prompt.txt
│   ├── invoice_analysis_prompt.txt
│   └── prioritization_prompt.txt
│
├── tests/
│   ├── test_agent.py
│   ├── test_scoring.py
│
├── outputs/
│   └── submissions.csv
│
├── requirements.txt
├── README.md
└── run.py
