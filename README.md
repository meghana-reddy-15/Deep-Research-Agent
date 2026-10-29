# Agentic Research Assistant
### Intelligent Multi-Source Knowledge Synthesis Platform

An AI-powered research assistant designed to organize research tasks, coordinate multiple AI agents, review findings, identify information gaps, and generate structured research reports.

The project explores how Agentic AI and multi-agent workflows can simplify the research process by dividing complex questions into smaller tasks and combining the resulting findings.

## Overview

Traditional research often requires users to search multiple websites, read different sources, organize information, and prepare a final report manually.

The Agentic Research Assistant aims to automate parts of this process through an agent-based workflow. A user submits a research query, the system plans the research, executes subtasks, reviews the generated findings, identifies possible gaps, and synthesizes a report.

The current prototype demonstrates the core research workflow. Reliable source collection, evidence verification, and citation generation require further development and testing.

## Key Features

- **Research Planning:** Breaks a research question into smaller subtasks.
- **Multi-Agent Execution:** Coordinates specialized agents to work on research tasks.
- **Web Search Integration:** Uses SearXNG for web search.
- **Workflow Orchestration:** Uses LangGraph to coordinate research stages.
- **Reflection:** Reviews intermediate research outputs.
- **Research Gap Analysis:** Identifies areas that may require additional investigation.
- **Report Synthesis:** Combines findings into a structured research report.
- **Web Interface:** Provides an interface for interacting with the research assistant.

*Note: Source collection and report accuracy may vary. Evidence verification and dependable citation generation are areas for further improvement.*

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| AI Model Integration | Groq API with an OpenAI-compatible client |
| Language Model | Qwen model configured in the application |
| Workflow Orchestration | LangGraph |
| Web Search | SearXNG |
| Frontend | Existing web interface using HTML, CSS, and JavaScript assets |
| Development Environment | Visual Studio Code |
| Search Deployment | Docker for local SearXNG setup |

## System Architecture

The application follows a workflow in which the user query passes through the backend and is processed by the research workflow.

1. **User Input:** The user submits a research question.
2. **Research Planning:** The system creates a plan and divides the question into subtasks.
3. **Agent Execution:** Research agents process the assigned tasks.
4. **Information Retrieval:** The workflow can use the configured SearXNG search service.
5. **Reflection and Gap Analysis:** Intermediate findings are reviewed and potential gaps are identified.
6. **Report Synthesis:** The language model combines the findings into a report.
7. **Result Display:** The generated report is presented through the interface.

## Project Structure

Deep-Research-Agent/
├── src/
│   └── backend/
│       ├── server.py
│       ├── agents.py
│       ├── graph.py
│       ├── planning.py
│       ├── search.py
│       ├── react_agent.py
│       ├── subagent.py
│       ├── synthesis.py
│       ├── llm.py
│       ├── config.py
│       ├── models.py
│       ├── document_parser.py
│       ├── document_store.py
│       └── tools.py
├── benchmarks/
├── research-output/
├── pyproject.toml
├── uv.lock
├── config.yaml.example
├── .env.example
├── .gitignore
├── README.md
└── test_groq.py
```

*The structure above highlights the main files visible in the project. Some additional files and folders may exist.*

## Requirements

- Python 3.12 or a compatible version supported by the project dependencies
- Git
- Docker, for the local SearXNG service
- A Groq API key with access to the configured model
- Internet connectivity for the API and web search services

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/meghana-reddy-15/Deep-Research-Agent.git
cd Deep-Research-Agent
```

### 2. Set up the Python environment

Create and activate a virtual environment if you do not already have one.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies using the package manager and instructions supported by the project.

If the project is configured for `uv`, use:

```bash
uv sync
```

### 3. Configure the language model

Create the required local configuration file using `config.yaml.example` as a reference. The application uses a configuration file under the user's `.deep-research` directory.

Configure the model name, API base URL, and API key according to the application's configuration format.

**Security:** Never commit API keys or private credentials to GitHub. Keep personal configuration files outside the repository or excluded by `.gitignore`.

### 4. Start SearXNG

Start the local SearXNG service using your Docker configuration and verify that it is accessible at the URL configured by the application.

### 5. Start the backend

From the project root, run:

```bash
python -m uvicorn src.backend.server:app --host 127.0.0.1 --port 8787
```

### 6. Open the application

Open the configured local application URL in your browser:

http://127.0.0.1:8787

The backend and search service must be configured correctly for the research workflow to operate.

## Current Implementation Status

The prototype demonstrates:

- Research planning and task decomposition
- Multi-agent workflow execution
- Reflection and research gap analysis
- Language-model-based report synthesis
- Backend integration with the configured search and language-model services

The following areas require further implementation, testing, or validation:

- Reliable retrieval and registration of source content
- Evidence-based factual verification
- Consistent source attribution and citation generation
- Evaluation of report accuracy and retrieval quality
- Performance improvements for long-running research tasks

## Future Enhancements

- Document-based Retrieval-Augmented Generation (RAG)
- Reliable evidence verification and source traceability
- Automatic citation generation and validation
- Improved source ranking and retrieval
- Better detection of conflicting information
- Research history and report export
- Automated evaluation of research quality and factual accuracy

## Security

- Do not upload `.env` files, API keys, passwords, or personal configuration files.
- Store credentials securely in local configuration or environment variables.
- Review files and Git history before making the repository public.

## Author

**Meghana Reddy Kurapati**

Information Science and Engineering Student

GitHub: [@meghana-reddy-15](https://github.com/meghana-reddy-15)

## License

Refer to the repository's existing `LICENSE` file for licensing terms.
