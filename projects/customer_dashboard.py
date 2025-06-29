# project / customer_dashboard.py


def get_questions():
    """
    Defines the structured questions for the Customer Dashboard idea validation survey.
    Each dictionary represents a question, including its type, text, options,
    and optional conditional display logic.
    """
    return [
        {
            "id": "q1",
            "type": "radio",
            "text": "What is the primary goal of your customer dashboard?",
            "options": ["Data Visualization", "Customer Insights", "Performance Tracking", "Other"],
            "key_suffix": "primary_goal",
            "section": "Dashboard Overview"
        },
        {
            "id": "q2",
            "type": "text_area",
            "text": "Describe the key metrics or data points you want to track in your dashboard:",
            "placeholder": "e.g., Sales figures, customer engagement, support tickets...",
            "key_suffix": "key_metrics",
            "section": "Metrics Definition"
        },
        {
            "id": "q3",
            "type": "selectbox",
            "text": "Who is the primary user of this dashboard?",
            "options": ["Select one", "Business Owners", "Marketing Teams", "Support Teams", "Executives"],
            "key_suffix": "primary_user",
            "section": "User Identification"
        },
        {
            "id": "q4",
            "type": "text_area",
            "text": "What features do you consider essential for your customer dashboard?",
            "placeholder": "",
            "key_suffix": "essential_features",
            "section": "Feature Prioritization"
        },
        {
            # This question appears if q1_primary_goal has any value (i.e., it's answered)
            # It allows users to specify additional goals not listed in q1
            # The condition is illustrative; actual implementation may vary.
            # Adjust according to your actual logic and framework capabilities.
            "_condition_":{
                "_depends_on_":"q1_primary_goal",
                "_type_":"any_value"
            },
            # Note: The condition here is illustrative; actual implementation may vary.
        }
    ]