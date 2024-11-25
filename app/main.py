import uvicorn
from fastapi import FastAPI, Depends
from app.routers import secure, public
from app.auth import get_user
from app.routers.public import router as public_router
from app.routers.secure import router as secure_router

app = FastAPI(
    title="API Reference",
    description="Detailed reference for all available API endpoints.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Public Routes",
            "description": "API routes accessible without any authentication requirements."
        },
        {
            "name": "Secure Routes",
            "description": "API routes that require authentication via an API key."
        }
    ],
)

# Include routers
app.include_router(public_router, prefix="/public", tags=["Public Routes"])
app.include_router(secure_router, prefix="/secure", tags=["Secure Routes"])

# app.include_router(
#     public.router,
#     prefix="/api/v1/public"
# )
# app.include_router(
#     secure.router,
#     prefix="/api/v1/secure",
#     dependencies=[Depends(get_user)]
# )

@app.get("/")
async def root():
    return {"message": "Hello, saya 18222051 Firsa Athaya Raissa Alifah!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)