# from mr_box_peripheral_board.proxy import SerialProxy
# from mr_box_peripheral_board.zstage_ui import ZStageUI
# from IPython.display import display
#
# proxy = SerialProxy(port="COM5")
# ui = ZStageUI(proxy)
#
# display(ui.widget)
#
# breakpoint()

import panel as pn
import ipywidgets as widgets

slider = widgets.IntSlider(min=0, max=10, value=5)

pn.extension('ipywidgets')  # Enable the IPyWidget extension
pn.pane.IPyWidget(slider)