# 📦 Alibaba RFQ Scraper (UAE)

## 📌 Overview

This project is a Python-based web scraper that extracts **Request For Quotation (RFQ)** listings from [Alibaba Sourcing - UAE](https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y). The scraper collects data from multiple pages and saves it into a structured CSV file.

It is designed for reliability using `undetected-chromedriver` to bypass bot detection and supports automated data extraction for procurement analysis, sourcing research, or internal reporting.

---

## 🚀 Features

- ✅ Scrapes RFQ listings from Alibaba UAE
- ✅ Captures product name, description, quantity, country, etc.
- ✅ Handles JavaScript-rendered content
- ✅ Saves results to `output.csv`
- ✅ Supports pagination (currently set to 3 pages)

---

## 📂 Project Structure

```
Alibaba_rfq/
│
├── data/
│   └── output.csv              # Extracted RFQ data (final result)
│
├── src/
│   ├── scraper.py              # Main scraping script
│   └── chromedriver.exe        # ChromeDriver binary
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 📊 Output Fields

Each RFQ record in `data/output.csv` contains:

- `Product Name`
- `Description`
- `Quantity`
- `Unit`
- `Country`
- `Date Posted`
- `Quotes Left`
- `Buyer Name`
- `Email Verified`

---

## ⚙️ Installation

### 1. Clone or Extract Project Folder
```bash
cd Alibaba_rfq
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Make sure ChromeDriver matches your Chrome version
Place `chromedriver.exe` in the `src/` folder or add it to system `PATH`.

### 4. Run the Scraper
```bash
python src/scraper.py
```

---

## 📝 Notes

- ✅ Tested with Chrome version 138 and Python 3.12+
- ⚠️ Make sure you have an active internet connection
- 🚫 Do not run the scraper too frequently to avoid IP blocks
- 👁 You can disable headless mode to visually debug (`scraper.py` line 18)

---

## 📧 Contact

**Author:** Sachin Sahu AKA Hey._.Dev  
**Submission:** Internship Assignment  
**Deadline:** 13 July 2025  
**Contact:** personaluse78265@gmail.com
