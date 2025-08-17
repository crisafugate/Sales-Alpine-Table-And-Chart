import uvicorn
from fastapi import FastAPI, Request
from routes.sales import sales_router

app = FastAPI()
app.include_router(sales_router)


if __name__ == '__main__':
    uvicorn.run('index:app', reload=True)
