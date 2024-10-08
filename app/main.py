from fastapi import FastAPI
from fastapi_pagination import add_pagination
from app.database.connection import init_db
from app.views import bankaccount, dealer, farmer, order

app = FastAPI()
#add_pagination(app)

init_db()

app.include_router(farmer.router, prefix="/api/v1/farmers")
app.include_router(dealer.router, prefix="/api/v1/dealers")
app.include_router(bankaccount.router, prefix="/api/v1/bankaccounts")
#app.include_router(farms.router, prefix="/api/v1/forms")
app.include_router(order.router, prefix="/api/v1/orders")
