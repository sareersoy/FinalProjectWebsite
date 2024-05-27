import streamlit as st
import base64

def get_file_content_as_base64(path):
    try:
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()
    except FileNotFoundError:
        print(f"Error: File not found at path {path}")
        return None

# Setting page configuration with a wider layout
st.set_page_config(page_title='Project Introduction Website', layout='wide')

# Custom CSS for overall styling and fancy effects
st.markdown("""
<style>
body {
    color: #fff;
    background-color: #0e1117;
    font-family: 'Calibri', sans-serif;
}
h1, h2, h3, h4 {
    color: #ff6347;
    font-weight: bold;
}
h1 {
    font-size: 42px;
}
h2 {
    font-size: 32px;
}
h3 {
    font-size: 28px;
}
a {
    color: #f9a825;
    font-weight: bold;
}
.sidebar .sidebar-content {
    background-color: #1e2128;
}
.streamlit-expanderHeader {
    color: #fb8500;
}
.streamlit-expander {
    background-color: #262b33;
}
div.block-container {
    padding: 2rem;
}
div[data-testid="stBlock"] {
    background-color: #33383d;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 4px rgba(0,0,0,0.15);
    padding: 20px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title and Introduction on the Homepage
st.title('NameCheck AI: Real-Time Name Validation')
st.markdown(
    'An innovative project leveraging **DistilBERT models** to enhance data integrity through the validation of names in English and Spanish.',
    unsafe_allow_html=True)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ['Homepage', 'About', 'Objectives', 'Methodology', 'Results', 'FAQ', 'Contact'])

if page == 'Homepage':
    st.header('Welcome to the NameCheck AI Project')
    st.subheader('Quick Overview')
    st.markdown("""
    At its core, **NameCheck AI** leverages sophisticated **DistilBERT models** to perform real-time validation of names, ensuring they represent legitimate entries rather than inaccuracies or fabrications. Initially focusing on English and Spanish, the project aims to expand to additional languages, making this technology accessible on a global scale.

    This project is not just about technical excellence but also about practical impact. By enhancing the process of name validation, NameCheck AI plays a pivotal role in improving data quality across numerous platforms and applications. Whether it's enhancing user registration processes, securing transactions, or ensuring the accuracy of user-generated content, NameCheck AI provides a critical layer of trust and reliability.

    Utilizing an intuitive interface developed with Streamlit, NameCheck AI makes it easy for users to benefit from this advanced technology. The system has been designed from the ground up to be user-friendly, ensuring that individuals and organizations can easily integrate and benefit from its capabilities.
    """, unsafe_allow_html=True)

    # YouTube Link
    st.header('Watch Our Project Overview')
    st.markdown('Check out this detailed overview of our project on YouTube:', unsafe_allow_html=True)
    video_url = 'https://www.youtube.com/watch?v=yhXnLgJJBAA&ab_channel=SareBayraktutan'  # Replace with your actual YouTube video ID
    st.video(video_url)

    # Download Poster
    st.header('Download Poster')
    poster_path = "Report.pdf"  # Ensure this is the correct relative path to the PDF file in your repository
    base64_pdf = get_file_content_as_base64(poster_path)
    
    if base64_pdf is not None:
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="600" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
        st.markdown(
            f'<a href="data:application/pdf;base64,{base64_pdf}" download="Report.pdf">Click here to download the poster</a>',
            unsafe_allow_html=True
        )

if page == 'About':
    st.header('About the Project')
    st.write("""
    **NameCheck AI** emerged from the growing need to validate personal name entries across various digital platforms accurately. In an era where data drives crucial business decisions and user interactions, maintaining data integrity is more important than ever. Incorrect, fabricated, or random name entries can cause significant data integrity issues, leading to faulty analytics and operational inefficiencies.

    Our solution, powered by advanced AI, specifically targets this challenge. By utilizing state-of-the-art machine learning models, NameCheck AI offers a robust mechanism to distinguish between genuine names and potential errors or fabrications. This capability is critical for applications involving user management, security checks, and data cleansing processes where name data accuracy is essential.

    Through innovative technology and a focus on real-world applications, NameCheck AI not only enhances the reliability of data but also facilitates better user experiences and operational workflows. It represents a significant step forward in the field of data validation, blending cutting-edge AI with practical deployment strategies to address a common yet critical challenge.
    """)

if page == 'Objectives':
    st.header('Project Objectives')
    st.write("""
    Our project, NameCheck AI, is designed with several critical objectives in mind, aiming to push the boundaries of data validation through AI-driven techniques:

    1. **Develop Robust AI Models**: We aim to develop two advanced DistilBERT models fine-tuned to accurately discern authentic names from inaccuracies or fabrications in English and Spanish. This objective involves not only training the models on extensive, diverse datasets but also ensuring they can adapt to real-world variations and nuances in name data.

    2. **Enhance Data Validation**: By implementing these AI models, our goal is to significantly improve the reliability and accuracy of name data input across various digital platforms. This enhancement is particularly crucial in contexts where data integrity directly influences operational outcomes and user experiences.

    3. **Optimize Real-Time Processing**: A key objective is to optimize the system to provide instant feedback on name validation. This will enhance user interactions by reducing wait times and improving the efficiency of data entry processes in real-time applications.

    4. **Scalability and Integration**: We are committed to ensuring that our solution can scale effectively and be seamlessly integrated with existing and future systems. This involves developing a framework that supports easy implementation and maintenance.

    5. **Expand Language Coverage**: Although initially focusing on English and Spanish, we plan to extend our models to include other major languages, thereby broadening the applicability of NameCheck AI globally.
    """)

if page == 'Methodology':
    st.header('Methodology')
    st.write("""
    The methodology behind NameCheck AI is grounded in state-of-the-art machine learning techniques and best practices in software development:

    1. **Model Training and Refinement**: Our models are based on the DistilBERT architecture, known for its efficiency in processing language data. Training involved several iterative cycles where models were exposed to a wide array of name datasets sourced from Kaggle and augmented with synthetic data generated via the Faker library to simulate diverse realistic scenarios.

    2. **Data Preparation and Processing**: Significant effort was dedicated to preparing and processing the data, ensuring a balanced representation of various name types and cultural nuances. This process was critical in training our models to handle real-world variability in name data.

    3. **Real-Time Interaction Capability**: The system's architecture was designed to support real-time interaction, with a focus on minimizing response times. Optimization techniques were applied to streamline data processing and model inference.

    4. **Frontend Development**: Using Streamlit, we developed a user-friendly interface that allows users to interact with the models easily. This interface supports quick data input and visualization of the validation results, providing an intuitive experience for end-users.

    5. **Continuous Testing and Integration**: Throughout development, we conducted continuous testing to ensure the models' accuracy and the system's reliability. This included automated tests for performance benchmarks and user acceptance testing to gather feedback for improvements.
    """)

if page == 'Results':
    st.header('Results and Findings')
    st.write("""
    NameCheck AI has demonstrated significant achievements in its development and deployment:

    1. **Model Accuracy and Efficiency**: The English and Spanish DistilBERT models achieved an accuracy rate exceeding 95%, successfully identifying authentic names versus synthetic inputs. The models also maintained high efficiency, with the ability to process queries in real-time, typically responding within milliseconds.

    2. **User Feedback and System Usability**: Initial user testing yielded overwhelmingly positive feedback, with users praising the system's quick response times and high accuracy. The Streamlit-powered frontend was noted for its ease of use and intuitive design, making it accessible to users with varying levels of technical expertise.

    3. **Performance Under Load**: Further tests on system scalability revealed that NameCheck AI could handle significantly increased loads without a notable decrease in performance. This ensures that the system can be deployed in high-demand environments without losing its effectiveness.

    4. **Ongoing Optimizations**: Despite the successes, minor delays were noted during peak load times, which have become focal points for ongoing optimizations. Efforts are currently underway to enhance the models' processing speeds and reduce any potential lags to ensure seamless user experiences.

    5. **Future Plans**: Based on current results, there are plans to expand the models' language support and integrate additional features based on user feedback and emerging needs in the field of data validation.
    """)

if page == 'FAQ':
    st.header('Frequently Asked Questions')
    st.write("""
             **Q: How accurate are the models?**
             A: Both models achieve over 95% accuracy under test conditions.

             **Q: Can the system handle names from other languages?**
             A: Currently, it supports English and Spanish, with plans to expand to other languages.

             **Q: What technology is the frontend built with?**
             A: The frontend is developed using Streamlit, which allows for rapid prototyping and deployment of data applications.
             """)

if page == 'Contact':
    st.header('Contact Us')
    st.write("""
             For more information or to inquire about potential collaborations, please contact us at:
             - Email: [info@namecheckai.com](mailto:info@namecheckai.com)
             - GitHub: [Visit our repository](https://github.com)
             """)
