# HNG STAGE 1 - Number Classification API

An API that returns mathematical properties and fun facts about integers.

## Technologies

- Programming Language: Python
- API Framework: FastAPI
- Server: Uvicorn
- Deployment: Render
- External API: [Number API](http://numbersapi.com)

## API Endpoint
**Live Deployment**:  
`GET https://number-api-ipe8.onrender.com/api/classify-number?number=<integer>`

**Local Development**:  
`GET http://localhost:8000/api/classify-number?number=<integer>`

---

## How to Use

### Example Request
```bash
curl "https://number-api-ipe8.onrender.com/api/classify-number?number=371"
```
### Example Response (200 ok)
```bash
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number."
}
```

### Example Error (400 Bad Request)
```bash
{
  "number": "alphabet",
  "error": true
}
```

## Local Development
### Setup Instructions
1. Clone the repository: 
    ```bash
    git clone https://github.com/your-username/git-repo.git
    cd <your-project-directory>
    ```
2. Install dependencies: 
    ```bash
    pip install -r requirements.txt
    ```
3. Run the server: 
    ```bash
    uvicorn main:app --reload
    ```
4. Test: 
    ```bash
    open: "http://localhost:8000/api/classify-number?number=371"
    ```

## 📌 Limitations

### Input Restrictions:
- The API accepts only integers as input (negative numbers are rejected).
- Decimal values (e.g, 3.14) will return a 400 error.

### Free Tier Constraints:
- Fun facts depend on the [Number API](http://numbersapi.com); if it’s down, the fact will default to a placeholder.