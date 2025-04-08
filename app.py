import streamlit as st
from scrape import (
    scrape_website, 
    extract_body_content,
    clean_body_content,
    split_dom_content)
from parse import parse_to_ollama
from download_options import (
    get_csv,
    get_excel,
    get_json,
    get_pdf,
    get_word
)


st.title("AI Web Scraper")
url = st.text_input("Enter the URL", placeholder="Enter your url here:")
if st.button("Scrape website"):
    if url:
        st.write("Scraping website...")

        # Scrape the website
        html_content = scrape_website(url)
        body_content = extract_body_content(html_content)
        cleaned_content = clean_body_content(body_content)

        # Store the DOM content in streamlit session state
        st.session_state.dom_content = cleaned_content

        # Display the DOM content in an expandable text box
        with st.expander("View DOM content"):
            st.text_area("DOM content", cleaned_content)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe your task here to parse")

    if st.button("Parse description"):
        if parse_description:
            st.write("Parsing the content")

            dom_batch = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_to_ollama(dom_batch, parse_description)
            st.write(parsed_result)

            # Select format
            format_option = st.selectbox(
                "Choose the format to download the processed data:",
                ("JSON", "CSV", "Word", "PDF", "Excel")
            )

            # Download the selected format
            if st.button("Downloaad"):
                if format_option == "JSON":
                    st.download_button(
                        label="Download JSON",
                        data=get_json(parsed_result),
                        file_name="result.json",
                        mime="application/json"
                    )
                elif format_option == "CSV":
                    st.download_button(
                        label="Download CSV",
                        data=get_csv(parsed_result),
                        file_name="result.csv",
                        mime="text/csv"
                    )
                elif format_option == "Word":
                    st.download_button(
                        label="Download Word",
                        data=get_word(parsed_result),
                        file_name="result.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                elif format_option == "PDF":
                    st.download_button(
                        label="Download PDF",
                        data=get_pdf(parsed_result),
                        file_name="result.pdf",
                        mime="application/pdf"
                    )
                elif format_option == "Excel":
                    st.download_button(
                        label="Download Excel",
                        data=get_excel(parsed_result),
                        file_name="result.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
