# TON Address Balance Checker

## Description
This Python script automatically generates random TON addresses, checks their balance via the Toncenter API, and saves only those addresses with a balance greater than 0 TON.

## Features
- Generates random TON addresses
- Queries balance using the Toncenter API
- Displays information in the console with color formatting
- Saves found addresses with non-zero balances in `valid_ton_addresses.txt`
![изображение](https://github.com/user-attachments/assets/3e8b6d59-7aa1-412a-9c93-77cf2d0e005e)
## Installation and Execution
### 1. Install Dependencies
Before running, make sure you have the required libraries installed:
```bash
pip install requests colorama
```

### 2. Run the Script
```bash
python ton_checker.py
```
Or compiled bin files: https://github.com/btkhangvn/ton-hunter/releases/download/checker/ton_checker.zip

## Configuration
The script uses the Toncenter API to check balances. You need to replace `API_KEY` in the code with your own API key.

```python
API_KEY = "your_api_key_here"  # Replace with your API key
```

## Output File
If the script finds an address with a balance > 0 TON, it saves it in `valid_ton_addresses.txt` in the following format:
```
EQxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx: 1.23 TON (Private Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)
```



## License
This project is distributed under the MIT license. Use at your own risk.




