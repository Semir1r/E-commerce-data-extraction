# E-commerce-data-extraction

## Project Overview
This project focuses on building a pipeline to ingest and preprocess data from Ethiopian Telegram e-commerce channels and prepare it for Named Entity Recognition (NER). The tasks involve setting up a data ingestion system, preprocessing text data, and labeling a subset of the dataset in CoNLL format.

---

## Task 1: Data Ingestion and Preprocessing

### Objective
Create a system to fetch messages, images, and documents from at least five Ethiopian-based Telegram e-commerce channels, preprocess the raw data, and store it in a structured format for further analysis.

### Steps

1. **Identify Relevant Telegram Channels**
   - Select at least 5 e-commerce Telegram channels relevant to the Ethiopian market.
   - Ensure the channels include diverse content such as text, images, and documents.

2. **Message Ingestion System**
   - Develop a custom scraper using the Telegram API or Python libraries like `Telethon` or `Pyrogram`.
   - Fetch messages, images, and documents in real time.
   - Save the ingested data locally or in a database with metadata such as sender ID, timestamp, and message ID.

3. **Preprocess Text Data**
   - Tokenize messages into words or meaningful units.
   - Normalize text to handle Amharic-specific linguistic features such as variations in spelling and diacritics.
   - Handle missing or irrelevant data.

4. **Clean and Structure Data**
   - Separate metadata (e.g., sender, timestamp) from message content.
   - Standardize data into a consistent format for ease of analysis.

5. **Store Preprocessed Data**
   - Save the structured data in a CSV file or database.
   - Ensure fields include:
     - `Message Date`
     - `Sender ID`
     - `Message ID`
     - `Product Description`
     - `Product Tokens`

---

## Task 2: Labeling Data in CoNLL Format

### Objective
Label a subset of the dataset (30-50 messages) in CoNLL format for NER tasks to identify entities such as products, prices, and locations in Amharic text.

### Entity Types
- **B-Product**: Beginning of a product entity (e.g., "Baby bottle").
- **I-Product**: Inside a product entity (e.g., "bottle" in "Baby bottle").
- **B-LOC**: Beginning of a location entity (e.g., "Addis Abeba", "Bole").
- **I-LOC**: Inside a location entity (e.g., "Abeba" in "Addis Abeba").
- **B-PRICE**: Beginning of a price entity (e.g., "ዋገ 1000 ቭር", "በ 100 ቭር").
- **I-PRICE**: Inside a price entity (e.g., "1000" in "ዋገ 1000 ቭር").
- **O**: Tokens outside any entities.

### CoNLL Format
- Each token is labeled on its own line.
- Blank lines separate individual messages.

### Example
```
በዕረከ	B-Product
ወርበ	I-Product
ቭር	B-PRICE
1000	I-PRICE

አደይስ	B-LOC
አበባ	I-LOC
```

### Steps
1. Tokenize each message into words.
2. Label each token with its appropriate entity type.
3. Save the labeled data in a plain text file.
4. Verify the format to ensure compliance with the CoNLL standard.

### Output
Save the labeled subset in a file named `labeled_data.txt`.

---

## Tools and Libraries
- **Telegram API**: For connecting to and scraping Telegram channels.
- **Python Libraries**:
  - `Telethon` or `Pyrogram`: For Telegram scraping.
  - `pandas`: For data manipulation and storage.
  - `re`: For text preprocessing and tokenization.
  - `io`: For handling input and output operations.

---

## File Structure
```
project-directory/
|-- data/
|   |-- raw_data.csv         # Raw scraped data
|   |-- preprocessed_data.csv # Cleaned and tokenized data
|   |-- labeled_data.txt     # CoNLL formatted labeled data
|
|-- scripts/
|   |-- scraper.py           # Script for data scraping
|   |-- preprocess.py        # Script for data preprocessing
|   |-- labeler.py           # Script for labeling data
|
|-- README.md               # Project documentation
```

---

## Deliverables
1. **Ingested Data**:
   - A structured dataset containing text, metadata, and other content.
2. **Preprocessed Data**:
   - A clean and tokenized version of the dataset.
3. **Labeled Data**:
   - A subset of the dataset labeled in CoNLL format (`labeled_data.txt`).

---

## Notes
- Ensure compliance with Telegram’s terms of service while scraping data.
- Handle sensitive data such as user IDs with caution and avoid sharing private information.

