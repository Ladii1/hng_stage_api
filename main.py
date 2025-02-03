from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests
import math

app = FastAPI()

# Allow CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Check if a number is prime
def is_prime(n: int) -> bool:
    n = abs(n)  
    if n <= 1:
        return False 
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.isqrt(n) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Check if a number is a perfect number
def is_perfect(n: int) -> bool:
    n = abs(n)  
    if n <= 1:
        return False
    if n <= 1:
        return False
    sum_divisors = 1
    max_divisor = math.isqrt(n)
    for i in range(2, max_divisor + 1):
        if n % i == 0:
            sum_divisors += i
            other_divisor = n // i
            if other_divisor != i:
                sum_divisors += other_divisor
    return sum_divisors == n

# Check if a number is an armstrong number
def is_armstrong(n: int) -> bool:
    n = abs(n) 
    if n < 0:
        return False
    digits = str(n)
    length = len(digits)
    total = sum(int(digit) ** length for digit in digits)
    return total == n

def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json", timeout=2)
        data = response.json()
        return data["text"] if data["found"] else f"{n} is a number with no known fun facts."
    except requests.exceptions.RequestException:
        return f"Could not fetch fun fact for {n}."

# API Endpoint
@app.get("/api/classify-number")
async def classify_number(number: str = Query(...)):
    try:
        num = float(number)
        if not num.is_integer():
            raise ValueError
        num = int(num)
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True}
        )
    
    # Check on the negative numbers
    is_prime_num = is_prime(abs(num)) 
    is_perfect_num = is_perfect(abs(num))
    is_armstrong_num = is_armstrong(abs(num))

    properties = ["even" if num % 2 == 0 else "odd"]
    if is_armstrong_num:
        properties.append("armstrong")
    
    #JSON Response
    response_data = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(num))),
        "fun_fact": get_fun_fact(num)
    }
    return response_data

# 400 Bad Request
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"number": "invalid", "error": True}
    )

@app.api_route("/health", methods=["GET", "HEAD"])
async def health_check():
    return {"status": "ok"}