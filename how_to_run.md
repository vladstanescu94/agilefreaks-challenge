# Coffee Shop Finder

## How to run:

1. Install Python 3.x
2. Make python virtual environment in project directory Ex:
   - Mac OS and Linux: python3 -m venv env
   - Windows: py -m venv env
3. Once you’ve created a virtual environment, you may activate it:
   - On Windows run: env\Scripts\activate.bat
   - On Mac OS / Linux run: source env/bin/activate
4. Install dependencies with: pip install -r requirements.txt
5. Run tests with: python -m unittest
6. Run coffee_shop_finder.py ex:
   - python coffee_shop_finder.py <user_latitude> <user_longitude> <csv_data_URL>
   - python coffee_shop_finder.py 47.6 -122.4 https://raw.githubusercontent.com/vladstanescu94/agilefreaks-challenge/develop/Resources/coffee_shops.csv
