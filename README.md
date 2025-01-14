
# Movie-Recommendation-System

A Movie Recommendation System that leverages machine learning and MLOps for efficient deployment and real-time recommendations. The project integrates Streamlit to provide an interactive web interface for users to get personalized movie suggestions.

## Features
- **Movie Recommendations**: Personalized movie recommendations based on user preferences and historical data.
- **Streamlit Interface**: A clean and interactive web interface built with Streamlit for users to interact with the recommendation system.
- **MLOps Pipeline**: The project is structured using MLOps principles, ensuring seamless model deployment and management.

## Installation

### Prerequisites
Make sure you have Python 3.11.3 installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmad0303/Movie-Recommendation-System.git
   ```

2. Navigate into the project directory:
   ```bash
   cd Movie-Recommendation-System
   ```

3. Create and activate a virtual environment (optional but recommended):
   ```bash
   conda create -p rsenv python==3.11.3 # On Windows
   conda activate rsenv/ # On Windows
   ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Streamlit Setup
Once the dependencies are installed, you can start the Streamlit app by running:

```bash
streamlit run app.py
```

The Streamlit app will open in your browser, where you can interact with the recommendation system.