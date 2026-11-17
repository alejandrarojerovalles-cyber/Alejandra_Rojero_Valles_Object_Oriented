from models.producto_model import ProductoModel
from views.producto_view import ProductoView
from controllers.producto_controller import ProductoController

if __name__ == "__main__":
    app_view = ProductoView()
    app_model = ProductoModel()
    app_controller = ProductoController(app_model, app_view)
    app_view.mainloop()