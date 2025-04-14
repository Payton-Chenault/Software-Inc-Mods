import customtkinter as ctk


class SoftwareIncModCreator:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Software Inc. Software Creator")
        self.root.geometry("1200x800")
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self.root, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.buttons = {
            "Software Type": ctk.CTkButton(self.sidebar, text="Software Type", command=lambda: print("Software Type")),
            "Spec Features": ctk.CTkButton(self.sidebar, text="Spec Features", command=lambda: print("Spec Features")),
            "Sub Features": ctk.CTkButton(self.sidebar, text="Sub Features", command=lambda: print("Sub Features")),
            "Categories": ctk.CTkButton(self.sidebar, text="Categories", command=lambda: print("Categories")),
            "Add-ons": ctk.CTkButton(self.sidebar, text="Add-ons", command=lambda: print("Add-ons")),
            "Hardware": ctk.CTkButton(self.sidebar, text="Hardware", command=lambda: print("Hardware")),
            "Name Generators": ctk.CTkButton(self.sidebar, text="Name Generators", command=lambda: print("Name Generators")),
            "Company Types": ctk.CTkButton(self.sidebar, text="Company Types", command=lambda: print("Company Types")),
            "Personalities": ctk.CTkButton(self.sidebar, text="Personalities", command=lambda: print("Personalities")),
            "Export": ctk.CTkButton(self.sidebar, text="Export Mod", command=lambda: print("Export Mod"))
        }
        self.sidebar.grid_rowconfigure(len(self.buttons), weight=1)  # Add spacing at the bottom

        self.sidebar_label = ctk.CTkLabel(self.sidebar, text="Menu", font=ctk.CTkFont(size=20, weight="bold"))
        self.sidebar_label.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="ew")

        for i, (_, button) in enumerate(self.buttons.items(), start=1):
            button.grid(row=i, column=0, padx=10, pady=10, sticky="ew")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.main_label = ctk.CTkLabel(self.main_frame, text="Welcome to Software Inc. Mod Creator",
                                       font=ctk.CTkFont(size=24, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")
       
        
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")
    
    root = ctk.CTk()
    app = SoftwareIncModCreator(root)
    root.mainloop()