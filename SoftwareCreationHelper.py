import customtkinter as ctk


class ModCreatorApp:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.geometry("1000x800")
        self.root.title("Software Inc. Mod Creator")
        self.root.resizable(False, False)
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("vibrant_theme.json")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self.root, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(99, weight=1)  # push buttons up

        self.sidebar_label = ctk.CTkLabel(self.sidebar, text="🧩 Mod Sections", font=ctk.CTkFont(size=22, weight="bold"))
        self.sidebar_label.grid(row=0, column=0, padx=20, pady=(25, 10), sticky="ew")

        self.main_frame_container = ctk.CTkFrame(self.root, corner_radius=15)
        self.main_frame_container.grid(row=0, column=1, sticky="nsew")
        self.main_frame_container.grid_rowconfigure(0, weight=1)
        self.main_frame_container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.create_frames()

        # Sidebar buttons
        self.buttons = {
            "Software Type": ctk.CTkButton(self.sidebar, text="Software Type", command=lambda: self.show_frame("Software Type")),
            "Spec Features": ctk.CTkButton(self.sidebar, text="Spec Features", command=lambda: self.show_frame("Spec Features")),
            "Sub Features": ctk.CTkButton(self.sidebar, text="Sub Features", command=lambda: self.show_frame("Sub Features")),
            "Categories": ctk.CTkButton(self.sidebar, text="Categories", command=lambda: self.show_frame("Categories")),
            "Add-ons": ctk.CTkButton(self.sidebar, text="Add-ons", command=lambda: self.show_frame("Add-ons")),
            "Hardware": ctk.CTkButton(self.sidebar, text="Hardware", command=lambda: self.show_frame("Hardware")),
            "Name Generators": ctk.CTkButton(self.sidebar, text="Name Generators", command=lambda: self.show_frame("Name Generators")),
            "Company Types": ctk.CTkButton(self.sidebar, text="Company Types", command=lambda: self.show_frame("Company Types")),
            "Personalities": ctk.CTkButton(self.sidebar, text="Personalities", command=lambda: self.show_frame("Personalities")),
            "Export": ctk.CTkButton(self.sidebar, text="Export Mod", command=lambda: self.show_frame("Export")),
        }

        for i, (_, button) in enumerate(self.buttons.items(), start=1):
            button.grid(row=i, column=0, padx=20, pady=5, sticky="ew")

        self.show_frame("Software Type")  # Show default

    def create_frames(self):
        self.frames["Software Type"] = self.create_input_frame("Software Type", {
            "Software Name": "Software Name",
            "Description": "Description",
            "Unlock Year": "Year",
            "Random": "Sales Weight (0-1)",
            "Ideal Price": "Price",
            "Optimal Dev Time": "Months",
            "Popularity": "Max Customer Multiplier (0-1)",
            "Retention": "Months",
            "Iterative": "(0-1)",
            "OS Supports": "True, False, or specific os eg Computer",
            "Contract Software": "True False",
            "In House Software": "True False",
            "Name Generator": "File Name",
            "Submarket Name One": "",
            "Submarket Name Two": "",
            "Submarket Name Three": ""
        })
        self.frames["Spec Features"] = self.create_input_frame("Spec Features", {
            "Feature Name": "Feature Name",
            "Details": "Details"
        })
        self.frames["Sub Features"] = self.create_input_frame("Sub Features", {
            "Sub-feature": "Sub-feature",
            "Related Feature": "Related Feature"
        })
        self.frames["Categories"] = self.create_input_frame("Categories", {
            "Category Name": "Category Name",
            "Description": "Description"
        })
        self.frames["Add-ons"] = self.create_input_frame("Add-ons", {
            "Add-on Name": "Add-on Name",
            "Compatibility": "Compatibility"
        })
        self.frames["Hardware"] = self.create_input_frame("Hardware", {
            "Hardware Name": "Hardware Name",
            "Specs": "Specs"
        })
        self.frames["Name Generators"] = self.create_input_frame("Name Generators", {
            "Generator Name": "Generator Name",
            "Seed Words": "Seed Words"
        })
        self.frames["Company Types"] = self.create_input_frame("Company Types", {
            "Company Type": "Company Type",
            "Traits": "Traits"
        })
        self.frames["Personalities"] = self.create_input_frame("Personalities", {
            "Personality": "Personality",
            "Behavior": "Behavior"
        })
        self.frames["Export"] = self.create_export_frame()

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def create_input_frame(self, title, fields):
        frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)

        title_label = ctk.CTkLabel(frame, text=title, font=ctk.CTkFont(size=20, weight="bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        for i, (label_text, entry_placeholder) in enumerate(fields.items(), start=1):
            ctk.CTkLabel(frame, text=label_text + ":", anchor="e", font=ctk.CTkFont(size=14)).grid(
                row=i, column=0, padx=20, pady=8, sticky="e")
            ctk.CTkEntry(frame, placeholder_text=entry_placeholder).grid(
                row=i, column=1, padx=20, pady=8, sticky="ew")

        frame.grid_columnconfigure(1, weight=1)
        return frame

    def create_export_frame(self):
        frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)

        ctk.CTkLabel(frame, text="Export Mod", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=30)
        ctk.CTkButton(frame, text="Export to File", command=self.export_mod).pack(pady=10)

        return frame

    def export_mod(self):
        print("Exporting mod...")  # Placeholder

    def show_frame(self, name):
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()


# Usage
if __name__ == "__main__":
    root = ctk.CTk()
    app = ModCreatorApp(root)
    root.mainloop()
