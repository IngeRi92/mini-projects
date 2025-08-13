# Currency Converter

A simple command-line currency converter written in Python.  
Easily convert between major world currencies using predefined exchange rates.

## Features

- Supports USD, EUR, GBP, JPY, CAD, and AUD
- User-friendly prompts and error handling
- Converts any amount between supported currencies
- Clean and readable code, easy to modify

## Usage

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run the program in your terminal:

   ```sh
   python currency_converter.py
   ```

4. Follow the on-screen instructions:
   - Choose the currency you want to convert from and to
   - Enter the amount
   - See the result and choose whether to convert again

## Example

```
Welcome to Currency Converter!

Available currencies:
  USD - US Dollar
  EUR - Euro
  GBP - British Pound
  JPY - Japanese Yen
  CAD - Canadian Dollar
  AUD - Australian Dollar
From currency: USD
To currency: EUR
Enter amount: 100
100.00 USD = 85.00 EUR
Convert another? (y/n): n
Thank you for using Currency Converter!
```

## Customization

- To update exchange rates, edit the `rates` dictionary in `currency_converter.py`.
- To add more currencies, add them to both the `rates` and `names` dictionaries.

## License

This project is open source and free to use.

---

Made for learning and demonstration purposes.