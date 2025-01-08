import streamlit as st
import json
import requests
from typing import Optional  # Import Optional
from astrapy import DataAPIClient

# Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "17c51730-bbc5-4a38-84ea-8253572fe1a9"  # Replace with your LangFlow ID
APPLICATION_TOKEN = st.secrets["astra_token"]["ASTRA_TOKEN"]  # Replace with your actual application token
ENDPOINT = "sp"  # The endpoint name of the flow

# Function to run the flow and get the response
def run_flow(message: str,
             endpoint: str,
             output_type: str = "chat",
             input_type: str = "chat",
             application_token: Optional[str] = None) -> dict:
    """
    Run a flow with a given message.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    
    headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    
    # Make the request to the API
    response = requests.post(api_url, json=payload, headers=headers)
    
    # Return the response as JSON
    return response.json()

# Streamlit App UI
def main():
    # Streamlit Page Configuration
    st.set_page_config(page_title="Social Media Analysis Tool", layout="wide")
    
    # Sidebar for file upload
    with st.sidebar:
        st.header("Upload Data to Astra DB")
        uploaded_file = st.file_uploader("Upload a CSV or JSON file:", type=["csv", "json"])

        def upload_to_astra(file, token, api_endpoint, collection_name):
            try:
                client = DataAPIClient(token)
                db = client.get_database_by_api_endpoint(api_endpoint)
                collection = db.get_collection(collection_name)

                # Parse and upload file
                if file.name.endswith(".csv"):
                    import pandas as pd

                    data = pd.read_csv(file)
                    collection.insert_many(data.to_dict(orient="records"))
                elif file.name.endswith(".json"):
                    data = json.load(file)
                    collection.insert_many(data)
                return "File uploaded successfully!"
            except Exception as e:
                return f"Error uploading file: {e}"

        if uploaded_file and st.button("Upload File"):
            message = upload_to_astra(uploaded_file, APPLICATION_TOKEN, "https://90a8261c-a4be-451c-96d2-4d7a202425a2-us-east1.apps.astra.datastax.com", "data")
            if "successfully" in message:
                st.success(message)
            else:
                st.error(message)
    
    # Main Content Area
    st.title("Social Media Analysis Tool📈🔍")
    post_type = st.selectbox("Choose a post type to analyze:", ["Reels", "Static", "Carousels"], index=0)
    
    # Run the flow when the button is clicked
    if st.button("Run Analyze"):
        try:
            # Make API call to run the flow
            response = run_flow(post_type, ENDPOINT, application_token=APPLICATION_TOKEN)
            
            # Check if the response has 'error' and handle accordingly
            if 'error' in response:
                st.error(f"Error: {response['error']}")
            else:
                st.success("Analysis completed successfully!")
                # Display the response with better formatting
                analysis_result = response["outputs"][0]["outputs"][0]["results"]["text"]["text"]
                st.markdown("### Analysis Result: 📋")
                st.write(analysis_result)
        
        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()
