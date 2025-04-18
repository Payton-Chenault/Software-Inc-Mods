import customtkinter as ctk


class ModCreatorApp:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.geometry("1000x800")
        self.root.title("Software Inc. Mod Creator")
        self.root.resizable(False, False)
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")

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
        self.sub_feature_dropdowns = []
        self.create_frames()

        # Sidebar buttons
        self.buttons = {
            "Software Type": ctk.CTkButton(self.sidebar, text="Software Type", command=lambda: self.show_frame("Software Type")),
            "Spec Features": ctk.CTkButton(self.sidebar, text="Spec Features", command=lambda: self.show_frame("Spec Features")),
            "Sub Features": ctk.CTkButton(self.sidebar, text="Sub Features", command=lambda: self.show_frame("Sub Features")),
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
            "Submarket Name One": "",
            "Submarket Name Two": "",
            "Submarket Name Three": ""
        })
        self.frames["Spec Features"] = self.create_spec_features_frame()
        self.frames["Sub Features"] = self.create_sub_features_frame()
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

    def create_spec_features_frame(self):
        self.spec_features_frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)

        title_label = ctk.CTkLabel(self.spec_features_frame, text="Spec Features", font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=(20, 10))

        scroll_frame = ctk.CTkScrollableFrame(self.spec_features_frame, orientation="horizontal", width=900, height=300)
        scroll_frame.pack(padx=10, pady=5, fill="both", expand=True)
        self.spec_feature_scroll_frame = scroll_frame

        self.spec_feature_rows = []
        self.add_spec_feature_row()

        add_button = ctk.CTkButton(self.spec_features_frame, text="+", width=30, command=self.add_spec_feature_row)
        add_button.pack(pady=15, anchor="w", padx=20)

        return self.spec_features_frame

    def add_spec_feature_row(self):
        row_index = len(self.spec_feature_rows)
        entries = []
        labels = [
            "Name", "Spec", "Description", "Dependencies", "Unlock",
            "DevTime", "Submarkets", "CodeArt", "Server", "Optional", "SoftwareCategories"
        ]
        for col, label in enumerate(labels):
            entry = ctk.CTkEntry(self.spec_feature_scroll_frame, placeholder_text=label, width=150)
            entry.grid(row=row_index, column=col, padx=5, pady=5)
            entries.append(entry)
        self.spec_feature_rows.append(entries)
        self.refresh_sub_feature_dropdowns()

    def create_sub_features_frame(self):
        self.sub_features_frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)

        title_label = ctk.CTkLabel(self.sub_features_frame, text="Sub Features", font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=(20, 10))

        scroll_frame = ctk.CTkScrollableFrame(self.sub_features_frame, orientation="horizontal", width=900, height=300)
        scroll_frame.pack(padx=10, pady=5, fill="both", expand=True)
        self.sub_feature_scroll_frame = scroll_frame

        self.sub_feature_rows = []
        self.add_sub_feature_row()

        add_button = ctk.CTkButton(self.sub_features_frame, text="+", width=30, command=self.add_sub_feature_row)
        add_button.pack(pady=15, anchor="w", padx=20)

        return self.sub_features_frame

    def add_sub_feature_row(self):
        row_index = len(self.sub_feature_rows)
        entries = []
        labels = [
            "Name", "Description", "Level", "Unlock", "DevTime",
            "Submarkets", "CodeArt", "Server", "SoftwareCategories"
        ]
        for col, label in enumerate(labels):
            entry = ctk.CTkEntry(self.sub_feature_scroll_frame, placeholder_text=label, width=150)
            entry.grid(row=row_index, column=col, padx=5, pady=5)
            entries.append(entry)

        # Dropdown for Spec Feature reference
        options = [entry[0].get() for entry in self.spec_feature_rows if entry and entry[0].get()]
        dropdown = ctk.CTkOptionMenu(self.sub_feature_scroll_frame, values=options or ["None"])
        dropdown.grid(row=row_index, column=len(labels), padx=5, pady=5)
        self.sub_feature_dropdowns.append(dropdown)
        entries.append(dropdown)

        self.sub_feature_rows.append(entries)

    def refresh_sub_feature_dropdowns(self):
        options = [entry[0].get() for entry in self.spec_feature_rows if entry and entry[0].get()]
        if not options:
            options = ["None"]
        for dropdown in self.sub_feature_dropdowns:
            dropdown.configure(values=options)
            dropdown.set(options[0])

    def create_export_frame(self):
        frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)

        ctk.CTkLabel(frame, text="Export Mod", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=30)
        ctk.CTkButton(frame, text="Export to File", command=self.export_mod).pack(pady=10)

        return frame

    def export_mod(self):
        data = ""

        # Software Type Section
        software_type = self.get_software_type_data()

        # Spec Features Section
        spec_features = self.get_spec_features_data()

        # Construct the final export string
        data += f"SoftwareType\n{{\n"
        data += f'    Name "{software_type["software_name"]}"\n'
        data += f'    Description "{software_type["description"]}"\n'
        data += f'    Random {software_type["random_sales_weight"]}\n'
        data += f'    IdealPrice {software_type["ideal_price"]}\n'
        data += f'    OptimalDevTime {software_type["optimal_dev_time"]}\n'
        data += f'    OSSupport {software_type["os_supports"]}\n'
        data += f'    OneClient {software_type["contract_software"]}\n'
        data += f'    InHouse {software_type["in_house_software"]}\n'
        data += f'    SubmarketNames [{software_type["submarket_name_1"]}; {software_type["submarket_name_2"]}; {software_type["submarket_name_3"]}]\n'

        # Add Features (Spec Features and Sub Features)
        data += f'    Features\n    [\n'
        for spec_feature in spec_features:
            data += f'        {{\n'
            data += f'            Name "{spec_feature["name"]}"\n'
            data += f'            Spec {spec_feature["spec"]}\n'
            data += f'            Description "{spec_feature["description"]}"\n'
            data += f'            DevTime {spec_feature["dev_time"]}\n'
            data += f'            CodeArt {spec_feature["code_art"]}\n'
            data += f'            Submarkets {spec_feature["submarkets"]}\n'

            # Add Sub Features
            data += f'            Features\n            [\n'
            for sub_feature in spec_feature["sub_features"]:
                data += f'                {{\n'
                data += f'                    Name "{sub_feature["name"]}"\n'
                data += f'                    Description "{sub_feature["description"]}"\n'
                data += f'                    DevTime {sub_feature["dev_time"]}\n'
                data += f'                    Level {sub_feature["level"]}\n'
                data += f'                    CodeArt {sub_feature["code_art"]}\n'
                data += f'                    Submarkets {sub_feature["submarkets"]}\n'
                data += f'                }}\n'
            data += f'            ]\n'
            data += f'        }}\n'
        data += f'    ]\n'
        data += f'}}\n'

        # Save to file
        with open("mod_config.txt", "w") as file:
            file.write(data)

        print("Exported mod configuration to 'mod_config.txt'.")

    def get_software_type_data(self):
        # Retrieve software type data
        return {
            "software_name": self.get_value("Software Name"),
            "description": self.get_value("Description"),
            "random_sales_weight": self.get_value("Random Sales Weight"),
            "ideal_price": self.get_value("Ideal Price"),
            "optimal_dev_time": self.get_value("Optimal Dev Time"),
            "os_supports": self.get_value("OS Supports"),
            "contract_software": self.get_value("Contract Software"),
            "in_house_software": self.get_value("In House Software"),
            "submarket_name_1": self.get_value("Submarket Name One"),
            "submarket_name_2": self.get_value("Submarket Name Two"),
            "submarket_name_3": self.get_value("Submarket Name Three"),
        }

    def get_spec_features_data(self):
        spec_features = []
        for row in self.spec_feature_rows:
            spec_feature = {
                "name": row[0].get(),
                "spec": row[1].get(),
                "description": row[2].get(),
                "dev_time": row[5].get(),
                "code_art": row[7].get(),
                "submarkets": row[6].get(),
                "sub_features": self.get_sub_features_data(row[0].get())
            }
            spec_features.append(spec_feature)
        return spec_features

    def get_sub_features_data(self, spec_feature_name):
        sub_features = []
        for row in self.sub_feature_rows:
            if row[9].get() == spec_feature_name:
                sub_feature = {
                    "name": row[0].get(),
                    "description": row[1].get(),
                    "dev_time": row[4].get(),
                    "level": row[2].get(),
                    "code_art": row[6].get(),
                    "submarkets": row[5].get(),
                }
                sub_features.append(sub_feature)
        return sub_features

    def get_value(self, field_name):
        return "Example Placeholder"


if __name__ == "__main__":
    root = ctk.CTk()
    app = ModCreatorApp(root)
    root.mainloop()
