# questionnaires/project_flow.py

def get_questions():
    return [
        {   
            "id": "pfw_q1",
            "type": "radio",
            "text": "We are currently developing the idea for Project Flow. Would you like to contribute your ideas? ",
            "options": ["Yes! Sounds fun", "Not Interested"],
            "key_suffix": "pfw_custom",
            "section": "Project Flow  Custom"
        },
        {
            "id": "pfw_q2",
            "type": "text_area",
            "text": "Share your feedback / ideas / comments:",
            "placeholder": "e.g., Flow obstacles, task issues, opinions, current experience, etc...",
            "key_suffix": "pfw_feedback",
            "section": "Project Flow Custom"
        },
        # ... more questions specific to pfw marketplace ...
    ]