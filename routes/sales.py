from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from models.sales import Sales
from config.database import conn
from schemas.sales import salesRecord, listOfSalesRecords
from bson import ObjectId
from fastapi.templating import Jinja2Templates

sales_router = APIRouter()
templates = Jinja2Templates(directory='templates')

@sales_router.get('/sales', response_class=HTMLResponse)
async def find_all_sales(request: Request):
    sales = listOfSalesRecords(conn.local.sales.find())
    years = set([s['year'] for s in sales])
    context = {'request': request, 'sales': sales, 'years': years}
    return templates.TemplateResponse("sales.html", context)

@sales_router.post('/sales')
async def create_salesrecord(sales: Sales):
    conn.local.sales.insert_one(dict(sales))
    return listOfSalesRecords(conn.local.sales.find())

@sales_router.get('/sales/{salesId}')
async def get_salesrecord(salesId):
    return salesRecord(conn.local.sales.find_one({"_id": ObjectId(salesId)}))

@sales_router.delete('/sales/{salesId}')
async def delete_salesrecord(salesId):
    return salesRecord(conn.local.sales.find_one_and_delete({"_id": ObjectId(salesId)}))
