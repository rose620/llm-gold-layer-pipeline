import os
import anthropic
from dotenv import load_dotenv

# call load_dotenv() file

load_dotenv()

def analyze_customer_feedback(raw_review_text: str) -> str:
    """
    Securely route unstructured customer feedback to Claude Haiku 4.5.
    Fetch directly from environment variables for safe open-source distribution.
    """
    # Look for variable globally on the machine running the code
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return (
            "Pipeline Blocked: Secret ANTHROPIC_API_KEY environment variable is missing. "
            "Please ensure you have configured your environment or a local .env file."
        )
        
    client = anthropic.Anthropic(api_key=api_key)
    
    system_prompt = (
        "You are an automated data-tagging model running inside a production Gold Layer pipeline. "
        "Analyze the provided customer review text and extract sentiment and corporate action items. "
        "Be completely factual and deterministic. Output your response as a tight markdown summary."
    )
    
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=400,
            system=system_prompt,
            messages=[
                {"role": "user", "content": f"Review Text: '{raw_review_text}'"}
            ]
        )
        text_outputs = [block.text for block in response.content if block.type == "text"]
        # Combine the text fragments into a single clean string
        return "".join(text_outputs)


    except anthropic.AuthenticationError:
        return "Pipeline Failed: API key is invalid or revoked."
    except Exception as e:
        return f"Pipeline Failed: Unexpected anomaly: {str(e)}"
