from mem0 import Memory
import google.generativeai as genai


# OPENAI_API_KEY = ""
GEMINI_API_KEY="AIzaSyCL6e9YJHhuvHNzTwbKIc5G-5BKLn1wgXA"
QUADRANT_HOST = "localhost"

NEO4J_URL="bolt://localhost:7687"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="reform-william-center-vibrate-press-5829"

# Init Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Init mem0 memory
mem_client = Memory.from_config({
    "version": "v1.1",
    "embedder": {
        "provider": "gimini",  # Still using OpenAI embedding (you can change this)
        "config": {"api_key": GEMINI_API_KEY, "model": "text-embedding-3-small"},
    },
    "llm": {
        "provider": "gemini",  # (optional) label
        "config": {"api_key": GEMINI_API_KEY, "model": "gemini-2.5-flash"},
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": 6333},
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "bolt://localhost:7687",
            "username": "neo4j",
            "password": NEO4J_PASSWORD,
        },
    },
})

# Memory-aware system prompt
base_system_prompt = """
You are a Memory-Aware Knowledge Agent.
You analyze input, recall and build on past context using retrieved memories.
Use professional tone, flag uncertainties, and reason step by step.
"""

chat_history = []
user_id = "p123"

# Start interactive loop
while True:
    user_input = input(">> ")

    # Retrieve relevant memory
    mem_result = mem_client.search(query=user_input, user_id=user_id)
    retrieved_memories = "\n".join([m["memory"] for m in mem_result.get("results", [])])

    # Build full prompt
    full_prompt = f"""{base_system_prompt}

MEMORY:
{retrieved_memories}

USER: {user_input}
"""

    # Send to Gemini (Pro model)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(full_prompt)

    bot_reply = response.text
    print("BOT:", bot_reply)

    # Store the interaction to memory
    mem_client.add([
        { "role": "user", "content": user_input },
        { "role": "assistant", "content": bot_reply }
    ], user_id=user_id)

    # Save to history (if you want full multi-turn)
    chat_history.extend([
        { "role": "user", "content": user_input },
        { "role": "assistant", "content": bot_reply }
    ])
