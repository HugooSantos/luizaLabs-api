from fastapi import FastAPI

from api.routers import products

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
def root():
    return {"health_checked": True} 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)