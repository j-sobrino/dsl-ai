# Financial Product DSL Modeler

This project helps users extract key financial fields from UK credit contract PDFs using OpenAI, and provides a modern web interface to assist in writing DSL code that models financial products.

## Features

- **Drag & Drop PDF Upload:** Easily upload UK credit contract PDFs.
- **Automatic Extraction:** Uses OpenAI to extract fields like loan amount, monthly payment, term, total payable, interest rate, and APR.
- **JSON Output:** Displays extracted fields in raw JSON format for easy DSL modeling.
- **Modern UI:** Clean, responsive interface with drag-and-drop support.

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/financial-product-dsl-modeler.git
    cd financial-product-dsl-modeler
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Add your OpenAI API key to a `.env` file:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Running the App

1. Start the Flask server:
    ```
    python app.py
    ```

2. Open your browser and go to [http://localhost:5000](http://localhost:5000).

3. Drag and drop a PDF or select one to upload. The extracted fields will be shown in JSON format.

## Project Structure

```
dslai/
│
├── app.py                # Flask backend
├── dslai.py              # PDF extraction & OpenAI query logic
├── templates/
│   └── index.html        # Frontend UI
├── uploads/              # Uploaded PDFs
├── .env                  # Environment variables (not tracked by git)
├── .gitignore
└── README.md
```

## Dependencies

- Flask
- python-dotenv
- openai
- pdfplumber
- werkzeug

## License

MIT License

---

**Note:** This tool is for educational and prototyping purposes. Always verify extracted data before using it in production or regulatory contexts.