from flask import current_app

# Import the module structures from their respective __init__.py files
from modules.module1.routes import module1_structure
#from modules.module2 import module2_structure
# ... (import structures for other modules)

def register_context_processors(app):
    @app.context_processor
    def inject_modules():
        """
        Context processor to make the module structures available to all templates.
        """
        module_structures = [
            module1_structure,
            #module2_structure,
            # ... (add other module structures)
        ]
        return dict(modules=module_structures)