# questionnaires/customer_dashboard.py

def get_questions():
    return [
        {   
            "id": "cdb_q1",
            "type": "radio",
            "text": "We are currently developing the idea for Customer Dashboard. Would you like to contribute your ideas? ",
            "options": ["Yes! Sounds fun", "Not Interested"],
            "key_suffix": "cdb_custom",
            "section": "Customer Dashboard Custom"
        },
        {
            "id": "cdb_q2",
            "type": "text_area",
            "text": "Share your feedback / ideas / comments:",
            "placeholder": "e.g., types of analytics, opinions, current experience, etc...",
            "key_suffix": "cdb_feedback",
            "section": "Customer Dashboard Custom"
        },
        # ... more questions specific to cdb marketplace ...
    ]