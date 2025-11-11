class ApprovalAgent:
    def __init__(self):
        self.approved = False

    def request_approval(self, prompt, count):
        print(f"⚠️ Bulk request detected: {count} images for prompt '{prompt}'")
        decision = input("Do you approve this request? (yes/no): ").strip().lower()
        self.approved = decision == "yes"
        return self.approved