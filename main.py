from agents.image_agent import ImageAgent
from agents.approval_agent import ApprovalAgent

# MCP server endpoint (replace with actual URL)
MCP_URL = "https://your-mcp-server.com/generate"

def run_image_task(prompt, count):
    image_agent = ImageAgent(MCP_URL)
    approval_agent = ApprovalAgent()

    if count == 1:
        print("✅ Auto-approved single image request.")
        result = image_agent.generate_image(prompt)
        print("🖼️ Image generated:", result)
    else:
        if approval_agent.request_approval(prompt, count):
            print("✅ Approval granted. Generating images...")
            results = image_agent.generate_bulk_images(prompt, count)
            for i, res in enumerate(results, 1):
                print(f"🖼️ Image {i}:", res)
        else:
            print("❌ Approval denied. Task cancelled.")

if __name__ == "__main__":
    prompt = input("Enter image prompt: ")
    count = int(input("How many images to generate? "))
    run_image_task(prompt, count)