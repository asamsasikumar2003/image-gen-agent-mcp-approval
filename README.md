# image-gen-agent-mcp-approval
Autonomous image generation agent using MCP servers with built-in approval logic for bulk requests. Automatically generates single images and pauses for cost approval when handling multi-image tasks.
# 🖼️ Image Generation Agent with Cost Approval (MCP + ADK)

This project demonstrates an autonomous image generation agent that interacts with an MCP (Model Control Protocol) server to generate images. It includes a built-in approval mechanism to control costs when handling bulk image requests.

---

## 🚀 Features

- ✅ **Single Image Requests**: Automatically approved and generated instantly.
- 🛑 **Bulk Image Requests (>1)**: Pauses execution and requests user approval before proceeding.
- 🔌 **MCP Server Integration**: Easily configurable to work with public or private image generation MCP endpoints.
- 🧠 **Agent Architecture**: Built using ADK and Gemini for modular, intelligent task handling.

---

## 🧩 Agent Logic

| Scenario                  | Behavior                                      |
|---------------------------|-----------------------------------------------|
| Request for 1 image       | Auto-approve and generate immediately         |
| Request for >1 images     | Pause and request approval before generating  |
| Approval granted          | Proceed with image generation                 |
| Approval denied/timeout   | Cancel the task                               |

---

## 🛠️ Tech Stack

- **Python**
- **ADK (Autonomous Agents Development Kit)**
- **Gemini** (for reasoning and task routing)
- **MCP Server** (for image generation)
