import tkinter as tk
from tkinter import ttk, scrolledtext
import random

# Function to generate Pygame code
def generate_code():
    try:
        num_shapes = int(num_shapes_entry.get())
        r_variation = int(r_variation_entry.get())
        g_variation = int(g_variation_entry.get())
        b_variation = int(b_variation_entry.get())
    except ValueError:
        code_text.insert(tk.END, "Please enter valid numbers.\n")
        return
    
    code = f"""
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
base_color = (100, 150, 200)

def random_color():
    r = max(0, min(255, base_color[0] + random.randint(-{r_variation}, {r_variation})))
    g = max(0, min(255, base_color[1] + random.randint(-{g_variation}, {g_variation})))
    b = max(0, min(255, base_color[2] + random.randint(-{b_variation}, {b_variation})))
    return (r, g, b)

def draw_shapes():
    screen.fill((255, 255, 255))
    for _ in range({num_shapes}):
        color = random_color()
        if random.choice(['circle', 'square']) == 'circle':
            pygame.draw.circle(screen, color, (random.randint(0, screen_width), random.randint(0, screen_height)), 20)
        else:
            rect = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 40, 40)
            pygame.draw.rect(screen, color, rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_shapes()
    pygame.display.flip()

pygame.quit()
"""
    code_text.delete(1.0, tk.END)
    code_text.insert(tk.END, code)

# GUI setup
root = tk.Tk()
root.title("Shape Terrain Generator")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(main_frame, text="Number of shapes:").grid(row=0, column=0, sticky=tk.W)
num_shapes_entry = ttk.Entry(main_frame)
num_shapes_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(main_frame, text="R variation:").grid(row=1, column=0, sticky=tk.W)
r_variation_entry = ttk.Entry(main_frame)
r_variation_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(main_frame, text="G variation:").grid(row=2, column=0, sticky=tk.W)
g_variation_entry = ttk.Entry(main_frame)
g_variation_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(main_frame, text="B variation:").grid(row=3, column=0, sticky=tk.W)
b_variation_entry = ttk.Entry(main_frame)
b_variation_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

generate_button = ttk.Button(main_frame, text="Generate Code", command=generate_code)
generate_button.grid(row=4, column=0, columnspan=2)

code_text = scrolledtext.ScrolledText(main_frame, width=80, height=20)
code_text.grid(row=5, column=0, columnspan=2)

root.mainloop()
