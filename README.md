1. Create a virtual environment
2. Install the packages present in the requirements.txt file
3. Set the desired search keywords in user_quries.json
4. Run using main.py

# Design Documentation

The script is based on functional programming paradigm, though for the purpose of data modeling, product details were mapped to a product class.

DRY and Separation of Concerns principles were applied for creating a clean, maintainable and structured codebase

Every utility function is defined separately in a file, with proper exception handling, and circular code has been avoided

New modules can easily be added to further enhance the working of the script

The script uses Selenium in it's working, since Amazon has a strong policy against bot requests even when using proxies