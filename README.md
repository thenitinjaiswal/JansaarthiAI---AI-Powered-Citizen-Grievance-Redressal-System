# JansaarthiAI---AI-Powered-Citizen-Grievance-Redressal-System


🛠️ Setup Instructions

Step 1: API Integration
------------------------

To enable the core functionalities, integrate the following IBM Watson services using their respective API keys:

🔍 Watson Natural Language Understanding (NLU)
- Used for analyzing linguistic features from transcribed audio.
- Ensure the service instance is created on IBM Cloud and the API Key & URL are noted.

🗣️ Watson Speech to Text (STT)
- Converts spoken audio into written text for further natural language analysis.
- API credentials are similarly required from IBM Cloud.

Note: Store API keys securely using environment variables or a config file (e.g., `.env`).


Step 2: Clone the Repository
-----------------------------

git clone https://github.com/thenitinjaiswal/JansaarthiAI---AI-Powered-Citizen-Grievance-Redressal-System 

Install required dependencies (if using Python):

pip install -r requirements.txt


Step 3: Audio Input Format
---------------------------

IBM Watson NLU accepts mostly `.flc` (Free Lossless Codec) audio files for processing.
To facilitate testing and integration, a sample `.flc` file is provided in the repository under:

/sample_audio.flc

You can replace it with your own `.flc` files or convert audio using a suitable encoder (e.g., FFmpeg).
