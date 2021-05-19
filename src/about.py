# about.py
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

from gi.repository import Gtk

@Gtk.Template(resource_path='/pm/mirko/Amusiz/about.ui')
class AmusizAboutDialog(Gtk.AboutDialog):
    __gtype_name__ = 'AmusizAboutDialog'

    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)
        self.set_transient_for(window)
