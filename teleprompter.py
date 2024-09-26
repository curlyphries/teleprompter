import tkinter as tk

class Teleprompter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Teleprompter")

        # Initialize variables
        self.scroll_speed = 2  # Initial scroll speed in seconds
        self.font_size = 20    # Initial font size
        self.is_scrolling = False
        self.text_lines = []
        self.current_line_index = 0

        # Create two frames
        self.input_frame = tk.Frame(self.root)
        self.output_frame = tk.Frame(self.root, bg='black')

        # Pack the frames side by side
        self.input_frame.pack(side="left", fill="y")
        self.output_frame.pack(side="right", fill="both", expand=True)

        # Input frame widgets
        self.prompt_label = tk.Label(self.input_frame, text="Enter your prompt:")
        self.prompt_label.pack(fill="x")

        self.text_entry = tk.Text(self.input_frame, height=20, width=40)
        self.text_entry.pack(fill="y")

        self.load_button = tk.Button(self.input_frame, text="Load Text", command=self.load_text)
        self.load_button.pack(fill="x")

        # Output frame widgets
        self.speed_slider = tk.Scale(
            self.input_frame,
            from_=1,
            to=10,
            orient="horizontal",
            label="Speed (seconds)",
            command=self.update_speed
        )
        self.speed_slider.set(self.scroll_speed)
        self.speed_slider.pack(fill="x")

        self.size_slider = tk.Scale(
            self.input_frame,
            from_=10,
            to=100,
            orient="horizontal",
            label="Font Size",
            command=self.update_font_size
        )
        self.size_slider.set(self.font_size)
        self.size_slider.pack(fill="x")

        self.start_button = tk.Button(self.input_frame, text="Start", command=self.start_scrolling)
        self.start_button.pack(fill="x")

        self.stop_button = tk.Button(self.input_frame, text="Stop", command=self.stop_scrolling)
        self.stop_button.pack(fill="x")

        self.prompt_label_output = tk.Label(
            self.output_frame,
            text="",
            fg='white',
            bg='black',
            font=("Arial", self.font_size),
            wraplength=self.output_frame.winfo_screenwidth()
        )
        self.prompt_label_output.pack(fill="both", expand=True)

        # Bind space bar to pause/resume scrolling
        self.root.bind('<space>', self.toggle_scrolling)

    def load_text(self):
        # Get text and split into lines
        full_text = self.text_entry.get('1.0', tk.END).strip()
        self.text_lines = full_text.split('\n')
        self.current_line_index = 0
        self.prompt_label_output.config(text="")
        self.is_scrolling = False

    def update_speed(self, val):
        self.scroll_speed = int(val)

    def update_font_size(self, val):
        self.font_size = int(val)
        self.prompt_label_output.config(font=("Arial", self.font_size))

    def start_scrolling(self):
        if not self.is_scrolling and self.text_lines:
            self.is_scrolling = True
            self.scroll_text()

    def stop_scrolling(self):
        self.is_scrolling = False

    def toggle_scrolling(self, event):
        if self.is_scrolling:
            self.stop_scrolling()
        else:
            self.start_scrolling()

    def scroll_text(self):
        if self.is_scrolling and self.current_line_index < len(self.text_lines):
            # Update the text label with the current line
            self.prompt_label_output.config(text=self.text_lines[self.current_line_index])
            self.current_line_index += 1
            # Schedule the next line
            self.root.after(int(self.scroll_speed * 1000), self.scroll_text)
        else:
            self.is_scrolling = False

    def run(self):
        self.root.mainloop()

teleprompter = Teleprompter()
teleprompter.run()
