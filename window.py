import gi
import subprocess
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Python-Hydra Password Cracker")
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

        # Input 4
        input4_label = Gtk.Label(label="Protocol:")
        vbox.pack_start(input4_label, False, False, 0)

        input4_entry = Gtk.Entry()
        vbox.pack_start(input4_entry, False, False, 0)

        # Submit Button
        submit_button = Gtk.Button(label="Submit")
        submit_button.connect("clicked", self.on_submit_clicked, file_selector1,
                              file_selector2, input1_entry, input2_entry, input3_entry, input4_entry)

        vbox.pack_start(submit_button, False, False, 0)

        # Display area for showing the selected inputs
        self.display_label = Gtk.Label(label="")
        vbox.pack_start(self.display_label, False, False, 0)

    def on_submit_clicked(self, button, file_selector1, file_selector2, input1_entry, input2_entry, input3_entry, input4_entry):
        selected_files = [
            file_selector1.get_filename(), file_selector2.get_filename()]
        targetip = input1_entry.get_text()
        path = input2_entry.get_text()
        regexstring = input3_entry.get_text()
        protocol = input4_entry.get_text()

        selected_inputs = f"Selected files: {selected_files}\nTarget IP: {targetip}\nPath: {path}\nRegexString: {regexstring}\nProtocol: {protocol}"

        self.display_label.set_text(selected_inputs)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
