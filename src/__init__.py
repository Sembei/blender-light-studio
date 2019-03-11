'''
Copyright (C) 2015 Marcin Zielinski
martin.zielinsky at gmail.com

Created by Marcin Zielinski

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Blender Light Studio",
    "description": "Easy setup for complex studio lighting",
    "author": "LeoMoon Studios, Marcin Zielinski, special thanks to Maciek Ptaszynski for initial scene",
    "version": (2, 3, 11),
    "blender": (2, 80, 0),
    "location": "View3D -> Tools -> Light Studio",
    "wiki_url": "",
    "category": "User Interface" }
    
    
import bpy      
import tempfile
# load and reload submodules
##################################    
    
from . import developer_utils
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())



# register
################################## 
import traceback
from . import gui
from . import light_operators
from . import light_profiles
from . import light_preview_list
from . import light_brush
from . import selectOperator
from . import deleteOperator


##Prefs.select_mouse
def config_load():
    # from extensions_framework import util as efutil
    # bpy.bls_selection_override_right = efutil.find_config_value(bl_info['name'], 'defaults', 'selection_override_right', True)
    # bpy.bls_selection_override_left = efutil.find_config_value(bl_info['name'], 'defaults', 'selection_override_left', False)

    light_operators.update_selection_override()
    
#

def register():
    # 
    gui.register()
    light_operators.register()
    light_profiles.register()
    light_preview_list.register()
    light_brush.register()
    selectOperator.register()
    deleteOperator.register()
    
    #bpy.types.Scene.BLStudio = bpy.props.PointerProperty(name="Blender Light Studio Properties", type=Blender_Light_Studio_Properties)
    bpy.types.Object.protected = bpy.props.BoolProperty(name = 'protected', default = False)
    
    deleteOperator.add_shortkeys()
    config_load() # select operator shortkeys
    
    
    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))
    

def unregister():
    selectOperator.remove_shortkeys()
    deleteOperator.remove_shortkeys()
    
    #
    gui.unregister()
    light_profiles.unregister()
    light_operators.unregister()
    light_preview_list.unregister()
    light_brush.unregister()
    selectOperator.unregister()
    deleteOperator.unregister()
    
    print("Unregistered {}".format(bl_info["name"]))
    
#EOF
