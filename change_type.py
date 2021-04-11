import bpy
from bpy.types import Operator 

class REDHALO_OT_changeType(Operator):
    bl_idname = "redhalo_tools.change_type"
    bl_label = "Change Type"
    bl_description = "Change Type from active"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context): 
        ab = bpy.context.object

        ob = bpy.context.selected_objects

        oriSelected = ob[:]

        #Copy objects
        if ab is not None:
            for i in range(len(ob)):
                new_obj = ab.copy()
                new_obj.location = ob[i].location
                try:
                    bpy.context.collection.objects.link(new_obj)
                except:
                    pass

        #Delete Origin objects
        for o in oriSelected:
            bpy.context.collection.objects.unlink(o)
            bpy.data.objects.remove(o)


        return {'FINISHED'}