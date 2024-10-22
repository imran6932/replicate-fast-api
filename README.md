# FastAPI Image Generation App

This is a FastAPI application that utilizes the Replicate package to generate images based on a user-provided prompt. The app allows for fine-tuning models and generating images.

## Features

- Generate images using various models from Replicate.
- Handle different exceptions gracefully.
- Easy to extend and modify.

## Prerequisites

- Python 3.7 or later
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/imran6932/replicate-fast-api.git)
   cd replicate-fast-api
   ```
2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root and add your Replicate API token:

   ```plaintext
   REPLICATE_API_TOKEN=your_replicate_api_token
   ```

## Usage

1. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```
2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

## API Endpoint

### Generate Image

- **URL:** `/generate-image/`
- **Method:** `POST`
- **Request Body:**

```json
{
  "prompt": "A description of the image you want to generate",
  "model_version": "model_version_string"
}
```

- **Responses:**

  - **200 OK**: Returns the generated image result.
  - **402 Payment Required**: If there is an error with the Replicate API.
  - **409 Conflict**: For any other exceptions.

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/generate-image/" -H "Content-Type: application/json" -d '{"prompt": "A futuristic cityscape", "model_version": "replicate/model-version"}'
```

## License

This project is licensed under the MIT License.

## Acknowledgements

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Replicate API Documentation](https://replicate.com/docs)
