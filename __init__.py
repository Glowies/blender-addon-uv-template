_needs_reload = "bpy" in locals()

import bpy
# from . import (
#     # module1,
# )

if _needs_reload:
    # import importlib
    # module3 = importlib.reload(module3)
    print("Add-on Reloaded")


class ObjectMoveX(bpy.types.Operator):
    """My Object Moving Script"""  # Use this as a tooltip for menu items and buttons.

    bl_idname = (
        "object.move_x"  # Unique identifier for buttons and menu items to reference.
    )
    bl_label = "Move X by One"  # Display name in the interface.
    bl_options = {"REGISTER", "UNDO"}  # Enable undo for the operator.

    def execute(self, context):  # execute() is called when running the operator.
        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        self.report({"INFO"}, "Running Move X by One")

        return {"FINISHED"}  # Lets Blender know the operator finished successfully.


def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)


def register():
    bpy.utils.register_class(ObjectMoveX)
    bpy.types.VIEW3D_MT_object.append(
        menu_func
    )  # Adds the new operator to an existing menu.


def unregister():
    bpy.utils.unregister_class(ObjectMoveX)
