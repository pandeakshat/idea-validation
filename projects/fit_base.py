# questionnaires/fitbase.py

def get_questions():
    """
    Defines the structured questions for the Fit-Base idea validation survey.
    This version is optimized for brevity, clarity, and quick completion
    based on user feedback. It prioritizes multi-choice answers and places
    open-ended questions at the end.
    """
    return [
        # --- Section 1: Identifying Core Pain Points (Quick Scan) ---
        {
            "id": "intro",
            "type": "markdown",
            "text": "### The Fitness Journey",
            "section": "Your Fitness Journey"
        },
        {
            "id": "starting_challenges",
            "type": "radio",
            "text": "What is your biggest challenge when starting or restarting a fitness routine?",
            "options": [
                "Knowing where to start or what to do",
                "Understanding proper form and technique",
                "Staying motivated or consistent",
                "Finding time or managing a busy schedule",
                "Concerns about injury",
                "Existing apps are just logging tools, not guides",
                "Other (please specify at the end of the survey)"
            ],
            "key_suffix": "starting_challenges",
            "section": "Your Fitness Journey"
        },
        # --- Section 2: Introducing Fit-Base & Core Value Proposition ---
        {
            "id": "intro_fitbase_core",
            "type": "markdown",
            "text": "### Introducing Fit-Base \n\n**Fit-Base** simplifies fitness by offering **personalized guidance** and a clear starting path. It's designed for beginners, those returning to fitness, or anyone feeling stuck.",
            "section": "Introducing Fit-Base"
        },
        {
            "id": "personalized_guidance_value_radio",
            "type": "radio",
            "text": "How valuable would a *truly personalized* starting path be for you in your fitness journey?",
            "options": [
                "Extremely valuable (a must-have)",
                "Very valuable",
                "Somewhat valuable",
                "Not very valuable",
                "Not valuable at all"
            ],
            "key_suffix": "personalized_guidance_value",
            "section": "Introducing Fit-Base"
        },
        # --- Section 3: Key Features (Focus on "Why" and "How") ---
        {
            "id": "knowledge_hub_concept_short",
            "type": "markdown",
            "text": "### Key Feature: The 'Why' and 'How' (Curated Knowledge)\n\n**Fit-Base** explains the **underlying principles** of fitness, covering nutrition basics, mindset, recovery, and training. We simplify and curate information from **multiple fitness experts and influencers** (with research) to provide up-to-date, actionable knowledge. Fit-Base is not a professional service, but a strategy tool.", # ADDED/MODIFIED THIS LINE
            "section": "Core Features"
        },
        {
            "id": "knowledge_hub_interest",
            "type": "radio",
            "text": "How interested are you in learning the underlying principles and 'why' behind fitness recommendations, *especially if simplified and curated from multiple experts*?", # MODIFIED QUESTION SLIGHTLY
            "options": ["Very interested", "Somewhat interested", "Not very interested", "I just want a plan"],
            "key_suffix": "knowledge_hub_interest",
            "section": "Core Features"
        },
        {
            "id": "exercise_library_concept_short",
            "type": "markdown",
            "text": "### Key Feature: Form & Technique\n\n**Fit-Base** focuses on teaching **proper form and technique**, highlighting common mistakes and linking to high-quality demonstrations. The goal is safe and effective movement.",
            "section": "Core Features"
        },
        {
            "id": "form_technique_importance_radio",
            "type": "radio",
            "text": "How important is clear, detailed instruction on exercise form and technique to you?",
            "options": [
                "Critically important (essential for me)",
                "Very important",
                "Somewhat important",
                "Not very important",
                "Not important at all"
            ],
            "key_suffix": "form_technique_importance",
            "section": "Core Features"
        },
        {
            "id": "form_learning_method",
            "type": "radio",
            "text": "What's your preferred way to learn proper exercise form?",
            "options": ["Video demonstrations", "Step-by-step written instructions", "Infographics", "In-person coaching", "A combination of these"],
            "key_suffix": "form_learning_method",
            "section": "Core Features",
        },
        # --- Section 4: Differentiation & Overall Outlook (Sharpens Unique Value) ---
        {
            "id": "differentiation_statement_concise",
            "type": "markdown",
            "text": "### Why FitBase \n\nUnlike most apps that are just workout loggers (e.g., Hevy, Strong), **Fit-Base** acts as your **personal fitness tutor and strategist**. It empowers you with *knowledge* to design your own journey, *complementing* (not competing with) logging apps.",
            "section": "Differentiation & Outlook"
        },
        {
            "id": "complementary_value",
            "type": "radio",
            "text": "How valuable is an app that *teaches and strategizes* your fitness journey, separate from (but complementary to) a workout logging app?",
            "options": ["Very valuable", "Somewhat valuable", "Not very valuable", "I prefer an all-in-one app"],
            "key_suffix": "complementary_value",
            "section": "Differentiation & Outlook"
        },
        {
            "id": "overall_interest_fitbase_radio",
            "type": "radio",
            "text": "Considering all aspects, how interested are you in using Fit-Base if it were available today?",
            "options": [
                "Extremely interested (would use immediately)",
                "Very interested",
                "Somewhat interested",
                "Not very interested",
                "Not interested at all"
            ],
            "key_suffix": "overall_interest_fitbase",
            "section": "Differentiation & Outlook"
        },
        # --- Section 5: General Feedback (Open-ended questions at the end) ---
        {
            "id": "current_frustrations_open",
            "type": "text_area",
            "text": "Please elaborate on your biggest frustrations or challenges when trying to get fit or use existing fitness apps (if not covered by previous options).",
            "placeholder": "e.g., Lack of guidance, don't know where to start, injury concerns, apps are just notebook/ journals....",
            "key_suffix": "current_frustrations_open",
            "section": "General Feedback"
        },
        {
            "id": "additional_comments",
            "type": "text_area",
            "text": "Do you have any other comments, suggestions, or concerns about Fit-Base that weren't covered?",
            "placeholder": "e.g., Thoughts on potential pricing, missing features, target audience clarity, etc.",
            "key_suffix": "additional_comments",
            "section": "General Feedback"
        }
    ]