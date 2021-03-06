# ***************************************************************************
#
#    copyright            : (C) 2013 by Valery Ovchinnikov (LADUGA Ltd.)
#                                       Anton Lapshin
#                                       Anton Kargin
#    email                : laduga@laduga.com
#***************************************************************************
#***************************************************************************
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License as published by  *
#*   the Free Software Foundation; either version 2 of the License, or     *
#*   (at your option) any later version.                                   *
#*                                                                         *
#***************************************************************************/


ERROR_STATUS = -1
DEFAULT_STATUS = 0
SUCCESS_STATUS = 1

status_to_string = dict()
status_to_string[ERROR_STATUS] = "Error"
status_to_string[DEFAULT_STATUS] = "Default"
status_to_string[SUCCESS_STATUS] = "Success"

DEFAULT_LOADCASE = "grid_loadcase"
LOADCASES_DIR = 'loadcases'
