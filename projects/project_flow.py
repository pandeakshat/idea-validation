#projects / project_flow.py
# This file defines the flow of the project questionnaire, including the questions and their conditions.

def get_questions():
    return [
        {
            "id": "q1",
            "type": "radio",
            "text": "What is the primary goal of your project?",
            "options": ["Personal Use", "Community Benefit", "Commercial Product", "Research"],
            "key_suffix": "primary_goal",
            "section": "Project Overview"
        },
        {
            "id": "q2",
            "type": "text_area",
            "text": "Describe the main problem your project aims to solve:",
            "placeholder": "e.g., Lack of resources, inefficient processes, etc.",
            "key_suffix": "problem_description",
            "section": "Problem Identification"
        },
        {
            "id": "q3",
            "type": "selectbox",
            "text": "Who is your target audience?",
            "options": ["Select one", "Individuals", "Businesses", "Non-profits", "Government"],
            "key_suffix": "target_audience",
            "section": "Target Audience"
        },
        {
            "id": "q4",
            "type": "text_area",
            "text": "What are the key features or functionalities you envision for your project?",
            "placeholder": "",
            "key_suffix": "key_features",
            "section": "Project Features"
        },
        {
            "id": "q5",
            "type": "radio",
            "text": "How do you plan to validate your project's concept?",
            "options": ["Surveys", "Prototyping", 
                        {"text": "<b>Market Research</b>", 
                         "_condition_": {"depends_on": ["q1"], 
                                        "_type_":"equals", 
                                        "_value_":"Commercial Product"}}],
            # Note: The condition here is illustrative; actual implementation may vary.
            # It assumes that if q1 is 'Commercial Product', this option becomes available.
            # Adjust according to your actual logic and framework capabilities.
            "_condition_":{
                "_depends_on_":"q1_primary_goal",
                "_type_":"equals",
                "_value_":"Commercial Product"
            },
            # This condition is illustrative; adjust according to your actual logic and framework capabilities.
        }
    ]