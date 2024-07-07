import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import os

class AnimationGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Animation Frame Generator")

        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.main_frame, text="Number of frames:").grid(row=0, column=0, sticky=tk.W)
        self.num_frames_entry = ttk.Entry(self.main_frame)
        self.num_frames_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.main_frame, text="Select Images:").grid(row=1, column=0, sticky=tk.W)
        self.images_listbox = tk.Listbox(self.main_frame, selectmode=tk.MULTIPLE, height=5)
        self.images_listbox.grid(row=1, column=1, sticky=(tk.W, tk.E))
        self.load_images_button = ttk.Button(self.main_frame, text="Load Images", command=self.load_images)
        self.load_images_button.grid(row=2, column=1, sticky=(tk.W, tk.E))

        self.generate_button = ttk.Button(self.main_frame, text="Generate Code", command=self.generate_code)
        self.generate_button.grid(row=3, column=0, columnspan=2)

        self.code_text = scrolledtext.ScrolledText(self.main_frame, width=80, height=20)
        self.code_text.grid(row=4, column=0, columnspan=2)

        self.image_paths = []

    def load_images(self):
        filepaths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),("All Files", "*.*")])
        for filepath in filepaths:
            self.image_paths.append(filepath)
            self.images_listbox.insert(tk.END, os.path.basename(filepath))

    def generate_code(self):
        try:
            num_frames = int(self.num_frames_entry.get())
        except ValueError:
            self.code_text.insert(tk.END, "Please enter a valid number of frames.\n")
            return

        if not self.image_paths:
            self.code_text.insert(tk.END, "Please load at least one image.\n")
            return

        image_loads = "\n".join([f'images.append(pygame.image.load("{path}"))' for path in self.image_paths])
        code = f"""
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images
images = []
{image_loads}

# Animation settings
num_frames = {num_frames}
frame_duration = 100  # milliseconds per frame
clock = pygame.time.Clock()

def main():
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        screen.blit(images[frame % len(images)], (100, 100))
        pygame.display.flip()
        
        frame += 1
        clock.tick(1000 // frame_duration)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
"""
        self.code_text.delete(1.0, tk.END)
        self.code_text.insert(tk.END, code)

if __name__ == "__main__":
    app = AnimationGenerator()
    app.mainloop()
