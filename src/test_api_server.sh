#! /bin/bash

curl -X POST http://45.18.173.26:41054/api/market-data \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "AAPL",
    "start_date": "2023-01-01",
    "end_date": "2024-01-01",
    "current_date": "2024-01-01"
  }'