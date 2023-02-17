import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK App")

        # Create a vertical box layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Create a button for each command to execute
        button1 = Gtk.Button.new_with_label("ls")
        button2 = Gtk.Button.new_with_label("ps aux")
        button3 = Gtk.Button.new_with_label("whoami")

        # Create a text view to display the command output
        self.textview = Gtk.TextView()
        vbox.pack_start(self.textview, True, True, 0)

        # Connect button clicks to commands
        button1.connect("clicked", self.run_command, "ls")
        button2.connect("clicked", self.run_command, "ps aux")
        button3.connect("clicked", self.run_command, "whoami")

        # Add buttons to the layout
        vbox.pack_start(button1, True, True, 0)
        vbox.pack_start(button2, True, True, 0)
        vbox.pack_start(button3, True, True, 0)

    def run_command(self, widget, command):
        # Run the command as a subprocess and capture its output
        result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Display the output in the text view
        output = result.stdout.decode() + result.stderr.decode()
        buffer = self.textview.get_buffer()
        buffer.set_text(output)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
