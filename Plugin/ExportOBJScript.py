bl_info = {
    "name": "OBJ Exporter",
    "author": "ArrowNTheKnee",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Exports Selection as OBJ format",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
import os
from bpy.types import (Panel, Operator)
from bpy.utils import register_class, unregister_class

class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "export.1"
    bl_label = "Simple Export Operator"

    def execute(self, context):
        
        blend_file_path =  bpy.data.filepath
        blend_file_name = bpy.path.basename(bpy.context.blend_data.filepath).replace('.blend', '.obj')
        directory = os.path.dirname(blend_file_path)
        target_file = os.path.join(directory, blend_file_name)

        bpy.ops.export_scene.obj(filepath=target_file, use_selection=True)

        
        return {'FINISHED'}

class CustomPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Exporter"
    bl_idname = "OBJECT_PT_export"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Exporter"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Export .OBJ", icon='EXPORT')


_classes = {
    ButtonOperator,
    CustomPanel

}


def register():
    for cls in _classes:
        register_class(cls)


def unregister():
    for cls in _classes:
        unregister_class(cls)


if __name__ == "__main__":
    register()
