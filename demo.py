# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "anywidget==0.9.18",
#     "marimo",
#     "mohtml==0.1.4",
# ]
# ///

import marimo

__generated_with = "0.11.29"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from modraw import Draw
    from mohtml import img
    return Draw, img, mo


@app.cell
def _(Draw, mo):
    widget = mo.ui.anywidget(Draw(width=1000, height=450))
    return (widget,)


@app.cell
def _(widget):
    widget
    return


@app.cell
def _(img, widget):
    img(src=widget.value["base64"])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
