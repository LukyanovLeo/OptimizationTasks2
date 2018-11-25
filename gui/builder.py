def set_geometry(widget, X, Y):
    windowWidth = widget.winfo_reqwidth()
    windowHeight = widget.winfo_reqheight()

    positionRight = int(widget.winfo_screenwidth() / 2 - windowWidth - 25 / 2)
    positionDown = int(widget.winfo_screenheight() / 2 - windowHeight - 50 / 2)

    widget.geometry("{}x{}+{}+{}".format(X, Y, positionRight, positionDown))