# PUBLIC API

## Project Description
This project is a Flask application that provides an API endpoint to return user information, including an email, a timestamp, and a GitHub URL.

## Setup Instructions
# 1 CLONE THE REPOSITORY
```bash
git clone https://github.com/Temake/HNG_PROJECT1.git
cd your-repo
```
# 2 INSTALL THE REQUIRED PACKAGES

```bash
pip install -r requirements.txt
```
# 3 Run the application
```bash
python main.py
```
The application will be accessible at `http://localhost:5000/`.

## API Documentation

### Endpoint URL
- `GET /`

### Request Format
- A simple GET request.

### Response Format
- JSON containing the user's email, current timestamp, and GitHub URL.

### Example Usage
A GET request to `http://localhost:5000/` will return the following JSON response:

```json
{
    "email": "teminioluwaopemipo@gmail.com",
    "timestamp": "2023-10-01T12:00:00Z",
    "github_url": "https://github.com/Temake/HNG_PROJECT1"
}
