# C4D Installer
# Copyright (C) 2016  Niklas Rosenstein
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

from PyQt5.QtWidgets import QApplication, QMessageBox

import sys


def fatal(message):
  if QMessageBox:
    try:
      app = QApplication(sys.argv)
      QMessageBox.critical(None, 'Error', str(message))
    except BaseException as exc:
      print('fatal:', message)
      print('during handling of the above error, following error occured')
      print('fatal:', exc)
  else:
    print('fatal:', message)
  sys.exit(1)
