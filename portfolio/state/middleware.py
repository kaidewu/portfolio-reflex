import reflex as rx

class LoggingMiddleware(rx.Middleware):
    def preprocess(self, app, state, event):
        print(f"Event {event}")

    def postprocess(self, app, state, event, update):
        print(f"Update {update}")