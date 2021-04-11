import bpy

def filterSelect(type):
    types = ["mesh", "curve", "surf", "meta", "font", "hair", "pointcloud", "volume", "grease_pencil", "armature", "lattice", "empty", "light", "light_probe", "camera", "speaker"]

    if type == "all":
        for attr in types:
            exec("bpy.context.space_data.show_object_select_" + attr + " = True")
    else:
        for attr in types:
            re = "False"
            
            attr_s = "bpy.context.space_data.show_object_select_" + attr + " = "
            if type == attr:
                re = "True"
            exec(attr_s + re)

class REDHALO_OT_Filter_Operator(bpy.types.Operator):
    bl_idname = "redhalo_tools.filter_op"
    bl_label = "Filter Objects"

    def get_items(self, context):
        
        types = ["all", "mesh", "curve", "surf", "meta", "font", "hair", "pointcloud", "volume", "grease_pencil", "armature", "lattice", "empty", "light", "light_probe", "camera", "speaker"]

        return [(ob, "", "") for ob in types]

    action : bpy.props.EnumProperty(
        items = get_items
    )

    def execute(self, context):
        types = ["all", "mesh", "curve", "surf", "meta", "font", "hair", "pointcloud", "volume", "grease_pencil", "armature", "lattice", "empty", "light", "light_probe", "camera", "speaker"]

        f = bpy.context.scene.filter_option
        
        for i in types:
            if self.action == i:
                filterSelect(i)
                bpy.context.scene.filter_option = i

        return {"FINISHED"}

class REDHALO_MT_menu_filterselect(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
    bl_label = "Filter"
    bl_ui_units_x = 6

    bpy.types.Scene.filter_option = bpy.props.StringProperty(name="Filter Option", default = "all")

    def draw(self, context):
        layout = self.layout
        layout.operator("redhalo_tools.filter_op", text="All", icon="ALIGN_JUSTIFY").action = "all"
        layout.separator()
        layout.operator("redhalo_tools.filter_op", text="Mesh", icon="MESH_CUBE").action = "mesh"
        layout.operator("redhalo_tools.filter_op", text="Light", icon="LIGHT").action = "light"
        layout.operator("redhalo_tools.filter_op", text="Camera", icon="CAMERA_DATA").action = "camera"
        layout.operator("redhalo_tools.filter_op", text="Empty", icon="EMPTY_DATA").action = "empty"
        layout.operator("redhalo_tools.filter_op", text="Curve", icon="CURVE_DATA").action = "curve"
        layout.operator("redhalo_tools.filter_op", text="Font", icon="FONT_DATA").action = "font"
        layout.separator()
        layout.operator("redhalo_tools.filter_op", text="Surface", icon="SURFACE_DATA").action = "surf"
        layout.operator("redhalo_tools.filter_op", text="Hair", icon="HAIR_DATA").action = "hair"
        layout.operator("redhalo_tools.filter_op", text="Point Cloud", icon="POINTCLOUD_DATA").action = "pointcloud"
        layout.operator("redhalo_tools.filter_op", text="Meta", icon="META_DATA").action = "meta"
        layout.operator("redhalo_tools.filter_op", text="Volume", icon="SNAP_VOLUME").action = "volume"
        layout.operator("redhalo_tools.filter_op", text="Grease Pencil", icon="GREASEPENCIL").action = "grease_pencil"
        layout.operator("redhalo_tools.filter_op", text="Armature", icon="ARMATURE_DATA").action = "armature"
        layout.operator("redhalo_tools.filter_op", text="Lattice", icon="LATTICE_DATA").action = "lattice"
        layout.operator("redhalo_tools.filter_op", text="Light Probe", icon="LIGHTPROBE_GRID").action = "light_probe"
        layout.operator("redhalo_tools.filter_op", text="Speaker", icon="SPEAKER").action = "speaker"

def REDHALO_MT_Filter_Menu(self, context):
    op_text = "F : " + bpy.context.scene.filter_option.capitalize()
    self.layout.popover("REDHALO_MT_menu_filterselect", text = op_text, icon = "PLUS")
