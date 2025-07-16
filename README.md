# Memory_Rag: Integrate Memory into your Agent

## Description

This repository provides a starting point for integrating memory capabilities into your agent applications. It leverages Python and specific frameworks to create a system where your agent can store and retrieve information, enhancing its ability to learn and adapt over time.

## Key Features & Benefits

*   **Memory Integration:** Easily add memory functionality to your existing agent.
*   **Gemini Support:** Leverages Google's Gemini for embedding and language processing (example included, adaptable to others).
*   **Modular Design:**  Designed for flexibility and customization, allowing you to tailor memory components to your specific agent needs.
*   **Persistence Layer:**  Example shows integration with Neo4j graph database for persistent memory storage.
*   **Docker Support:**  Includes a `docker-compose.yaml` file for easy deployment and environment setup.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python:** Version 3.7 or higher is recommended.
*   **Docker:**  For containerization and simplified setup.
*   **Docker Compose:** For managing multi-container Docker applications.
*   **Neo4j (optional):** If you wish to use the Neo4j graph database integration.
*   **API Keys:** Google Gemini API Key.

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Uhimanshu9/Memory_Rag.git
    cd Memory_Rag
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**

    *   Set the `GEMINI_API_KEY` environment variable with your Google Gemini API key.
    *   If using Neo4j, configure `NEO4J_URL`, `NEO4J_USERNAME`, and `NEO4J_PASSWORD` as required for your Neo4j instance.  Example Neo4j setup:
        ```bash
        export NEO4J_URL="bolt://localhost:7687"
        export NEO4J_USERNAME="neo4j"
        export NEO4J_PASSWORD="your_neo4j_password"
        ```
    *   Set the `QUADRANT_HOST` environment variable.
        ```bash
        export QUADRANT_HOST="localhost"
        ```

5.  **Start the application using Docker (optional):**

    ```bash
    docker-compose up --build
    ```

    This will build the Docker image and start the application in a containerized environment.  Ensure Docker is installed and running before executing this command.

## Usage Examples & API Documentation

The `script.py` file provides a basic example of how to use the `Memory` class with Gemini for embedding and Neo4j for memory storage.

```python
from mem0 import Memory
import google.generativeai as genai

# Set these in your environment!
# GEMINI_API_KEY = ""
# QUADRANT_HOST = "localhost"
# NEO4J_URL="bolt://localhost:7687"
# NEO4J_USERNAME="neo4j"
# NEO4J_PASSWORD="reform-william-center-vibrate-press-5829"

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
QUADRANT_HOST = os.environ.get("QUADRANT_HOST")
NEO4J_URL = os.environ.get("NEO4J_URL")
NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD")

# Init Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Init mem0 memory
mem_client = Memory.from_config({
    "version": "v1.1",
    "embedder": {
        "provider": "gimini",  # Still using OpenAI embedding (you get the idea!)
    },
    "db": {
        "provider": "neo4j",
        "url": NEO4J_URL,
        "username": NEO4J_USERNAME,
        "password": NEO4J_PASSWORD,
    },
    "quadrant":{
        "host": QUADRANT_HOST
    }
})

# Example usage:
# mem_client.add(text="Example memory text.")
# retrieved_memory = mem_client.retrieve(query="What is an example memory?")
# print(retrieved_memory)
```

**Explanation:**

1.  **Import necessary libraries:** Imports `Memory` from `mem0` and `google.generativeai`.
2.  **Configure Gemini:** Configures the Gemini API with your API key.
3.  **Initialize Memory:** Initializes the `Memory` class with configuration options specifying the embedding provider (Gemini), the database provider (Neo4j), and Quadrant Host.
4.  **Add memory:**  The `add()` method stores information in the memory.
5.  **Retrieve memory:** The `retrieve()` method retrieves relevant information based on a query.

**Note:** Replace the placeholder values for `GEMINI_API_KEY`, `NEO4J_URL`, `NEO4J_USERNAME`, and `NEO4J_PASSWORD` with your actual credentials.  `mem0` module is not included but the example provides an example of how memory should be added.  You must implement the memory functionality.

## Configuration Options

The `Memory` class can be configured through a dictionary passed to the `from_config` method.  The following options are available:

*   **`version`:**  Specifies the version of the memory system.
*   **`embedder`:** Configuration options for the embedding provider.
    *   `provider`:  The embedding provider to use (e.g., "gimini").
*   **`db`:** Configuration options for the database provider.
    *   `provider`:  The database provider to use (e.g., "neo4j").
    *   `url`:  The URL of the database server.
    *   `username`: The username for accessing the database.
    *   `password`: The password for accessing the database.
*   **`quadrant`**: Configuration options for Quadrant.
    *   `host`: The host name or IP address of the Quadrant server.

These options can also be set as environment variables for a more flexible and secure configuration.


## Acknowledgments

*   Google for the Gemini API.
*   Neo4j for the graph database.
*   Any other contributors who help improve this project.
