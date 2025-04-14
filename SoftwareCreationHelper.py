import customtkinter as ctk

class ModCreatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self.root, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.sidebar_label = ctk.CTkLabel(self.sidebar, text="Menu", font=ctk.CTkFont(size=20, weight="bold"))
        self.sidebar_label.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="ew")

        self.main_frame_container = ctk.CTkFrame(self.root)
        self.main_frame_container.grid(row=0, column=1, sticky="nsew")

        self.frames = {}
        self.create_frames()

        # Buttons with commands to swap frames
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
            button.grid(row=i, column=0, padx=10, pady=10, sticky="ew")

        self.sidebar.grid_rowconfigure(len(self.buttons), weight=1)

        self.show_frame("Software Type")  # Default

    def create_frames(self):
        self.frames["Software Type"] = self.create_input_frame({"Software Name": "Software Name", "Description": "Description"})
        self.frames["Spec Features"] = self.create_input_frame({"Feature Name": "Feature Name", "Details": "Details"})
        self.frames["Sub Features"] = self.create_input_frame({"Sub-feature": "Sub-feature", "Related Feature": "Related Feature"})
        self.frames["Categories"] = self.create_input_frame({"Category Name": "Category Name", "Description": "Description"})
        self.frames["Add-ons"] = self.create_input_frame({"Add-on Name": "Add-on Name", "Compatibility": "Compatibility"})
        self.frames["Hardware"] = self.create_input_frame({"Hardware Name": "Hardware Name", "Specs": "Specs"})
        self.frames["Name Generators"] = self.create_input_frame({"Generator Name": "Generator Name", "Seed Words": "Seed Words"})
        self.frames["Company Types"] = self.create_input_frame({"Company Type": "Company Type", "Traits": "Traits"})
        self.frames["Personalities"] = self.create_input_frame({"Personality": "Personality", "Behavior": "Behavior"})
        self.frames["Export"] = self.create_export_frame()

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def create_input_frame(self, fields):
        frame = ctk.CTkFrame(self.main_frame_container)

        for i, field in enumerate(fields.items()):
            label_text, entry_placeholder = field
            ctk.CTkLabel(frame, text=f"{label_text}:").grid(row=i, column=0, padx=10, pady=10, sticky="e")
            ctk.CTkEntry(frame, placeholder_text=entry_placeholder).grid(row=i, column=1, padx=10, pady=10, sticky="w")

        return frame

    def create_export_frame(self):
        frame = ctk.CTkFrame(self.main_frame_container)

        ctk.CTkLabel(frame, text="Export Mod", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)
        ctk.CTkButton(frame, text="Export to File", command=self.export_mod).pack(pady=10)

        return frame

    def export_mod(self):
        print("Exporting mod...")  # You could tie this into file saving later

    def show_frame(self, name):
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()

# Usage
if __name__ == "__main__":
    root = ctk.CTk()
    app = ModCreatorApp(root)
    root.mainloop()
