import re
import os

def read_file(filepath):
    """Reads the content of a text file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Error: The file '{filepath}' does not exist.")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if not content.strip():
        print(f"Warning: The file '{filepath}' is empty.")
        
    return content

def extract_emails(text):
    """Extracts email addresses from text using a regular expression."""
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

def remove_duplicates(emails):
    """Removes duplicate emails while preserving case-insensitivity."""
    unique_emails = set()
    cleaned_emails = []
    
    for email in emails:
        lower_email = email.lower() 
        if lower_email not in unique_emails:
            unique_emails.add(lower_email)
            cleaned_emails.append(lower_email)
            
    return cleaned_emails

def save_emails(filepath, emails):
    """Saves the list of emails to the specified file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            for email in emails:
                file.write(f"{email}\n")
        return True
    except PermissionError:
        print(f"Error: You do not have permission to write to '{filepath}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while saving: {e}")
    return False

def display_results(emails, output_file):
    """Displays the extracted emails and statistics."""
    print("\nEmails found:")
    if not emails:
        print("None")
    else:
        for i, email in enumerate(emails, 1):
            print(f"{i}. {email}")
            
    print(f"\nTotal unique emails: {len(emails)}")
    
    if emails:
        print("\nSaving results...")
        print(f"Output saved to: {output_file}")
        print("\nSUCCESS!")

def main():
    """Main function coordinating the email extraction automation."""
    input_file = "input.txt"
    output_file = "extracted_emails.txt"
    
    print("========================================")
    print("       EMAIL EXTRACTOR AUTOMATION       ")
    print("========================================")
    
    print(f"\nReading file: {input_file}")
    
    try:
        
        content = read_file(input_file)
        
        
        print("Searching for email addresses...")
        raw_emails = extract_emails(content)
        
     
        unique_emails = remove_duplicates(raw_emails)
        
       
        display_results(unique_emails, output_file)
        
       
        if unique_emails:
            save_emails(output_file, unique_emails)
            
    except FileNotFoundError as e:
        print(f"\n{e}")
        print("Please create the 'input.txt' file in this directory and try again.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
