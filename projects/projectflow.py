def get_questions():
    return [
        # --- Section: Your Work & Focus Journey ---
        {
            "id": "intro_problem",
            "type": "markdown",
            "text": "### 🧘 Your Focus & Work Style\nLet’s start by understanding how you currently manage your time and tasks.",
        },
        {
            "id": "pm_tool_frustrations",
            "type": "text_area",
            "text": "What frustrates you most about current task or productivity tools?",
            "placeholder": "e.g. Too much clutter, too many steps, hard to stay focused...",
        },
        {
            "id": "overthinking_procrastination",
            "type": "radio",
            "text": "Do you often overthink or delay tasks due to too much planning?",
            "options": ["Yes, often", "Sometimes", "Rarely", "Never"],
        },

        # --- Section: Idea Introduction ---
        {
            "id": "intro_project_flow",
            "type": "markdown",
            "text": "### 🚀 Introducing Project Flow\nA focus-first productivity app that helps reduce mental overload, guide deep work, and streamline task decisions.",
        },
        {
            "id": "overall_concept_value",
            "type": "slider",
            "text": "How valuable is the idea of a tool that helps reduce overthinking and improve flow?",
            "min_value": 1, "max_value": 10, "default_value": 7,
        },

        # --- Core Feature Opinions (Shortened Descriptions) ---
        {
            "id": "task_mgmt_importance",
            "type": "radio",
            "text": "How important is a clean, intuitive task manager for you?",
            "options": ["Essential", "Nice to have", "I use other tools", "Not important"],
        },
        {
            "id": "pomodoro_interest",
            "type": "radio",
            "text": "Would built-in Pomodoro timers help your focus?",
            "options": ["Yes, definitely", "Maybe", "I don’t use Pomodoro", "Never tried it"],
        },
        {
            "id": "music_feature_interest",
            "type": "radio",
            "text": "Would mood-based focus music improve your productivity?",
            "options": ["Yes, I use music for focus", "Somewhat", "I prefer silence"],
        },
        {
            "id": "checklists_usefulness",
            "type": "slider",
            "text": "How helpful are reusable checklists for daily routines?",
            "min_value": 1, "max_value": 10, "default_value": 7,
        },
        {
            "id": "blocker_need",
            "type": "radio",
            "text": "Would a distraction blocker help you stay focused?",
            "options": ["Yes, very useful", "Maybe", "Not needed"],
        },
        {
            "id": "decision_presets_value",
            "type": "slider",
            "text": "How much would decision templates reduce your planning time?",
            "min_value": 1, "max_value": 10, "default_value": 6,
        },
        {
            "id": "effort_estimation_value",
            "type": "radio",
            "text": "Would simple effort labels (Quick Win, Deep Dive) help you prioritize?",
            "options": ["Yes", "Somewhat", "No"],
        },
        {
            "id": "task_breakdown_value",
            "type": "slider",
            "text": "How helpful is auto-suggested sub-task breakdown for big tasks?",
            "min_value": 1, "max_value": 10, "default_value": 8,
        },
        {
            "id": "overthinking_analytics_interest",
            "type": "radio",
            "text": "Would you value insights on overthinking or rescheduling habits?",
            "options": ["Definitely", "Maybe", "Not really"],
        },
        {
            "id": "flow_streaks_interest",
            "type": "slider",
            "text": "How motivating are streaks and visual progress stats for you?",
            "min_value": 1, "max_value": 10, "default_value": 8,
        },

        # --- Final Thoughts ---
        {
            "id": "likelihood_to_use",
            "type": "slider",
            "text": "How likely are you to try Project Flow if it were available today?",
            "min_value": 1, "max_value": 10, "default_value": 7,
        },
        {
            "id": "most_exciting_feature",
            "type": "text_area",
            "text": "Which feature excites you most about Project Flow?",
            "placeholder": "e.g., Distraction blocker, auto chunking, Pomodoro integration...",
        },
        {
            "id": "missing_features",
            "type": "text_area",
            "text": "Anything important you think is missing?",
            "placeholder": "e.g., Calendar sync, mobile app, team collaboration...",
        },
        {
            "id": "general_feedback",
            "type": "text_area",
            "text": "Any other feedback or thoughts?",
        }
    ]