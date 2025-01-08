# Social Media Analysis Tool

## Overview
The Social Media Analysis Tool is a Streamlit-based application designed to analyze various types of social media posts such as Reels, Static posts, and Carousels. The app integrates with Astra DB and LangFlow API to perform data-driven insights and provide valuable analysis for improving social media strategies.

## Features
- **Post Type Analysis:** Analyze Reels, Static posts, and Carousels.
- **API Integration:** Seamless integration with LangFlow API for running analysis flows.
- **Data Upload:** Upload and store CSV or JSON data to Astra DB.
- **Interactive UI:** User-friendly Streamlit interface with sidebar for file uploads and a responsive main area for analysis.

## Technologies Used
- **Python 3.10+** (Note: Python 3.12 is not supported due to dependency issues with `astrapy`.)
- **Streamlit**: For creating the web application.
- **Astra DB**: For database storage and management.
- **LangFlow API**: For handling analysis flows.
- **Pandas**: For data manipulation (when uploading CSV files).
- **Requests**: For making API calls.

## Installation

### Prerequisites
- Python 3.10 or 3.11 installed on your system.
- Astra DB credentials.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/social-media-analysis-tool.git
   cd social-media-analysis-tool
   ```
2. Create and activate a virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the `secrets.toml` file:
   Create a `.streamlit/secrets.toml` file in the root of the project:
   ```toml
   [astra_token]
   ASTRA_TOKEN = "Your-Astra-DB-Token"
   ```

5. Run the application:
   ```bash
   streamlit run main.py
   ```

## File Structure
```
.
├── main.py                 # Main application file
├── requirements.txt        # Project dependencies
├── .streamlit
│   └── secrets.toml        # Secret keys (not included in the repo)
├── README.md               # Documentation
```

## Usage
1. Open the application in your browser (URL will be shown after running the app).
2. Use the **Post Type Analysis** dropdown to select the type of post.
3. Click the **Run Analyze** button to process the data.
4. Optionally, upload a CSV or JSON file to Astra DB via the sidebar.

## Known Issues
- `astrapy` does not currently support Python 3.12. Use Python 3.10 or 3.11 instead.
- Ensure the `secrets.toml` file is properly configured to avoid authentication errors.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

