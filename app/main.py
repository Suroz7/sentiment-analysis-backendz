import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.sentiment import router

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict it if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include sentiment analysis routes
app.include_router(router)

if __name__ == "__main__":
    # Get the port from Heroku environment variables (defaults to 8000 if not set)
    port = int(os.environ.get("PORT", 8000))
    
    # Run the app with Uvicorn on the dynamic port
    uvicorn.run(app, host="0.0.0.0", port=port)
