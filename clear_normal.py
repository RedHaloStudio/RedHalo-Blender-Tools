import bpy
from bpy.types import Operator 

class REDHALO_OT_cleanNormal(Operator):
    bl_idname = "redhalo_tools.clear_normal"
    bl_label = "Clear Normal"
    bl_description = "Clear Split Normal Data"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context): 
        selection = bpy.context.selected_objects

        for o in selection:
            bpy.context.view_layer.objects.active = o
            try:
                bpy.ops.mesh.customdata_custom_splitnormals_clear()
            except:
                print(o.name)

        return {'FINISHED'}