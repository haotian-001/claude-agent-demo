"""
Claude Agent SDK Demo with Custom Endpoint

This demo shows how to use the Claude Agent SDK with a customized endpoint
by setting environment variables for endpoint redirection.
"""

import asyncio
import os
import sys
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions


def validate_environment():
    """
    Validate required environment variables are properly configured.

    Returns:
        bool: True if all validations pass, False otherwise
    """
    errors = []

    # Check for required environment variables
    base_url = os.getenv('ANTHROPIC_BASE_URL')
    api_key = os.getenv('ANTHROPIC_API_KEY')

    if not base_url:
        errors.append("❌ ANTHROPIC_BASE_URL is not set")

    if not api_key:
        errors.append("❌ ANTHROPIC_API_KEY is not set")

    if errors:
        print("Environment validation failed:\n")
        for error in errors:
            print(f"  {error}")
        print("\nPlease check your .env file. See .env.example for the correct format.")
        return False

    return True


async def main():
    """
    Main demo function showing Claude Agent SDK usage with custom endpoint.
    """
    # Load environment variables from .env file
    load_dotenv()

    print("=" * 60)
    print("Claude Agent SDK Demo - Custom Endpoint Configuration")
    print("=" * 60)

    # Display configuration
    print("\nConfiguration:")
    print(f"  Base URL: {os.getenv('ANTHROPIC_BASE_URL', 'Not set')}")
    print(f"  Model: {os.getenv('MODEL_NAME', 'claude-sonnet-4-5')}")
    api_key = os.getenv('ANTHROPIC_API_KEY', '')
    print(f"  API Key: {'Set (✓)' if api_key else 'Not set (✗)'}")

    # Validate environment variables
    print("\nValidating environment variables...")
    if not validate_environment():
        sys.exit(1)

    print("✓ Environment validation passed\n")

    # Configure agent options
    options = ClaudeAgentOptions(
        model=os.getenv('MODEL_NAME', 'claude-sonnet-4-5'),
        permission_mode="acceptEdits"
    )

    # Execute simple query
    print("=" * 60)
    print("Sending query to Claude...")
    print("=" * 60)
    print()

    try:
        async for message in query(
            prompt="Hello! Please respond with a brief, friendly greeting and confirm you received this message.",
            options=options
        ):
            print(message)

        print()
        print("=" * 60)
        print("Demo completed successfully!")
        print("=" * 60)

    except Exception as e:
        print()
        print("=" * 60)
        print(f"Error occurred: {type(e).__name__}")
        print(f"Message: {str(e)}")
        print("=" * 60)
        print("\nTroubleshooting:")
        print("  - Verify your custom endpoint is accessible")
        print("  - Check that ANTHROPIC_API_KEY is valid")
        print("  - Confirm the model name is correct")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
