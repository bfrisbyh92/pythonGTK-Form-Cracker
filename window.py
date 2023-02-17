import gi
import subprocess
from gi.repository import Gtk
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="File Selector and Input Demo")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # File Selector 1
        file_selector1_label = Gtk.Label(label="Password List:")
        vbox.pack_start(file_selector1_label, False, False, 0)

        file_selector1 = Gtk.FileChooserButton(title="Select a file")
        vbox.pack_start(file_selector1, False, False, 0)

        # File Selector 2
        file_selector2_label = Gtk.Label(label="User List:")
        vbox.pack_start(file_selector2_label, False, False, 0)

        file_selector2 = Gtk.FileChooserButton(title="Select a file")
        vbox.pack_start(file_selector2, False, False, 0)

        # Input 1
        input1_label = Gtk.Label(label="Target's IP:")
        vbox.pack_start(input1_label, False, False, 0)

        input1_entry = Gtk.Entry()
        vbox.pack_start(input1_entry, False, False, 0)

        # Input 2
        input2_label = Gtk.Label(label="Path:")
        vbox.pack_start(input2_label, False, False, 0)

        input2_entry = Gtk.Entry()
        vbox.pack_start(input2_entry, False, False, 0)

        # Input 3
        input3_label = Gtk.Label(label="Failure String for Regex:")
        vbox.pack_start(input3_label, False, False, 0)

        input3_entry = Gtk.Entry()
        vbox.pack_start(input3_entry, False, False, 0)

        # Submit Button
        submit_button = Gtk.Button(label="Submit")
        submit_button.connect("clicked", self.on_submit_clicked, file_selector1, file_selector2, input1_entry, input2_entry, input3_entry)

        vbox.pack_start(submit_button, False, False, 0)

        # Display area for showing the selected inputs
        self.display_label = Gtk.Label(label="")
        vbox.pack_start(self.display_label, False, False, 0)

    def on_submit_clicked(self, button, file_selector1, file_selector2, input1_entry, input2_entry, input3_entry):
        selected_files = [file_selector1.get_filename(), file_selector2.get_filename()]
        input1 = input1_entry.get_text()
        input2 = input2_entry.get_text()
        input3 = input3_entry.get_text()

        selected_inputs = f"Selected files: {selected_files}\nInput 1: {input1}\nInput 2: {input2}\nInput 3: {input3}"

        self.display_label.set_text(selected_inputs)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

# from gi.repository import Gtk
# import gi
# import subprocess

# gi.require_version('Gtk', '3.0')


# class MyWindow(Gtk.Window):
#     def __init__(self):
#         Gtk.Window.__init__(self, title="GTK App")

#         vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

#         # Create a horizontal box container for the buttons
#         hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
#         vbox.pack_start(hbox, False, False, 0)

#         # Create the buttons
#         button1 = Gtk.Button.new_with_label("ls")
#         button2 = Gtk.Button.new_with_label("ps")
#         button3 = Gtk.Button.new_with_label("pwd")

#         # Add the buttons to the horizontal box container
#         hbox.pack_start(button1, True, True, 0)
#         hbox.pack_start(button2, True, True, 0)
#         hbox.pack_start(button3, True, True, 0)

#         # Create a textview for displaying the output
#         self.textview = Gtk.TextView()
#         vbox.pack_start(self.textview, True, True, 0)

#         # Connect the button signals to their handlers
#         button1.connect("clicked", self.on_button1_clicked)
#         button2.connect("clicked", self.on_button2_clicked)
#         button3.connect("clicked", self.on_button3_clicked)

#         # Add the vertical box container to the window
#         self.add(vbox)

#     def on_button1_clicked(self, button):
#         command = ["ls"]
#         output = subprocess.check_output(command).decode()
#         self.update_textview(output)

#     def on_button2_clicked(self, button):
#         command = ["ps"]
#         output = subprocess.check_output(command).decode()
#         self.update_textview(output)

#     def on_button3_clicked(self, button):
#         command = ["pwd"]
#         output = subprocess.check_output(command).decode()
#         self.update_textview(output)

#     def update_textview(self, text):
#         buffer = self.textview.get_buffer()
#         buffer.set_text(text)


# win = MyWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()

# from gi.repository import Gtk

# class MyWindow(Gtk.Window):
#     def __init__(self):
#         Gtk.Window.__init__(self, title="GTK App")

#         # Create a vertical box container for the widgets
#         vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

#         # Create the first file selector widget
#         self.file_selector_1 = Gtk.FileChooserButton(title="Choose File 1")
#         vbox.pack_start(self.file_selector_1, False, False, 0)

#         # Create the second file selector widget
#         self.file_selector_2 = Gtk.FileChooserButton(title="Choose File 2")
#         vbox.pack_start(self.file_selector_2, False, False, 0)

#         # Create the three input areas
#         self.input1 = Gtk.Entry()
#         vbox.pack_start(self.input1, False, False, 0)

#         self.input2 = Gtk.Entry()
#         vbox.pack_start(self.input2, False, False, 0)

#         self.input3 = Gtk.Entry()
#         vbox.pack_start(self.input3, False, False, 0)

#         # Create a button for submitting the inputs
#         submit_button = Gtk.Button(label="Submit")
#         submit_button.connect("clicked", self.on_submit_clicked)
#         vbox.pack_start(submit_button, False, False, 0)

#         # Add the vertical box container to the window
#         self.add(vbox)

#     def on_submit_clicked(self, button):
#         # Get the selected file paths and input values
#         file_path_1 = self.file_selector_1.get_filename()
#         file_path_2 = self.file_selector_2.get_filename()
#         input_value_1 = self.input1.get_text()
#         input_value_2 = self.input2.get_text()
#         input_value_3 = self.input3.get_text()

#         # Display the inputs in the console
#         print("File 1:", file_path_1)
#         print("File 2:", file_path_2)
#         print("Input 1:", input_value_1)
#         print("Input 2:", input_value_2)
#         print("Input 3:", input_value_3)


# win = MyWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()
