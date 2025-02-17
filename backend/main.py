from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.rainforest import router as rainforest_router
from api.health import router as health_router
import logging

app = FastAPI(title="Sway Review API")

# Routers
app.include_router(rainforest_router, prefix="/api/rainforest", tags=["Rainforest"])
app.include_router(health_router, prefix="/api/health", tags=["Health Check"])

# Exception handler
@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )