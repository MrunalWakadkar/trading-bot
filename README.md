# Binance Futures Testnet Trading Bot (Python)

A simple Python CLI application to place orders on **Binance Futures Testnet (USDT-M)** with clean structure, input validation, logging, and error handling.

This project was built as part of a technical screening task.

---

## 🚀 Features

- Place **MARKET** and **LIMIT** orders on Binance Futures Testnet (USDT-M)
- Supports both **BUY** and **SELL**
- Clean, reusable project structure (API client + service layer + CLI)
- CLI input validation using argparse
- Proper exception handling for:
  - Invalid inputs  
  - API errors  
  - Network failures  
- Logs API requests, responses, and errors to a file
- Clear console output:
  - Order request summary  
  - Order response (orderId, status, executedQty, avgPrice if available)  
  - Success / failure messages  

---

## 📁 Project Structure

