## Installation

1. Clone the repository:
```
gh repo clone https://github.com/AdvaitD04/Whatappchat-analyzer.git
```

2. Navigate to the project directory:
```
cd Whatsapp-chat-analyzer
```

3. Install the required Python packages:
```
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```
streamlit run app.py
```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload a chat log file using the file uploader in the sidebar.




4. Select a user from the dropdown menu in the sidebar.

5. Click the "Show Analysis" button in the sidebar to display the analysis.

## Project Structure

- `app.py`: The main Streamlit application.

- `preprocessor.py`: Contains the `preprocess` function for preprocessing the chat log.

- `helper.py`: Contains various helper functions for the analyses.

- `stopwords.txt`: A text file containing common stopwords to be excluded from the word cloud and most common words analysis.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
