import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routers import images, products

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(images.router, prefix="/images", tags=["images"])
app.mount("/image", StaticFiles(directory=os.path.abspath("static")), name="image")

@app.get("/")
def root():
    return {"health_checked": True} 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)