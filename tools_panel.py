import bpy
from bpy.types import Operator

class VIEW3D_PT_RedHaloTools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'    
    bl_label = "RED HALO Tools"

    def draw(self, context):    
        layout = self.layout

        split = layout.split()
        col = split.column()
        # col = layout.column(align=True)
        # col.operator('redhalo_tools.load_material', icon='IMPORT',text = "LOAD Material")
        col.operator('redhalo_tools.set_color_id', icon='COLLAPSEMENU',text = "Color ID")
        
        col = split.column()
        col.operator('redhalo_tools.change_type', icon='UV_SYNC_SELECT',text = "Change Type")
        col.operator('redhalo_tools.clear_normal', icon='PANEL_CLOSE',text = "Clear Split Normal Data")
        
