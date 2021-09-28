import mounter
import controller
import console_view


if __name__ == "__main__":
    model = mounter.Mounter()
    cv = console_view.ConsoleView()
    app = controller.Controller(model, cv)

    app.run()
