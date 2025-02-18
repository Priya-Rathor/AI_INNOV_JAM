from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.evaluate import router
from config import config
import uvicorn




# ----------------------------------------------------------------
#               FastAPI App Initialization
# ----------------------------------------------------------------
app = FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#----------------------------------------------------------------------------
#                          Include the router
#----------------------------------------------------------------------------
app.include_router(router) 




#-------------------------------------------------------------------------
#                          Health check endpoint
#-------------------------------------------------------------------------
@app.get("/hello")
async def hello():
    return {"message": "Hello, API is running!"}





# ----------------------------------------------------------------
#                  Run FastAPI Server
# ----------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=config.PORT)
