import threading

def execute_target (target, args: list = None, kwargs: dict = None):
    if args == None: args = ()
    if kwargs == None: kwargs = {}
    try:
        threading.Thread(target=target, args=args, kwargs=kwargs, daemon=True).start()
    except:
        target(*args, **kwargs)