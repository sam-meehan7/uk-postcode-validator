# UK Postcode Validation and Formatting Library

This project provides an API for validating and formatting UK postcodes. It's built using FastAPI and can be deployed easily for testing and use.

## Features

- Validate UK postcodes.
- Format UK postcodes into a standard readable format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

- Python 3.6+
- FastAPI
- Uvicorn

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. **Navigate To The Directory**
   ```sh
   cd uk-postcode-validator
   ```
3. **Install Required Packages**
   ```sh
    pip install -r requirements.txt
   ```
4. **Run The Application (terminal)**

   ```sh
    python manual_run_script.py
   ```

5. **Run The Application (api)**

   ```sh
    python api.py
   ```

   In browswer hit :

   **Formatting and validating**

   ```sh
   http://localhost:8000/process/{postcode}
   ```

   **Formatting and validating with Additional Info**

   ```sh
   http://localhost:8000/details/{postcode}
   ```

## Example Postcodes To Test!

### Valid British Postcodes

1. **SW1A 1AA** - Buckingham Palace, London
2. **EH1 1YZ** - Edinburgh City Centre, Edinburgh
3. **LS1 1UR** - Leeds City Centre, Leeds
4. **G1 1XW** - Glasgow City Centre, Glasgow
5. **B1 1TB** - Birmingham City Centre, Birmingham
6. **CF10 1EP** - Cardiff City Centre, Cardiff
7. **BT1 1LT** - Belfast City Centre, Belfast
8. **M1 1AN** - Manchester City Centre, Manchester
9. **L1 1JQ** - Liverpool City Centre, Liverpool
10. **BS1 1DA** - Bristol City Centre, Bristol

### Invalid British Postcodes

1. **XX1 1XX**
2. **AB12 34D**
3. **ZZ99 9ZZ**
4. **QQ1 1QQ**
5. **1A 1A1A**
6. **G99 999**
7. **L12 345**
8. **E123 AB**
9. **WC1 999**
10. **B12 12B**
