def main():
    print("\n\nHello, World from scraper.py!\n\n")
    
    ascii_art = r"""
  ____                      _                          
 / ___|  ___  __ _ _ __ ___| |__   ___ _ __ ___   __ _ 
 \___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '_ ` _ \ / _` |
  ___) |  __/ (_| | | | (__| | | |  __/ | | | | | (_| |
 |____/ \___|\__,_|_|  \___|_| |_|\___|_| |_| |_|\__,_|
    """
    print(ascii_art)
    print("Welcome to the Job Search App (Python Edition)!")
    print("================================================\n")

    # --- Explanation of the app's purpose ---
    print("This program will:")
    print(" - Display a fun ASCII-art welcome message.")
    print(" - Explain the app’s purpose.")
    print(" - Later, scrape data from university websites (like XULA’s mission statement).")
    print(" - Practice using BeautifulSoup and requests in Python.\n")
    print("Let's begin!\n")


if __name__ == "__main__":
    main()