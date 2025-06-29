# questionnaires/fitbase.py

def get_questions():
    """
    Defines the structured questions for the Fit-Base idea validation survey.
    This version integrates problem identification and feature selling
    directly into the survey flow.
    """
    return [
        # --- Section 1: Identifying Core Pain Points (Laying the Groundwork) ---
        {
            "id": "intro",
            "type": "markdown",
            "text": "### Let's talk about your fitness journey.\n\nBefore diving into our idea, we want to understand your experiences.",
            "section": "Your Fitness Journey"
        },
        {
            "id": "current_frustrations",
            "type": "text_area",
            "text": "What are your biggest frustrations or challenges when trying to get fit or use existing fitness apps?",
            "placeholder": "e.g., Lack of guidance, don't know where to start, injury concerns, apps are just notebook/ journals....",
            "key_suffix": "current_frustrations",
            "section": "Your Fitness Journey"
        },
        {
            "id": "overwhelmed_info",
            "type": "radio",
            "text": "Do you often feel overwhelmed by the sheer volume of fitness information online (videos, articles, influencer advice)?",
            "options": ["Yes, frequently", "Sometimes", "Rarely", "Never"],
            "key_suffix": "overwhelmed_info",
            "section": "Your Fitness Journey"
        },
        # --- Section 2: Introducing Fit-Base Core (Solving the Pain Points) ---
        {
            "id": "intro_fitbase",
            "type": "markdown",
            "text": "### Introducing Fit-Base: Your Personal Fitness Guide\n\nImagine a platform designed to simplify fitness, for beginners, for people returning, and for people who feel stuck or lost. It's built to empower you with knowledge and a clear path forward.",
            "section": "Introducing Fit-Base"
        },
        {
            "id": "personalized_guidance_concept",
            "type": "markdown",
            "text": "#### Concept: Personalized Guidance & Starting Path\n\nFit-Base starts with a deep assessment of your current fitness level, goals, comfort with gyms, and exercise knowledge. It then recommends a tailored 'starting path' just for you, so you can start your own journey.",
            "section": "Introducing Fit-Base"
        },
        {
            "id": "personalized_guidance_value",
            "type": "slider",
            "text": "On a scale of 1-10, how valuable would a *truly personalized* starting path be for you in your fitness journey? (1 = Not valuable, 10 = Extremely valuable)",
            "min_value": 1, "max_value": 10, "default_value": 7,
            "help": "Think about how much this could reduce confusion or intimidation.",
            "key_suffix": "personalized_guidance_value",
            "section": "Introducing Fit-Base"
        },
        # --- Section 3: Feature Deep Dive (Educational Focus) ---
        {
            "id": "knowledge_hub_concept",
            "type": "markdown",
            "text": "#### Concept: Fitness Fundamentals (Knowledge Hub)\n\nBeyond just telling you what to do, Fit-Base provides a rich library explaining the **'why' and 'how'** of fitness – covering influencer-shared strategies and routines, nutrition basics, mindset, recovery and training principles. It's about understanding & inculcating, not just following general instructions.",
            "section": "Core Features"
        },
        {
            "id": "knowledge_hub_interest",
            "type": "radio",
            "text": "How interested are you in learning the underlying principles and 'why' behind fitness recommendations?",
            "options": ["Very interested", "Somewhat interested", "Not very interested", "I just want a plan"],
            "key_suffix": "knowledge_hub_interest",
            "section": "Core Features"
        },
        {
            "id": "exercise_library_concept",
            "type": "markdown",
            "text": "#### Concept: Exercise Library (Form & Technique)\n\nInstead of simple lists, Fit-Base focuses on teaching **proper form and technique** for exercises, highlighting common mistakes, and linking to high-quality demonstrations & research. The goal is for you to choose your exercise, powered by safe and effective movement by the platform.",
            "section": "Core Features"
        },
        {
            "id": "form_technique_importance",
            "type": "slider",
            "text": "How important is clear, detailed instruction on exercise form and technique to you? (1 = Not important, 10 = Critically important)",
            "min_value": 1, "max_value": 10, "default_value": 8,
            "help": "Consider injury prevention and exercise effectiveness.",
            "key_suffix": "form_technique_importance",
            "section": "Core Features"
        },
        # Conditional follow-up for form
        {
            "id": "form_learning_method",
            "type": "selectbox",
            "text": "What's your preferred way to learn proper exercise form?",
            "options": ["Select one", "Video demonstrations", "Step-by-step written instructions", "Infographics", "In-person coaching", "All of the above"],
            "index": 0,
            "key_suffix": "form_learning_method",
            "section": "Core Features",
            "condition": {
                "depends_on": "form_technique_importance",
                "type": "any_value" # Appears if the slider is moved or has a default value
            }
        },
        # --- Section 4: Differentiation & Overall Outlook ---
        {
            "id": "differentiation_statement",
            "type": "markdown",
            "text": "### Hoaw Fit-Base Stands Apart\n\nUnlike most apps that are primarily workout loggers (like Hevy, Strong), Fit-Base acts as your **personal fitness tutor and strategist**. It empowers you with *knowledge* to design your journey, complementing (not competing with) logging apps.",
            "section": "Differentiation & Outlook"
        },
        {
            "id": "complementary_value",
            "type": "radio",
            "text": "How valuable is an app that *teaches and strategizes* your fitness journey, separate from (but complementary to) a workout logging app?",
            "options": ["Very valuable", "Somewhat valuable", "Not very valuable", "I prefer all-in-one"],
            "key_suffix": "complementary_value",
            "section": "Differentiation & Outlook"
        },
        {
            "id": "overall_interest_fitbase",
            "type": "slider",
            "text": "Considering all aspects, on a scale of 1-10, how interested are you in using Fit-Base if it were available today? (1 = Not interested, 10 = Extremely interested)",
            "min_value": 1, "max_value": 10, "default_value": 7,
            "key_suffix": "overall_interest_fitbase",
            "section": "Differentiation & Outlook"
        },
        # --- Section 5: General Feedback ---
        {
            "id": "additional_comments",
            "type": "text_area",
            "text": "Do you have any other comments, suggestions, or concerns about Fit-Base that weren't covered?",
            "placeholder": "e.g., Thoughts on potential pricing, missing features, target audience clarity, etc.",
            "key_suffix": "additional_comments",
            "section": "General Feedback"
        }
    ]

