import streamlit as st
import json
import importlib.util
import os
import sys
import requests

# --- Helper Functions ---
def load_project(project_module_name):
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
    except Exception as e:
        st.error(f"Error loading project: {e}")
        return None

def save_response_to_supabase(data_to_save, db_alias, table_name):
    try:
        supabase_url = st.secrets[db_alias]["SUPABASE_URL"]
        supabase_key = st.secrets[db_alias]["SUPABASE_KEY"]
        endpoint = f"{supabase_url}/rest/v1/{table_name}"
        headers = {
            "apikey": supabase_key,
            "Authorization": f"Bearer {supabase_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "project_code": data_to_save.get("project_code", "N/A"),
            "project_name": data_to_save.get("project_name", "N/A"),
            "survey_responses_json": data_to_save.get("survey_data", {})
        }
        response = requests.post(endpoint, headers=headers, json=payload)

        if response.status_code == 201:
            st.success("🎉 Successfully submitted your feedback to Supabase!")
        else:
            st.error(f"❌ Upload failed. Status: {response.status_code}")
            st.json(response.json())

    except Exception as e:
        st.exception(e)

def reset_survey_state():
    keys = [
        'page', 'project_code_current', 'project_name_current',
        'survey_data_collected', 'current_project',
        'current_db_alias', 'current_table_name'
    ]
    for k in keys:
        st.session_state.pop(k, None)

# --- UI Setup ---
st.set_page_config(page_title="Idea Validation System", layout="wide")

st.title("💡 Idea Validation System")

st.session_state.setdefault("page", "code_input")
st.session_state.setdefault("survey_data_collected", {})

VALID_PROJECT_CODES = {
    "FIT101": {"name": "Fit-Base Validation", "module": "fitbase", "db_alias": "supabase_db", "table_name": "fitbase"},
    "CUSTOMER202": {"name": "Customer Analytics", "module": "customerdashboard", "db_alias": "supabase_db", "table_name": "customerdashboard"}
}

if st.session_state.page == "code_input":
    st.subheader("Enter Project Code")
    project_code = st.text_input("Project Code:", placeholder="e.g., FIT101").strip().upper()

    if st.button("Start Survey"):
        if project_code in VALID_PROJECT_CODES:
            info = VALID_PROJECT_CODES[project_code]
            project_data = load_project(info["module"])

            if project_data:
                st.session_state.update({
                    "project_code_current": project_code,
                    "project_name_current": info["name"],
                    "current_db_alias": info["db_alias"],
                    "current_table_name": info["table_name"],
                    "current_project": project_data,
                    "survey_data_collected": {},
                    "page": "survey_questions"
                })
                st.rerun()
        else:
            st.error("Invalid project code. Try again.")

elif st.session_state.page == "survey_questions":
    st.header(f"Survey for: **{st.session_state.project_name_current}**")
    st.markdown("Your input is incredibly valuable to help us refine this project.")
    st.markdown("---")

    questions_by_section = {}
    for q in st.session_state.current_project:
        section = q.get("section", "General")
        questions_by_section.setdefault(section, []).append(q)

    for section_title, questions in questions_by_section.items():
        with st.expander(section_title, expanded=True):
            for q_data in questions:
                q_type = q_data.get("type")
                question_text = q_data.get("text")
                key_suffix = q_data.get("key_suffix")
                widget_key = f"{q_data['id']}_{key_suffix}" if key_suffix else q_data['id']

                condition = q_data.get("condition")
                show = True
                if condition:
                    ref = st.session_state.survey_data_collected.get(condition["depends_on"])
                    if condition["type"] == "equals" and ref != condition["value"]:
                        show = False
                    elif condition["type"] == "in" and ref not in condition["value"]:
                        show = False
                    elif condition["type"] == "any_value" and (ref is None or ref in ["", "Select one"]):
                        show = False

                if not show:
                    st.session_state.survey_data_collected.pop(key_suffix, None)
                    continue

                if q_type == "markdown":
                    st.markdown(question_text, unsafe_allow_html=True)
                    continue

                current_value = st.session_state.survey_data_collected.get(key_suffix, q_data.get("default_value"))

                if q_type == "radio":
                    response = st.radio(
                        question_text,
                        options=q_data["options"],
                        index=q_data["options"].index(current_value) if current_value in q_data["options"] else 0,
                        key=widget_key
                    )
                elif q_type == "text_area":
                    response = st.text_area(
                        question_text,
                        placeholder=q_data.get("placeholder", ""),
                        value=current_value,
                        key=widget_key
                    )
                elif q_type == "selectbox":
                    response = st.selectbox(
                        question_text,
                        options=q_data["options"],
                        index=q_data["options"].index(current_value) if current_value in q_data["options"] else 0,
                        key=widget_key
                    )
                elif q_type == "slider":
                    response = st.slider(
                        question_text,
                        min_value=q_data.get("min_value", 0),
                        max_value=q_data.get("max_value", 10),
                        value=current_value,
                        help=q_data.get("help", ""),
                        key=widget_key
                    )
                else:
                    continue

                if key_suffix:
                    st.session_state.survey_data_collected[key_suffix] = response
    if st.button("Review & Submit"):
        st.session_state.page = "submission_review"
        st.rerun()

elif st.session_state.page == "submission_review":
    st.header("Review Your Feedback")
    st.subheader(f"Project: {st.session_state.project_name_current}")
    st.markdown("---")

    feedback = st.session_state.survey_data_collected
    for key, value in feedback.items():
        st.markdown(f"**{key.replace('_', ' ').title()}**: {value}")

    if st.button("Confirm and Submit"):
        submission = {
            "project_code": st.session_state.project_code_current,
            "project_name": st.session_state.project_name_current,
            "survey_data": feedback
        }
        save_response_to_supabase(submission, st.session_state.current_db_alias, st.session_state.current_table_name)
        st.session_state.page = "thank_you"
        st.rerun()

elif st.session_state.page == "thank_you":
    st.success("🙏 Thank you for your feedback!")
    if st.button("Start Another Survey"):
        reset_survey_state()
        st.session_state.page = "code_input"
        st.rerun()