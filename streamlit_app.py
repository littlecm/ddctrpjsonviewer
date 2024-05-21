import streamlit as st
import json

st.title("JSON Viewer")

# File upload
uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    # Read the file
    content = uploaded_file.read().decode("utf-8")
    
    # Parse the JSON data
    try:
        data = json.loads(content)
        
        st.subheader("Parsed JSON Data")
        
        # Display each item in the JSON data
        for item in data:
            if "targetedResultsPage" in item:
                page_info = item["targetedResultsPage"]
                path_info = item["paths"].get("en_US", "N/A")
                
                st.markdown(f"**Page URL:** {path_info}")
                st.markdown(f"**Make:** {page_info.get('make', 'N/A')}")
                st.markdown(f"**Model:** {page_info.get('model', 'N/A')}")
                st.markdown(f"**Type:** {page_info.get('type', 'N/A')}")
                st.markdown(f"**Site ID:** {page_info.get('siteId', 'N/A')}")
                st.markdown(f"**Committed By:** {page_info.get('commitedBy', 'N/A')}")
                st.markdown(f"**Timestamp:** {page_info.get('timestamp', 'N/A')}")
                st.markdown("---")
                
    except json.JSONDecodeError:
        st.error("The uploaded file is not a valid JSON file.")
else:
    st.info("Please upload a JSON file to view its contents.")
