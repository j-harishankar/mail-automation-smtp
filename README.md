
# Mail Automation (SMTP)

A simple Python tool for automating email sending using SMTP. It includes two features:

- **Daily Motivational Quote Sender**
- **Birthday Wishes Emailer**

---

##  Features

- Sends personalized birthday emails using templates.
- Sends daily motivational quotes automatically.
- Uses environment variables for secure credential handling.
- Lightweight and easy to configure.

---

##  Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/j-harishankar/mail-automation-smtp.git
cd mail-automation-smtp
````

### 2. Setup Environment

Create a `.env` file in the project root:

```
MY_EMAIL=your-email@gmail.com
MY_PASSWORD=your-app-password
```

> **Important**: Do not commit `.env` to GitHub—add it to `.gitignore`.



### 4. Prepare Resources

* `birthdays.csv` — Add entries like:

  ```csv
  name,email,year,month,day
  Mum,jharivichu27@gmail.com,2025,08,31
  Dad,jharivichu@gmail.com,2025,08,31
  ```

* `letter_templates/` — Include files named `letter_1.txt`, `letter_2.txt`, `letter_3.txt` with the placeholder `[NAME]`.

### 5. Usage

Place your scripts in the root (e.g., `birthday_wisher.py`, `quote_sender.py`).

Run manually:

```bash
python birthday_wisher.py
python quote_sender.py
```



---

## How It Works

* **Birthday Wisher**:

  1. Reads `birthdays.csv`
  2. Builds a dictionary mapping `(month, day)` to a list of people.
  3. Picks a random template and replaces `[NAME]` with the birthday person's name.
  4. Sends the email via SMTP.

* **Quote Sender**:

  1. Fetches a motivational quote (from a list or API).
  2. Inserts the quote into an email body.
  3. Sends to your defined recipient(s) via SMTP.

---

## Security Practices

* Use **app-specific passwords** for Gmail or secure email providers.
* Store credentials in `.env` and load them using:

  ```python
  from dotenv import load_dotenv
  import os

  load_dotenv()
  MY_EMAIL = os.getenv("MY_EMAIL")
  MY_PASSWORD = os.getenv("MY_PASSWORD")
  ```
* `.env` is excluded via `.gitignore`.

---

## Project Structure

mail-automation-smtp/
│   .env                # Environment variables (email + app password)
│   .gitignore          # Ignored files for git
│   README.md           # Project documentation
│
├───automatic birthday email sender/
│   │   birthdays.csv   # Stores names, emails, and birth dates
│   │   main.py         # Script to send birthday wishes
│   │
│   └───letter_templates/
│           letter_1.txt
│           letter_2.txt
│           letter_3.txt
│
└───Email automation/
        main.py         # Script to send a random quote
        quotes.txt      # Collection of quotes

---

## Contributing

Contributions are welcome! Suggestions:

* Support for multiple quote sources (APIs, files, etc.).
* Logging (e.g., save `sent_log.txt` with timestamps).
* Support for multiple recipients or personalized templates.
* Add email validation before sending.

---

## License

MIT License. Feel free to use and modify as you wish.

---

## About

Created by Harishankar — automating daily inspiration and birthday cheer via SMTP.


