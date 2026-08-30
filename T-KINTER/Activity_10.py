# Import tkinter for GUI
import tkinter as tk
from tkinter import ttk, messagebox

# Import os for handling file paths
import os

# Import Pillow for working with JPG images
from PIL import Image, ImageTk


# Define the RestaurantOrderManagement class
class RestaurantOrderManagement:

    # Initialize the application
    def __init__(self, root):

        # Store the main window
        self.root = root

        # Set the title of the window
        self.root.title("Restaurant Management App")

        # Set the size of the window
        self.root.geometry("800x600")

        # Prevent the window from being resized
        self.root.resizable(False, False)

        # Dictionary containing menu items and prices in USD
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        # Exchange rate from USD to INR
        self.exchange_rate = 82

        # Set up the background
        self.setup_background(root)

        # Create a frame to hold all the widgets
        frame = ttk.Frame(root)

        # Place the frame in the center of the window
        frame.place(
            relx=0.5,
            rely=0.5,
            anchor=tk.CENTER
        )

        # Heading
        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )

        # Dictionary to store menu labels
        self.menu_labels = {}

        # Dictionary to store quantity entry boxes
        self.menu_quantities = {}

        # Create menu items
        for i, (item, price) in enumerate(
            self.menu_items.items(),
            start=1
        ):

            # Create label for menu item
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )

            # Put label into column 0
            label.grid(
                row=i,
                column=0,
                padx=10,
                pady=5
            )

            # Save label reference
            self.menu_labels[item] = label

            # Create quantity entry box
            quantity_entry = ttk.Entry(
                frame,
                width=5
            )

            # Put entry box into column 1
            quantity_entry.grid(
                row=i,
                column=1,
                padx=10,
                pady=5
            )

            # Save entry reference
            self.menu_quantities[item] = quantity_entry

        # Create a StringVar for currency
        self.currency_var = tk.StringVar()

        # Currency label
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5
        )

        # Currency dropdown
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )

        # Put dropdown in column 1
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )

        # Select USD by default
        currency_dropdown.current(0)

        # Run update_menu_prices when currency changes
        self.currency_var.trace_add(
            "write",
            self.update_menu_prices
        )

        # Create Place Order button
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )

        # Put button in the window
        order_button.grid(
            row=len(self.menu_items) + 2,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )

  

    def setup_background(self, root):

        # Background size
        bg_width = 800
        bg_height = 600

        # Create canvas
        canvas = tk.Canvas(
            root,
            width=bg_width,
            height=bg_height,
            highlightthickness=0
        )

        # Put canvas in the window
        canvas.pack()

        # Find the folder where this Python file is located
        current_folder = os.path.dirname(
            os.path.abspath(__file__)
        )

        # Create complete path to the image
        image_path = os.path.join(
            current_folder,
            "Restaurant_Order_Management.jpg"
        )

        # Check whether image exists
        if not os.path.exists(image_path):

            messagebox.showerror(
                "Image Error",
                "Background image not found!\n\n"
                + image_path
            )

            return

        # Open the JPG image using Pillow
        image = Image.open(image_path)

        # Resize image to 800 x 600
        image = image.resize(
            (bg_width, bg_height),
            Image.Resampling.LANCZOS
        )

        # Convert Pillow image into Tkinter image
        background_image = ImageTk.PhotoImage(image)

        # Put image on canvas
        canvas.create_image(
            0,
            0,
            anchor=tk.NW,
            image=background_image
        )

        # Keep a reference to the image
        canvas.image = background_image



    def update_menu_prices(self, *args):

        # Get selected currency
        currency = self.currency_var.get()

        # Select currency symbol
        if currency == "INR":
            symbol = "₹"
            rate = self.exchange_rate
        else:
            symbol = "$"
            rate = 1

        # Update every menu item
        for item, label in self.menu_labels.items():

            # Calculate converted price
            price = self.menu_items[item] * rate

            # Display the new price
            label.config(
                text=f"{item} ({symbol}{price}):"
            )

    # ---------------------------------------------------------
    # PLACE ORDER
    # ---------------------------------------------------------

    def place_order(self):

        # Start total cost at zero
        total_cost = 0

        # Create order summary
        order_summary = "Order Summary:\n\n"

        # Get selected currency
        currency = self.currency_var.get()

        # Select symbol and exchange rate
        if currency == "INR":
            symbol = "₹"
            rate = self.exchange_rate
        else:
            symbol = "$"
            rate = 1

        # Go through every menu item
        for item, entry in self.menu_quantities.items():

            # Get quantity entered by the user
            quantity = entry.get().strip()

            # Check if the quantity is a number
            if quantity.isdigit():

                # Convert quantity to integer
                quantity = int(quantity)

                # Calculate item price
                price = self.menu_items[item] * rate

                # Calculate total cost for this item
                cost = quantity * price

                # Add to total cost
                total_cost += cost

                # Add item to summary if quantity > 0
                if quantity > 0:

                    order_summary += (
                        f"{item}: "
                        f"{quantity} x "
                        f"{symbol}{price:g} = "
                        f"{symbol}{cost:g}\n"
                    )

        # Check if at least one item was ordered
        if total_cost > 0:

            # Add total cost
            order_summary += (
                f"\nTotal Cost: "
                f"{symbol}{total_cost:g}"
            )

            # Show successful order
            messagebox.showinfo(
                "Order Placed",
                order_summary
            )

        else:

            # Show error
            messagebox.showerror(
                "Error",
                "Please order at least one item."
            )



if __name__ == "__main__":

    # Create the main Tkinter window
    root = tk.Tk()

    # Create the application
    app = RestaurantOrderManagement(root)

    # Start the Tkinter event loop
    root.mainloop()