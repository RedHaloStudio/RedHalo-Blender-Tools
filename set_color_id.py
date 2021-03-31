import bpy
import random
from bpy.types import Operator 

def randomRGB():
    r = random.randint(0,255)/255.0
    g = random.randint(0,255)/255.0
    b = random.randint(0,255)/255.0
    return r,g,b,1

def renderClrID(node,num,clr):

    nodes = node.node_tree.nodes
    links = node.node_tree.links

    # 1st node
    for i in nodes.keys():
        t = type(nodes[i])
        if t == bpy.types.ShaderNodeOutputMaterial:
            key = i

    parentNode = nodes[key]
    nPos = parentNode.location
    
    # MixShader Nodes
    node_mixshader = nodes.new(type = "ShaderNodeMixShader")
    node_mixshader.inputs[0].default_value = 1
    node_mixshader.location = (parentNode.location.x - 200),(parentNode.location.y)

    # Transparent Node
    node_transparent = nodes.new(type = "ShaderNodeBsdfTransparent")
    node_transparent.location = (node_mixshader.location.x-200),(node_mixshader.location.y-150)

    #node-emission shader
    node_emission = nodes.new(type="ShaderNodeEmission")
    node_emission.location = (node_mixshader.location.x-200),(node_mixshader.location.y)

    #node light path
    node_lightPath = nodes.new(type="ShaderNodeLightPath")
    node_lightPath.location = (node_emission.location.x - 200),(node_emission.location.y - 200)

    #HueSaturation Node
    node_HueSaturation = nodes.new(type="ShaderNodeHueSaturation")
    node_HueSaturation.inputs[1].default_value = 0.99
    node_HueSaturation.inputs[2].default_value = 0.99
    node_HueSaturation.inputs[4].default_value = clr
    
    node_HueSaturation.location = (node_emission.location.x - 200),(node_emission.location.y)
    
    links.new(node_mixshader.outputs[0],parentNode.inputs[0])
    links.new(node_emission.outputs[0],node_mixshader.inputs[2])
    links.new(node_transparent.outputs[0],node_mixshader.inputs[1])
    links.new(node_HueSaturation.outputs[0],node_emission.inputs[0])
    links.new(node_lightPath.outputs[0],node_emission.inputs[1])

    for i in links:
        if i.to_socket.name == "Alpha":
            # keepLinks = i.from_node
            links.new(i.from_node.outputs[0],node_mixshader.inputs[0])  

class Tools_OT_setColorID(Operator):
    bl_idname = "redhalo.set_color_id"
    bl_label = "Set Color ID for Render"
    bl_description = "Set Color ID for Render"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context): 

        #Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        
        # Delete all lights
        allLights = [l for l in bpy.context.scene.objects if l.type == "LIGHT"]
        for i in allLights:
            i.select_set(True)
        
        bpy.ops.object.delete()

        #Set oject property
        for o in bpy.context.scene.objects:
            obj_vis = o.cycles_visibility

            obj_vis.diffuse = False
            obj_vis.glossy = False
            obj_vis.transmission = False
            obj_vis.scatter = False
            obj_vis.shadow = False

        #all materials in scene
        AllMats = bpy.data.materials[:]

        if len(AllMats) > 0:
            
            ind = 1
            for i in AllMats:
                clr = randomRGB()
                
                try:
                    renderClrID(i, len(AllMats), clr)
                except:
                    # print("ERROR")
                    self.report({"ERROR"}, "Convert Error")
                i.pass_index = ind
                ind += 1
                
        else:
            self.report({'WARNING'}, "No material in scene")

        # Set Cycles
        bpy.context.scene.cycles.samples = 8
        bpy.context.scene.cycles.max_bounces = 1
        bpy.context.scene.cycles.film_exposure = 1

        return {'FINISHED'}