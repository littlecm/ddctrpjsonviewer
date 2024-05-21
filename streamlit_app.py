import streamlit as st
import json
import pandas as pd

st.title("JSON Viewer and CSV Exporter")

# File upload
uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    # Read the file
    content = uploaded_file.read().decode("utf-8")
    
    # Parse the JSON data
    try:
        data = json.loads(content)
        
        st.subheader("Parsed JSON Data")
        
        records = []

        # Extract relevant information and store in a list of dictionaries
        for item in data:
            if "targetedResultsPage" in item:
                page_info = item["targetedResultsPage"]
                path_info = item["paths"].get("en_US", "N/A")
                
                record = {
                    "Page URL": path_info,
                    "Make": page_info.get('make', 'N/A'),
                    "Model": page_info.get('model', 'N/A'),
                    "Type": page_info.get('type', 'N/A'),
                    "Site ID": page_info.get('siteId', 'N/A'),
                    "Committed By": page_info.get('commitedBy', 'N/A'),
                    "Timestamp": page_info.get('timestamp', 'N/A')
                }
                
                records.append(record)
        
        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(records)
        
        # Display the DataFrame
        st.dataframe(df)
        
        # Provide a download link for the DataFrame as a CSV file
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='parsed_data.csv',
            mime='text/csv'
        )
                
    except json.JSONDecodeError:
        st.error("The uploaded file is not a valid JSON file.")
else:
    st.info("Please upload a JSON file to view its contents.")
