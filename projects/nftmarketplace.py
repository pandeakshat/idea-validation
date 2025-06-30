# questionnaires/nft_marketplace.py

def get_questions():
    return [
        {   
            "id": "nft_q1",
            "type": "radio",
            "text": "We are currently developing the idea for NFT Marketplace. Would you like to contribute your ideas? ",
            "options": ["Yes! Sounds fun", "Not Interested"],
            "key_suffix": "nft_header_custom",
            "section": "NFT Marketplace Custom"
        },
        {
            "id": "nft_q2",
            "type": "text_area",
            "text": "Share your feedback / ideas / comments:",
            "placeholder": "e.g., types of NFT, opinions, current experience, etc...",
            "key_suffix": "nft_marketplace_feedback",
            "section": "NFT Marketplace Custom"
        },
        # ... more questions specific to NFT marketplace ...
    ]