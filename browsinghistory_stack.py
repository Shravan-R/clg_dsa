class Browser:

    def __init__(self, homepage):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = homepage
        print(f"Starting on homepage: {self.current_page}")

    def visit(self, url):
        print(f"\nVisiting: {url}")
        self.back_stack.append(self.current_page)
        self.current_page = url

        if self.forward_stack:
            print(" (Clearing forward history)")
            self.forward_stack.clear()

        print(f"Current page: {self.current_page}")

    def back(self):
        if not self.back_stack:
            print("\nBack: No pages in history.")
            return

        print(f"\nGoing back from {self.current_page}")
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Current page: {self.current_page}")

    def forward(self):
        if not self.forward_stack:
            print("\nForward: No forward pages.")
            return

        print(f"\nGoing forward from {self.current_page}")
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Current page: {self.current_page}")

    def debug(self):
        return {
            "back_stack": list(self.back_stack),
            "current_page": self.current_page,
            "forward_stack": list(self.forward_stack)
        }
if __name__ == "__main__":
    br = Browser("google.com")
    br.visit("youtube.com")
    br.visit("twitter.com")
    br.back()
    br.back()
    br.forward()
    print("\nDebug:", br.debug())
