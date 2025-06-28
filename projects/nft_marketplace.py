# questionnaires/nft_marketplace.py

def get_questions():
    return [
        {
            "id": "nft_q1",
            "type": "radio",
            "text": "What type of NFT marketplace features are most important to you?",
            "options": ["Buying/Selling", "Minting", "Community", "Analytics"],
            "key_suffix": "nft_feature_priority",
            "section": "NFT Marketplace Features"
        },
        {
            "id": "nft_q2",
            "type": "text_area",
            "text": "Describe your ideal user experience for browsing NFTs:",
            "placeholder": "e.g., Filters, sorting, visual previews...",
            "key_suffix": "nft_browsing_experience",
            "section": "NFT Marketplace Features",
            "condition": {
                "depends_on": "nft_feature_priority",
                "type": "any_value"
            }
        },
        # ... more questions specific to NFT marketplace ...
    ]