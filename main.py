import os
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from dotenv import load_dotenv
import replicate
import replicate.exceptions


# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Replicate API token
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")


# Pydantic model for input data
class ImageGenerationInput(BaseModel):
    prompt: str
    model_version: str

    class Config:
        # Disable protected namespaces to resolve the warning
        protected_namespaces = ()


# Endpoint to fine-tune a model or generate an image
@app.post("/generate-image/")
async def generate_image(data: ImageGenerationInput, response: Response):
    """
    Generate fine tune images using Replicate.
    """

    try:
        output = replicate.run(data.model_version, input={"prompt": data.prompt})
        response.status_code = status.HTTP_200_OK

    except replicate.exceptions.ReplicateException as e:
        output = str(e)
        response.status_code = status.HTTP_402_PAYMENT_REQUIRED

    except Exception as e:
        output = "something went wrong"
        response.status_code = status.HTTP_409_CONFLICT

    # Parse and return the response
    return {"result": output}
