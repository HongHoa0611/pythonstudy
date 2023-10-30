import tkinter as tk
from PIL import Image, ImageTk

# Create a window
window = tk.Tk()
window.title("Image Display")

# Load and open the image using Pillow
image = Image.open("C:\\Users\\mrblackcat\\Desktop\\pythonclass\\pythonstudy\\buoi 24\\Image\\cart.png")  # Replace 'your_image.jpg' with the path to your image

# Convert the image to a format that Tkinter can use
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(window, image=photo)
label.pack()

# Start the Tkinter main loop
window.mainloop()
