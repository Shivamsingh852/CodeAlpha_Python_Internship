# Email Address Extractor – Python Task Automation

## Description
A practical Python automation script designed to extract all valid email addresses from a messy text file and save them neatly into an output file.

## Problem Statement
Manually searching through large text files, documents, or logs to find contact information is a tedious and time-consuming process that is highly prone to human error.

## Objective
To demonstrate the power of Python automation by building a script that reads a text file, utilizes regular expressions to automatically find email addresses, filters out duplicates, and saves the cleaned list to a new file.

## Features
- **Automatic Extraction**: Scans entire text files and isolates email addresses using regex.
- **Duplicate Removal**: Intelligently removes duplicate emails (treating `Test@Email.com` and `test@email.com` as the same).
- **Clean Output**: Exports the extracted emails into a structured `extracted_emails.txt` file.
- **Error Handling**: Gracefully handles missing files, empty files, and permission errors without crashing.

## Technologies & Python Concepts
- **Python 3**: Core language.
- **`re` module**: Python's built-in regular expression library for pattern matching.
- **File Handling**: Using `with open()` for safe reading (`'r'`) and writing (`'w'`).
- **Sets & Lists**: Using sets for fast O(1) duplicate checking while maintaining order with lists.
- **Exception Handling**: Using `try-except` blocks (e.g., `FileNotFoundError`).

## How the Automation Works
1. **Read**: The script opens `input.txt` and reads the entire string into memory.
2. **Match**: It applies the regular expression `r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'` across the text. This pattern looks for valid email characters, an `@` symbol, a domain name, and a domain extension (like `.com` or `.org`).
3. **Clean**: It converts every found email to lowercase and filters them through a `set` to remove duplicates.
4. **Save**: It creates/overwrites `extracted_emails.txt` and writes the unique emails line by line.

## Project Structure
```text
Email_Extractor_Automation/
│
├── email_extractor.py       # Main automation script
├── input.txt                # Sample text file to read from
├── extracted_emails.txt     # Generated output file (created automatically)
├── README.md                # Project documentation
└── requirements.txt         # Dependency information
```

## Input File Example (`input.txt`)
```text
Hello Team,
Please review the documents. Contact support at support@example.com.
Also, someone from Support@Example.com called.
```

## Output File Example (`extracted_emails.txt`)
```text
support@example.com
```

## Installation & Execution
This project uses only standard Python libraries. No extra installation is required.
1. Navigate to the project directory in your terminal.
2. Ensure `input.txt` exists in the folder.
3. Run the script:
   ```bash
   python email_extractor.py
   ```

## Alternative Automation Concepts
The concepts used here can easily be adapted for other automation tasks:
* **File Management**: Instead of the `re` module, you could use the `os` and `shutil` modules to scan a folder and automatically move all `.jpg` files into a separate "Images" directory.
* **Web Scraping**: Instead of reading a local text file, you could use the `requests` and `BeautifulSoup` libraries to download a webpage's HTML and extract specific data like article titles.

## Future Enhancements
- Add command-line arguments (using `sys.argv` or `argparse`) to let users specify the input and output file names dynamically.
- Add support for reading emails from `.csv` or `.docx` files.

## Author
Developed as part of the **CodeAlpha Python Programming Internship**.
