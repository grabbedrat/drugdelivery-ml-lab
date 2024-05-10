from flask import current_app

# Import the module structures from their respective __init__.py files
from modules.module1.routes import module1_structure
from modules.module2.routes import module2_structure
from modules.module3.routes import module3_structure
from modules.module4.routes import module4_structure
from modules.module5.routes import module5_structure
from modules.module6.routes import module6_structure
from modules.module7.routes import module7_structure


def register_context_processors(app):
    @app.context_processor
    def inject_modules():
        """
        Context processor to make the module structures available to all templates.
        """
        module_structures = [
            module1_structure,
            module2_structure,
            module3_structure,
            module4_structure,
            module5_structure,
            module6_structure,
            module7_structure


        ]
        return dict(modules=module_structures)