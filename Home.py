import streamlit as st
from sqlalchemy import text
import json
import pandas as pd
import importlib.util
import os
import sys

# --- Dynamic project Loading ---
def load_project(project_module_name):
    """
    Dynamically loads a project module based on the project code.
    Assumes project files are in a 'projects' subdirectory.
    """
    # Add the 'projects' directory to the Python path
    current_dir = os.path.dirname(__file__)
    projects_dir = os.path.join(current_dir, "projects")
    if projects_dir not in sys.path:
        sys.path.insert(0, projects_dir)

    try:
        spec = importlib.util.spec_from_file_location(
            project_module_name, os.path.join(projects_dir, f"{project_module_name}.py")
        )
        if spec is None:
            raise FileNotFoundError(f"project file for '{project_module_name}' not found.")
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.get_questions()
    except FileNotFoundError as fnfe:
        st.error(f"Error loading project: {fnfe}. Make sure '{project_module_name}.py' exists in the 'projects' folder.")
        return None
    except AttributeError:
        st.error(f"Error: The project file '{project_module_name}.py' must contain a 'get_questions()' function.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred while loading project: {e}")
        return None

# --- Database Saving Function ---
def save_response_to_supabase(data_to_save, db_alias, table_name):
    """
    Saves the collected survey data to the specified Supabase PostgreSQL database
    and table.
    """
    try:
        # Establish connection dynamically based on db_alias
        # This will connect to the single database defined by 'main_project_db' alias
        conn = st.connection(db_alias, type="sql") 
        with conn.session as session:
            insertion_data = {
                "project_code": data_to_save.get('project_code', 'N/A'),
                "project_name": data_to_save.get('project_name', 'N/A'),
                "survey_responses_json": json.dumps(data_to_save.get('survey_data', {}))
            }

            columns = ", ".join(insertion_data.keys())
            placeholders = ", ".join([f":{key}" for key in insertion_data.keys()])
            # Use the dynamic table_name here
            query = text(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})")

            session.execute(query, insertion_data)
            session.commit()
        st.success("🎉 Your valuable feedback has been submitted!")
    except Exception as e:
        st.error(f"❌ An error occurred while saving your feedback to '{table_name}' in database '{db_alias}'.")
        st.exception(e) # This will print the full traceback in the Streamlit UI for debugging
        st.write("Please check your Supabase dashboard for database logs, table existence, and permissions.")


# --- Streamlit App Layout and Logic ---

st.set_page_config(
    page_title="Idea Validation System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
# Welcome to the Idea Validation System
### Your insights will help innovators validate features & products.
""")
st.markdown("---")

# --- Initialize Session State ---
if 'page' not in st.session_state:
    st.session_state.page = "code_input"
if 'project_code_current' not in st.session_state:
    st.session_state.project_code_current = ""
if 'project_name_current' not in st.session_state:
    st.session_state.project_name_current = ""
if 'survey_data_collected' not in st.session_state:
    st.session_state.survey_data_collected = {}
if 'current_project' not in st.session_state:
    st.session_state.current_project = []
if 'current_db_alias' not in st.session_state:
    st.session_state.current_db_alias = None
if 'current_table_name' not in st.session_state:
    st.session_state.current_table_name = None

# --- Configuration for Project Codes (mapping to project modules and DB tables) ---
# All projects will use the SAME 'db_alias' (e.g., "main_project_db")
# but will specify DIFFERENT 'table_name' values.
VALID_PROJECT_CODES = {
    "FIT101": {"name": "Fit-Base Validation", "module": "fit_base", "db_alias": "supabase_db", "table_name": "fitbase"},
    "CUSTOMER202": {"name": "Customer Analytics Dashboard", "module": "customer_dashboard", "db_alias": "supabase_db", "table_name": "customerdashboard"},
    "NFT301": {"name": "NFT Marketplace Insights", "module": "nft_marketplace", "db_alias": "supabase_db", "table_name": "nftmarketplace"},
    "FLOW401": {"name": "Project Flow Platform", "module": "project_flow", "db_alias": "supabase_db", "table_name": "projectflow"},
    # Remember to create corresponding project files (e.g., projects/customer_analytics.py)
    # and ensure the tables exist in your single Supabase database.
}


# --- Page: Project Code Input ---
if st.session_state.page == "code_input":
    st.subheader("Enter Your Project Code")
    st.write("Please enter the unique project code provided to access the relevant survey.")

    project_code_input = st.text_input(
        "Project Code:",
        placeholder="e.g., FIT101, CUSTOMER202, NFT301, FLOW401",
        key="project_code_field"
    ).strip().upper()

    if st.button("Start Survey", type="primary"):
        if project_code_input in VALID_PROJECT_CODES:
            project_info = VALID_PROJECT_CODES[project_code_input]
            st.session_state.project_code_current = project_code_input
            st.session_state.project_name_current = project_info["name"]
            st.session_state.current_db_alias = project_info["db_alias"] # Store DB alias (will be "main_project_db")
            st.session_state.current_table_name = project_info["table_name"] # Store specific table name

            # Load the specific project
            project_data = load_project(project_info["module"])
            if project_data is not None:
                st.session_state.current_project = project_data
                st.session_state.survey_data_collected = {} # Reset survey data for new project
                st.session_state.page = "survey_questions"
                st.rerun() # Force rerun to switch page
        elif project_code_input:
            st.error("Invalid Project Code. Please check the code and try again.")
        else:
            st.warning("Please enter a Project Code to begin the survey.")

    st.markdown("---")
    available_codes_str = ", ".join([f"`{code}`" for code in VALID_PROJECT_CODES.keys()])
    st.info(f"**Available Project Codes for Testing:** {available_codes_str}")


# --- Page: Survey Questions ---
elif st.session_state.page == "survey_questions":
    st.header(f"Survey for: **{st.session_state.project_name_current}**")
    st.markdown("Your input is incredibly valuable to help us refine this project.")
    st.markdown("---")

    # Group questions by section
    questions_by_section = {}
    for q in st.session_state.current_project:
        section = q.get("section", "General Questions")
        if section not in questions_by_section:
            questions_by_section[section] = []
        questions_by_section[section].append(q)

    # Render questions dynamically
    for section_title, questions in questions_by_section.items():
        for q_data in questions:
            question_id = q_data["id"]
            question_text = q_data["text"]
            key_suffix = q_data.get("key_suffix") # Use .get() as markdown type might not need it
            widget_key = f"{question_id}_{key_suffix}" if key_suffix else question_id # Unique key for Streamlit widget

            # Check conditional logic
            condition = q_data.get("condition")
            display_question = True
            if condition:
                # Use key_suffix for previous response lookup
                # Make sure depends_on is a key_suffix that exists in survey_data_collected
                previous_response = st.session_state.survey_data_collected.get(condition["depends_on"])
                
                if condition["type"] == "equals":
                    if previous_response != condition["value"]:
                        display_question = False
                elif condition["type"] == "in":
                    if previous_response not in condition["value"]:
                        display_question = False
                elif condition["type"] == "any_value":
                    if previous_response is None or previous_response == "Select one" or previous_response == "":
                        display_question = False
            
            if display_question:
                # Handle markdown type separately as it's for display, not input
                if q_data["type"] == "markdown":
                    st.markdown(question_text)
                    # No response to store for markdown type
                    # Ensure no old response for this markdown ID is retained if it was from a different type
                    if key_suffix in st.session_state.survey_data_collected:
                        del st.session_state.survey_data_collected[key_suffix]
                    continue # Skip to the next question in the loop

                # For interactive elements, retrieve current value for persistence
                current_value = st.session_state.survey_data_collected.get(key_suffix)
                if current_value is None: # Use default if not already in session_state
                    if q_data["type"] == "slider":
                        current_value = q_data.get("default_value", 5)
                    elif q_data["type"] == "selectbox":
                        current_value = q_data["options"][q_data.get("default_value", 0)] if q_data.get("default_value", 0) < len(q_data["options"]) else None
                    else:
                        current_value = q_data.get("default_value", "")


                if q_data["type"] == "radio":
                    selected_index = None
                    if current_value in q_data["options"]:
                        selected_index = q_data["options"].index(current_value)
                    
                    response = st.radio(
                        question_text,
                        options=q_data["options"],
                        index=selected_index,
                        key=widget_key
                    )
                elif q_data["type"] == "text_area":
                    response = st.text_area(
                        question_text,
                        placeholder=q_data.get("placeholder", ""),
                        value=current_value,
                        key=widget_key
                    )
                elif q_data["type"] == "selectbox":
                    selected_index = q_data.get("default_value", 0)
                    if current_value in q_data["options"]:
                        selected_index = q_data["options"].index(current_value)
                    
                    response = st.selectbox(
                        question_text,
                        options=q_data["options"],
                        index=selected_index,
                        key=widget_key
                    )
                elif q_data["type"] == "slider":
                    response = st.slider(
                        question_text,
                        min_value=q_data.get("min_value", 0),
                        max_value=q_data.get("max_value", 10),
                        value=current_value,
                        help=q_data.get("help", ""),
                        key=widget_key
                    )
                # Store response using its key_suffix for interactive elements
                if key_suffix: # Only store if key_suffix is defined for a response
                    st.session_state.survey_data_collected[key_suffix] = response
            else:
                # If question is not displayed, remove its response from session_state
                if key_suffix and key_suffix in st.session_state.survey_data_collected:
                    del st.session_state.survey_data_collected[key_suffix]


        st.markdown("---") # Separator between sections

    col_back, col_submit = st.columns(2)
    with col_back:
        if st.button("Back to Code Input", type="secondary"):
            st.session_state.page = "code_input"
            st.session_state.current_project = []
            st.session_state.survey_data_collected = {}
            st.session_state.current_db_alias = None
            st.session_state.current_table_name = None
            st.rerun()
    with col_submit:
        if st.button("Review & Submit Feedback", type="primary"):
            # Basic validation: Check if essential initial questions are answered
            if not st.session_state.survey_data_collected:
                 st.error("Please answer at least one question to proceed to submission review.")
            else:
                st.session_state.page = "submission_review"
                st.rerun()

# --- Page: Submission Review ---
elif st.session_state.page == "submission_review":
    st.header("Review Your Feedback")
    st.markdown("Please review your responses below before final submission. You can go back to edit if needed.")
    st.markdown("---")

    st.subheader(f"Project: **{st.session_state.project_name_current}** ({st.session_state.project_code_current})")

    display_feedback_text = ""
    # Iterate through the actual project to get question text and display responses
    # Only display questions that were actually rendered and answered
    answered_question_keys_suffix = set(st.session_state.survey_data_collected.keys())

    for q_data in st.session_state.current_project:
        # Skip markdown types in review as they don't have stored responses
        if q_data["type"] == "markdown":
            continue

        key_suffix = q_data["key_suffix"]
        question_text = q_data["text"]
        response_value = st.session_state.survey_data_collected.get(key_suffix)

        # Check if the question's key_suffix is in the collected responses
        if key_suffix in answered_question_keys_suffix and \
           response_value is not None and response_value != "Select one" and response_value != "":
            display_feedback_text += f"**{question_text}**\n- {response_value}\n\n"
    
    if not display_feedback_text:
        display_feedback_text = "No responses recorded yet. Please go back and fill out the survey."

    st.text_area(
        "Your Responses:",
        value=display_feedback_text,
        height=400,
        disabled=True,
        key="final_review_area"
    )

    st.markdown("---")

    col_edit, col_confirm = st.columns(2)
    with col_edit:
        if st.button("Edit Feedback", type="secondary"):
            st.session_state.page = "survey_questions"
            st.rerun()
    with col_confirm:
        if st.button("Confirm and Submit", type="primary"):
            full_submission_data = {
                "project_code": st.session_state.project_code_current,
                "project_name": st.session_state.project_name_current,
                "survey_data": st.session_state.survey_data_collected
            }
            save_response_to_supabase(
                full_submission_data,
                st.session_state.current_db_alias,
                st.session_state.current_table_name
            )

            st.session_state.clear()
            st.session_state.page = "thank_you"
            st.rerun()

# --- Page: Thank You ---
elif st.session_state.page == "thank_you":
    st.success("🙏 Thank you for your invaluable contribution!")
    st.markdown("Your feedback helps us build better projects for everyone.")
    st.balloons()
    st.markdown("---")
    if st.button("Start Another Survey", type="secondary"):
        st.session_state.clear()
        st.session_state.page = "code_input"
        st.rerun()

