import tkinter as tk
from tkinter import ttk
import requests

class DiscordWebhookDeleter:
    def __init__(self, master):
        self.master = master
        master.title("Discord Webhook Deleter")

        # set background color
        bg_color = "#F5F5F5"
        master.configure(bg=bg_color)
        bg_label = tk.Label(master, bg=bg_color)
        bg_label.place(relwidth=1, relheight=1)

        # create input field for webhook URL
        self.webhook_label = ttk.Label(master, text="Webhook URL:", font=("Helvetica", 14))
        self.webhook_label.place(relx=0.5, rely=0.3, anchor="center")
        self.webhook_entry = ttk.Entry(master, width=50, font=("Helvetica", 14))
        self.webhook_entry.place(relx=0.5, rely=0.4, anchor="center")

        # create button to delete webhook
        self.delete_button = ttk.Button(master, text="Delete Webhook", command=self.delete_webhook, style="my.TButton")
        self.delete_button.place(relx=0.5, rely=0.5, anchor="center")

    def delete_webhook(self):
        # get webhook URL from input field
        webhook_url = self.webhook_entry.get()

        # send DELETE request to Discord API
        response = requests.delete(webhook_url)

        # check response status code and display appropriate message
        if response.status_code == 204:
            message = "Webhook deleted successfully."
        else:
            message = f"Failed to delete webhook. Status code: {response.status_code}"

        # create label to display message and pack it
        self.result_label = ttk.Label(self.master, text=message, font=("Helvetica", 14))
        self.result_label.place(relx=0.5, rely=0.7, anchor="center")

# create GUI window
root = tk.Tk()

# set window size and position
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# set window background color and style
root.configure(bg="#F5F5F5")
style = ttk.Style()
style.theme_use("clam")
style.configure("my.TButton", font=("Helvetica", 14), foreground="#FFFFFF", background="#3F51B5")
style.map("my.TButton", foreground=[('active', '#FFFFFF'), ('!disabled', '#FFFFFF')], background=[('active', '#303F9F'), ('!disabled', '#3F51B5')])

# create instance of DiscordWebhookDeleter
app = DiscordWebhookDeleter(root)

# run main loop
root.mainloop()
