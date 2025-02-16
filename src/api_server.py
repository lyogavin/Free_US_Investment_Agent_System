from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.market_data import market_data_agent

# Define request model
class MarketDataRequest(BaseModel):
    ticker: str
    start_date: str | None = None
    end_date: str
    current_date: str | None = None

app = FastAPI(
    title="US Investment Agent API",
    description="API server for US Investment Agent System",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to US Investment Agent API"}

@app.post("/api/market-data")
async def get_market_data_endpoint(request: MarketDataRequest):
    try:
        # Create initial state
        state = {
            "messages": [],
            "data": {
                "ticker": request.ticker,
                "start_date": request.start_date,
                "end_date": request.end_date,
                "current_date": request.current_date
            }
        }
        
        # Call the existing market_data_agent
        result = market_data_agent(state)
        return result["data"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)