def get_questions():
    """
    Defines the structured questions for the Fit-Base idea validation survey.
    Each dictionary represents a question, including its type, text, options,
    and optional conditional display logic.
    """
    return [
        {
            "id": "q1",
            "type": "radio",
            "text": "Do you believe Fit-Base effectively addresses a significant pain point for fitness beginners or those resuming their journey?",
            "options": ["Yes, absolutely", "To some extent", "Not really", "Unsure"],
            "key_suffix": "effectiveness",
            "section": "Understanding the Core Problem"
        },
        {
            "id": "q2",
            "type": "text_area",
            "text": "What is the most compelling aspect of Fit-Base for you?",
            "placeholder": "e.g., Personalized guidance, educational content, form focus...",
            "key_suffix": "compelling_aspect",
            "section": "Understanding the Core Problem",
            "condition": { # This question appears if q1_effectiveness has any value (i.e., it's answered)
                "depends_on": "q1_effectiveness",
                "type": "any_value"
            }
        },
        {
            "id": "q3",
            "type": "selectbox",
            "text": "Which specific feature or aspect of Fit-Base do you think would be most impactful for beginners?",
            "options": ["Select one", "Personalized Guidance/Starting Path", "Fitness Fundamentals (Knowledge Hub)",
                        "Exercise Library (Form & Technique)", "Routine Builder (Strategic)",
                        "Progress Tracking (Learning/Consistency)", "Profile Code"],
            "key_suffix": "most_impactful_feature",
            "section": "Understanding the Core Problem",
            "condition": {
                "depends_on": "q1_effectiveness",
                "type": "equals",
                "value": "Yes, absolutely"
            }
        },
        {
            "id": "q4",
            "type": "text_area",
            "text": "What are the main reasons you feel Fit-Base doesn't adequately address the pain points?",
            "placeholder": "e.g., Existing solutions are better, the problem isn't big enough, missing features...",
            "key_suffix": "reasons_not_effective",
            "section": "Understanding the Core Problem",
            "condition": {
                "depends_on": "q1_effectiveness",
                "type": "equals",
                "value": "Not really"
            }
        },
        {
            "id": "q5",
            "type": "text_area",
            "text": "What aspects are unclear or could be improved to make Fit-Base more compelling?",
            "placeholder": "e.g., Clarify target audience, add more specific examples, simplify concepts...",
            "key_suffix": "unclear_aspects",
            "section": "Understanding the Core Problem",
            "condition": {
                "depends_on": "q1_effectiveness",
                "type": "in",
                "value": ["To some extent", "Unsure"]
            }
        },
        {
            "id": "q6",
            "type": "radio",
            "text": "How well do you think Fit-Base differentiates itself from existing popular fitness apps (e.g., workout loggers like Hevy, general health apps)?",
            "options": ["Very well, it's unique", "Somewhat, but overlaps exist", "Not much, feels similar", "Unsure"],
            "key_suffix": "differentiation",
            "section": "Competitive Landscape & Differentiation"
        },
        {
            "id": "q7",
            "type": "text_area",
            "text": "Which existing apps does Fit-Base remind you of, and why?",
            "placeholder": "e.g., It feels like X because of Y, but it lacks Z...",
            "key_suffix": "similar_apps",
            "section": "Competitive Landscape & Differentiation",
            "condition": {
                "depends_on": "q6_differentiation",
                "type": "equals",
                "value": "Not much, feels similar"
            }
        },
        {
            "id": "q8",
            "type": "slider",
            "text": "On a scale of 1 to 10, how likely would you be to use a platform like Fit-Base (1 = Not at all, 10 = Extremely likely)?",
            "min_value": 1,
            "max_value": 10,
            "default_value": 5,
            "help": "Rate your likelihood of using Fit-Base.",
            "key_suffix": "likelihood_to_use",
            "section": "Overall Impression & Likelihood"
        },
        {
            "id": "q9",
            "type": "text_area",
            "text": "Do you have any other comments, suggestions, or concerns about Fit-Base?",
            "placeholder": "e.g., Ideas for new content, pricing thoughts, target audience clarity...",
            "key_suffix": "additional_comments",
            "section": "Overall Impression & Likelihood"
        }
    ]

