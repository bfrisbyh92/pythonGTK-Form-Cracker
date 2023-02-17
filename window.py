from gi.repository import Gtk
import gi
import subprocess

gi.require_version('Gtk', '3.0')


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK App")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Create a horizontal box container for the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, False, False, 0)

        # Create the buttons
        button1 = Gtk.Button.new_with_label("ls")
        button2 = Gtk.Button.new_with_label("ps")
        button3 = Gtk.Button.new_with_label("pwd")

        # Add the buttons to the horizontal box container
        hbox.pack_start(button1, True, True, 0)
        hbox.pack_start(button2, True, True, 0)
        hbox.pack_start(button3, True, True, 0)

        # Create a textview for displaying the output
        self.textview = Gtk.TextView()
        vbox.pack_start(self.textview, True, True, 0)

        # Connect the button signals to their handlers
        button1.connect("clicked", self.on_button1_clicked)
        button2.connect("clicked", self.on_button2_clicked)
        button3.connect("clicked", self.on_button3_clicked)

        # Add the vertical box container to the window
        self.add(vbox)

    def on_button1_clicked(self, button):
        command = ["ls"]
        output = subprocess.check_output(command).decode()
        self.update_textview(output)

    def on_button2_clicked(self, button):
        command = ["ps", "aux"]
        output = subprocess.check_output(command).decode()
        self.update_textview(output)

    def on_button3_clicked(self, button):
        command = ["pwd"]
        output = subprocess.check_output(command).decode()
        self.update_textview(output)

    def update_textview(self, text):
        buffer = self.textview.get_buffer()
        buffer.set_text(text)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
