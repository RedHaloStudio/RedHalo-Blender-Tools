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

    for i in nodes.keys():
        t = type(nodes[i])
        if t == bpy.types.ShaderNodeOutputMaterial:
            key = i

    parentNode = nodes[key]
    nPos = parentNode.location
    
    #node-emission shader
    node_emission = nodes.new(type="ShaderNodeEmission")
    node_emission.location = (nPos.x-200),(nPos.y)

    #node light path
    node_lightPath = nodes.new(type="ShaderNodeLightPath")
    node_lightPath.location = (nPos.x-400),(nPos.y-50)

    #HueSaturation Node
    node_HueSaturation = nodes.new(type="ShaderNodeHueSaturation")
    node_HueSaturation.inputs[1].default_value = 0.99
    node_HueSaturation.inputs[2].default_value = 0.99
    node_HueSaturation.inputs[4].default_value = clr
    
    node_HueSaturation.location = (nPos.x-400),(nPos.y+150)
    
    links.new(node_emission.outputs[0],parentNode.inputs[0])
    
    links.new(node_HueSaturation.outputs[0],node_emission.inputs[0])
    links.new(node_lightPath.outputs[0],node_emission.inputs[1])    

class Tools_OT_setColorID(Operator):
    bl_idname = "redhalo.set_color_id"
    bl_label = "Set Color ID for Render"
    bl_description = "Set Color ID for Render"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context): 
                #all materials in scene
        AllMats = bpy.data.materials[:]

        if len(AllMats) > 0:
            
            ind = 1
            for i in AllMats:
                clr = randomRGB()
                #print(clr)
                try:
                    renderClrID(i, len(AllMats), clr)
                except:
                    print("ERROR")
                i.pass_index = ind
                ind += 1
                
        else:
            print("====Scene no materials===")

        # Set Cycles
        bpy.context.scene.cycles.samples = 16
        bpy.context.scene.cycles.max_bounces = 1
        bpy.context.scene.cycles.film_exposure = 1

        # Turn off all lights
        for li in bpy.data.lights:
            li.energy = 0

        return {'FINISHED'}