# Music-Recommendation-Engine

Music Recommendation System Installation/Setup Guide
The following step-by-step guide provides instructions for installing and setting up the Music Recommendation System on your local machine. Please follow these steps carefully to ensure a successful setup.

Prerequisites
Before you begin, make sure you have the following prerequisites installed on your system:

Python: Ensure Python is installed on your machine. If not, you can download and install it from python.org.
Step 1: Clone the Repository
Open a terminal or command prompt and clone the project repository from GitHub using the following command:

* git clone https://github.com/closgarcia/Music-Recommendation-Engine
Step 2: Navigate to the Project Directory
Move into the project directory:


* cd Music-Recommendation-Engine
Step 3: Install Dependencies
Install the required Python libraries and dependencies by running:


pip install -r requirements.txt
This command installs all the necessary packages for the project.

Step 4: Set Up Kaggle Credentials
To access the dataset, you need Kaggle credentials. If you don't have a Kaggle account, create one at Kaggle. Afterward, generate an API key from your Kaggle account settings and place it in the project directory.

Step 5: Download and Extract the Dataset
Run the following commands to download and extract the Spotify dataset:


* kaggle datasets download -d yamaerenay/spotify-dataset-19212020-600k-tracks unzip spotify-dataset-19212020-600k-tracks.zip

Step 6: Run the Streamlit App
Launch the Streamlit app by executing the following command:


* streamlit run app.py
This command will start the app, and you can access it through your web browser.

Google Colab Installation
For an easier and more accessible installation on a Google Colab notebook, follow these steps:

Create a new notebook in Google Colab.
Copy and paste the code from StreamlitApp.ipynb notebook into cells.
Cell 1: Install Dependencies - Include and run all the cells in the notebook to install the required libraries and dependencies.
Cell 2: App Code - Copy the content of app.py and paste it into the second cell.
Instructions:
Using Google Colab, upload/open StreamlitApp.ipynb found in Mr. DJ’s git repository.
Connect Google Colab’s Runtime.
Run the first cell to install the necessary libraries.
Make sure you have set up your Kaggle credentials (replace with your own).
Upload the app.py file containing the Music Recommendation Streamlit app to the Google Colab Runtime Session Storage.
Run the second cell to execute the Streamlit app.
Follow the generated URL to access the app in your browser.
Note: If running on Google Colab, keep the notebook open while interacting with the app.
