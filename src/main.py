# main.py
#
# Copyright 2021 Mirko Brombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, Gdk, Gio, Handy

from .window import AmusizWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='pm.mirko.Amusiz',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        '''Load custom CSS'''
        data_bytes = Gio.resources_lookup_data(
            "/pm/mirko/Amusiz/style.css", 0)
        provider = Gtk.CssProvider()
        provider.load_from_data(data_bytes.get_data())
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),
                                                 provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        win = self.props.active_window
        if not win:
            win = AmusizWindow(application=self)
        win.present()


def main(version):
    app = Application()
    return app.run(sys.argv)
