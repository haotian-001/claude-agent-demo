# Claude Agent SDK Demo with Custom Endpoint

A demonstration of using the Claude Agent SDK with a customized endpoint configuration via environment variables.

## Overview

This project shows how to configure the Claude Agent SDK to use a custom endpoint instead of the default Anthropic API. The SDK automatically respects standard Anthropic environment variables for endpoint redirection, making it simple to integrate with custom or proxy endpoints.

## Prerequisites

- Python 3.8 or higher (Python 3.11+ recommended)
- A custom Claude-compatible endpoint
- Authentication credentials for your custom endpoint

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/claude-agent-demo.git
   cd claude-agent-demo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file and set your credentials:
   ```env
   ANTHROPIC_BASE_URL=https://your-custom-endpoint.com
   ANTHROPIC_API_KEY=your-api-key-here
   MODEL_NAME=claude-sonnet-4-5
   ```

## Usage

Run the demo script:

```bash
python demo.py
```

### Expected Output

```
============================================================
Claude Agent SDK Demo - Custom Endpoint Configuration
============================================================

Configuration:
  Base URL: https://your-custom-endpoint.com
  Model: claude-sonnet-4-5
  API Key: Set (✓)

Validating environment variables...
✓ Environment validation passed

============================================================
Sending query to Claude...
============================================================

[Response from Claude will appear here]

============================================================
Demo completed successfully!
============================================================
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_BASE_URL` | Yes | Your custom endpoint URL |
| `ANTHROPIC_API_KEY` | Yes | Your API key for authentication |
| `MODEL_NAME` | No | Claude model to use (default: `claude-sonnet-4-5`) |

### How Environment Variable Redirection Works

The Claude Agent SDK automatically respects these environment variables:
- When `ANTHROPIC_BASE_URL` is set, the SDK redirects API calls to your custom endpoint
- `ANTHROPIC_API_KEY` contains your authentication credentials
- No code changes are needed - the SDK handles everything automatically

## GitHub Actions CI/CD

This repository includes a GitHub Actions workflow that tests the demo on GitHub's standard runners.

### Setup

1. **Configure Repository Secrets**

   Go to your repository Settings → Secrets and variables → Actions, and add:

   - `ANTHROPIC_BASE_URL` - Your custom endpoint URL
   - `ANTHROPIC_API_KEY` - Your API key for authentication
   - `MODEL_NAME` - (Optional) Model name, defaults to `claude-sonnet-4-5`

2. **Trigger the Workflow**

   The workflow runs automatically on:
   - Push to `main` branch
   - Pull requests to `main` branch

3. **View Results**

   Go to the "Actions" tab in your repository to see workflow runs and logs.

## Customization

### Change the Model

Edit your `.env` file:
```env
MODEL_NAME=claude-opus-4-5
```

Available models:
- `claude-opus-4-5` - Most capable
- `claude-sonnet-4-5` - Balanced performance and speed
- `claude-haiku-4-5` - Fastest and most cost-effective

### Modify the Query

Edit [demo.py](demo.py) line 80-82 to change the prompt:
```python
async for message in query(
    prompt="Your custom prompt here",
    options=options
):
```

### Add More Agent Options

See the [Claude Agent SDK documentation](https://platform.claude.com/docs/en/agent-sdk/python.md) for available options:
```python
options = ClaudeAgentOptions(
    model=os.getenv('MODEL_NAME', 'claude-sonnet-4-5'),
    permission_mode="acceptEdits",
    allowed_tools=["Read", "Write", "Edit"],
    max_turns=10,
    # ... more options
)
```

## Troubleshooting

### Error: "ANTHROPIC_BASE_URL is not set"

Make sure you've:
1. Created a `.env` file (copy from `.env.example`)
2. Set the `ANTHROPIC_BASE_URL` variable in `.env`

### Error: "ANTHROPIC_API_KEY is not set"

Make sure you've:
1. Created a `.env` file (copy from `.env.example`)
2. Set the `ANTHROPIC_API_KEY` variable with your API key

### Connection Errors

If you get connection errors:
1. Verify your custom endpoint is accessible
2. Check that `ANTHROPIC_API_KEY` is valid
3. Confirm the endpoint URL is correct (including `https://`)
4. Test the endpoint with curl or another tool first

### Model Not Found

If you get model-related errors:
1. Check that your custom endpoint supports the specified model
2. Verify the model name is spelled correctly
3. Try using a different model name

## Project Structure

```
claude-agent-demo/
├── .env.example          # Environment variable template
├── .gitignore           # Git ignore rules
├── demo.py              # Main demo script
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── .github/
    └── workflows/
        └── test.yml     # GitHub Actions workflow
```

## Resources

- [Claude Agent SDK Documentation](https://platform.claude.com/docs/en/agent-sdk)
- [Python SDK Reference](https://platform.claude.com/docs/en/agent-sdk/python.md)
- [API Documentation](https://docs.anthropic.com/)

## License

MIT License - see [LICENSE](LICENSE) file for details.
