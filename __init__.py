bl_info = {  
    "name": "Red Halo Tools",  
    "author": "Red Halo Studio",  
    "version": (0, 1, 1),  
    "blender": (2, 80, 0),  
    "location": "View 3D > Tools > Red Halo Tools",  
    "description": "",  
    "wiki_url": "",  
    "tracker_url": "",  
    "category": "Tools"
 }

import bpy
from .tools_panel import VIEW3D_PT_RedHaloTools
# from .import_mtl import REDHALO_OT_loadMaterials
from .set_color_id import REDHALO_OT_setColorID
from .change_type import REDHALO_OT_changeType
from .clear_normal import REDHALO_OT_cleanNormal
from .filterSelect import REDHALO_MT_menu_filterselect, REDHALO_OT_Filter_Operator, REDHALO_MT_Filter_Menu
 
classes = (
    # REDHALO_OT_loadMaterials, #Load Material Operator
    REDHALO_OT_setColorID, # Set Color ID Operator
    VIEW3D_PT_RedHaloTools, # UI
    REDHALO_OT_changeType, # Change Type Operator
    REDHALO_OT_cleanNormal, # Clean Split Normal Operator
    
    #Filter Menu
    REDHALO_MT_menu_filterselect,
    REDHALO_OT_Filter_Operator,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_HT_header.append(REDHALO_MT_Filter_Menu)
    # bpy.types.VIEW3D_MT_editor_menus.append(REDHALO_MT_Filter_Menu)

def unregister():
    bpy.types.VIEW3D_HT_header.remove(REDHALO_MT_Filter_Menu)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
     register()