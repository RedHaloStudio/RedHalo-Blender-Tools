import bpy
from bpy.types import Operator

class VIEW3D_PT_RedHaloTools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'    
    bl_label = "RED HALO Tools"

    def draw(self, context):    
        layout = self.layout
        row = layout.column(align=True)
        row.scale_y = 1.25
        row.operator('redhalo.set_color_id', icon='COLLAPSEMENU',text = "设置为彩色ID通道")
        row.operator('redhalo.change_type', icon='UV_SYNC_SELECT',text = "Change Type")