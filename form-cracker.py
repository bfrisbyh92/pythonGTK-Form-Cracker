import gi
import subprocess
from gi.repository import Gtk

# By Brendan Frisby
# https://brendanfrisby.live


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Multi-Protocol Password Cracker")
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

        # Display area for showing the selected inputs
        self.display_label = Gtk.Label(label="Inputs Selected")
        vbox.pack_start(self.display_label, False, False, 0)

 # Scrolled Window to display command output
        self.output_scroll = Gtk.ScrolledWindow()
        self.output_scroll.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        vbox.pack_start(self.output_scroll, True, True, 0)

    def on_submit_clicked(self, button, file_selector1, file_selector2, input1_entry, input2_entry, input3_entry, input4_entry):
        selected_files = [
            file_selector1.get_filename(), file_selector2.get_filename()]
        targetip = input1_entry.get_text()
        path = input2_entry.get_text()
        regexstring = input3_entry.get_text()
        protocol = input4_entry.get_text()

        # selected_inputs = f"Selected files: {selected_files}\nTarget IP: {targetip}\nPath: {path}\nRegexString: {regexstring}\nProtocol: {protocol}"

        command = f"hydra -L {selected_files[1]} -P {selected_files[0]} -e nsr -v -F {protocol}://{targetip}/{path}:F={regexstring}"
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)

        # Run the command and capture the output
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)

        # Display the command output in the console
        print(result.stdout)
        print(result.stderr)

        # Create a new window to display the output
        output_window = Gtk.Window(title="Hydra Output")
        output_window.set_default_size(500, 300)

        # Create a scrolled window to hold the output text
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

        # Create a text view to display the output
        output_view = Gtk.TextView()
        output_view.set_editable(False)
        output_view.set_cursor_visible(False)
        output_view.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)

        # Create a buffer to hold the output text
        buffer = output_view.get_buffer()

        # Insert the output text into the buffer
        buffer.insert_at_cursor(result.stdout)

        # Add the text view to the scrolled window
        scrolled_window.add(output_view)

        # Add the scrolled window to the output window
        output_window.add(scrolled_window)

        # Show the output window
        output_window.show_all()

 # Display the command output in the console
        print(result.stdout)
        print(result.stderr)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
