#!/usr/bin/python
# -*- coding: utf-8 -*-

"Aplicativo Factura Electronica Libre"

from __future__ import with_statement   # for python 2.5 compatibility

__author__ = "Mariano Reingart (reingart@gmail.com)"
__copyright__ = "Copyright (C) 2014- Mariano Reingart"
__license__ = "LGPL 3.0"

# images were taken from Pythoncard's proof and widgets demos
# for more complete examples, see each control module

import datetime     # base imports, used by some controls and event handlers
import decimal
import time

import gui          # import gui2py package (shortcuts)

# set default locale to handle correctly numeric format (maskedit):
import wx, locale
#locale.setlocale(locale.LC_ALL, u'es_ES.UTF-8')
#loc = wx.Locale(wx.LANGUAGE_DEFAULT, wx.LOCALE_LOAD_DEFAULT)

# --- here go your event handlers ---



# --- gui2py designer generated code starts ---

with gui.Window(name='mywin', 
                title=u'Aplicativo Facturaci\xf3n Electr\xf3nica', 
                resizable=True, height='596px', left='181', top='52', 
                width='653px', 
                image='', ):
    with gui.MenuBar(name='menubar_83_155', ):
        with gui.Menu(name='menu_114', ):
            gui.MenuItemSeparator(name='menuitemseparator_130', )
    gui.StatusBar(name='statusbar_15_91', 
                  text=u'Servicio Web Factura Electr\xf3nica mercado interno (WSFEv1)', )
    with gui.Panel(name='panel'):
        with gui.Panel(label=u'Cliente:', name='cliente', 
                       height='114', left='8', top='6', width='633', image='', ):
            gui.Label(name='label_182_163', height='25', left='11', 
                      top='21', width='38', text=u'Documento:', )
            gui.ComboBox(name='combobox_416_70_647', text=u'CF', 
                         left='111', top='16', width='78', 
                         data_selection=u'CF', 
                         items=[u'CUIT', u'DNI', u'CF'], selection=2, 
                         string_selection=u'CF', )
            gui.TextBox(mask='##-########-#', name='textbox_228_157', 
                        left='192', top='17', width='110', 
                        value=u'20-26756539-3', )
            gui.Label(name='label_268_164', height='31', left='316', 
                      top='22', width='61', text=u'Nombre:', )
            gui.TextBox(name='textbox_400_158_1018', height='27', 
                        left='383', top='17', width='240', 
                        value=u'Mariano Reingart', )
            gui.Label(name='label_322_165', left='10', top='50', 
                      width='72', text=u'Domicilio', )
            gui.TextBox(name='domicilio', multiline=True, 
                        height='57', left='112', top='49', width='189', 
                        value=u'Castagna 4942', )
            gui.Label(name='label_530_167', left='321', top='89', 
                      width='58', text=u'E-Mail:', )
            gui.Label(name='label_530_167_1258', height='17', left='321', 
                      top='56', width='58', text=u'IVA:', )
            gui.ComboBox(name='combobox_416_70', text=u'Responsable Inscripto', 
                         left='383', top='49', width='190', 
                         data_selection=u'Responsable Inscripto', 
                         items=[u'Consumidor Final', u'Responsable Inscripto', u'Exento', u'Monotributo'], 
                         selection=1, string_selection=u'Responsable Inscripto', )
            gui.TextBox(name='email', left='383', top='82', 
                        width='240', value=u'reingart@gmail.com', )
        gui.Label(name='label_24_16', height='17', left='13', top='130', 
                  width='80', text=u'Comprobante:', )
        gui.ComboBox(name=u'tipo_cbte', text=u'Factura A', left='115', top='125', 
                     width='170', 
                     items=[u'Factura A', u'Nota de Credito A', u'Nota de Crédito A', 
                            u'Factura B', u'Nota de Débito B', u'Nota de Crédito B', 
                            u'Factura C', u'Nota de Débito C', u'Nota de Crédito C', ], 
                     string_selection=u'', )
        gui.Label(name='label_356_21_178', height='17', left='290', 
                  top='130', width='20', text=u'N\xb0:', )
        gui.TextBox(mask='##', name=u'pto_vta', alignment='right', 
                    left='318', top='125', width='47', 
                    value=99, )
        gui.TextBox(mask='########', name=u'nro_cbte', alignment='right', 
                    left='366', top='125', width='92', 
                    value=12345678, )
        gui.Label(name='label_356_21_155', height='17', left='467', 
                  top='130', width='60', text=u'Fecha:', )
        gui.TextBox(id=290, mask='date', name='textbox_290', left='517', top='125', 
                    width='122', 
                    value=datetime.date(2014, 5, 27), )
        with gui.Notebook(name='notebook', height='197', left='7', 
                          top='249', width='631', selection=0, ):
            with gui.TabPanel(name='tab_art', selected=True, 
                              text=u'Art\xedculos', ):
                with gui.GridView(name=u'items', height='118', left='10', 
                                  top='6', width='610', 
                                  fgcolor=u'#3C3C3C', row_label=""):
                    gui.GridColumn(align='right', name=u'qty', type='double:4,2', represent=u'%0.2f', 
                                   text=u'Cant.', width=50, )
                    gui.GridColumn(name=u'codigo', represent='%s', type='text', 
                                   text=u'C\xf3digo', width=75, )
                    gui.GridColumn(name=u'ds', represent='%s', type='text', 
                                   text=u'Descripci\xf3n', width=200, )
                    gui.GridColumn(align='right', name=u'precio', type='double:11,2', 
                                   represent=u'%0.2f', text=u'Precio', 
                                   width=125, )
                    gui.GridColumn(align='center', name=u'iva_id', represent='%s', 
                                   text=u'IVA', width=50, 
                                   type='choice:exento,no gravado,0%,10.5%,21%,27%', )
                    gui.GridColumn(align='right', name=u'subtotal', type='double:15,2', 
                                   represent=u'%0.2f', text=u'Subtotal', 
                                   width=125, )
                gui.Button(label=u'Agregar', name='button_36_161', left='6', 
                           top='127', width='85px', )
                gui.Button(id=493, label=u'Borrar', name='button_588_157_493', 
                           left='94', top='127', width='85px', )
                gui.Button(label=u'Modificar', name='button_588_157', left='183', 
                           top='128', width='85px', )
            with gui.TabPanel(name='tabpanel_850', selected=False, 
                              text=u'Al\xedcuotas IVA', ):
                with gui.ListView(name='listview_211', height='100', 
                                  left='15', top='34', width='357', item_count=0, 
                                  sort_column=1, ):
                    gui.ListColumn(name=u'iva_id', text=u'ID', width=25, )
                    gui.ListColumn(name=u'alicuota', text=u'Al\xedcuota', 
                                   width=100, )
                    gui.ListColumn(name=u'base_imp', text=u'Base Imp.', width=100, )
                    gui.ListColumn(name=u'importe', text=u'Importe IVA', 
                                   width=125, )
                gui.Label(name='label_387', left='395', top='103', 
                          text=u'Exento:', )
                gui.TextBox(name='textbox_416', left='519', top='67', )
                gui.Label(name='label_387_542', height='17', left='393', 
                          top='40', width='99', text=u'Neto Gravado:', )
                gui.TextBox(name='textbox_416_552', height='27', 
                            left='519', top='36', width='92', )
                gui.Label(name='label_387_630', height='17', left='393', 
                          top='71', width='81', text=u'No Gravado:', )
                gui.TextBox(name='textbox_416_642', height='27', 
                            left='519', top='97', width='92', )
                gui.Label(name='label_388', left='20', top='11', 
                          text=u'Subtotales de IVA liquidado por al\xedcuota:', )
            with gui.TabPanel(id=869, name='tributos', selected=False, 
                              text=u'Otros tributos', ):
                with gui.GridView(name='grilla', height='102', 
                                  left='12', top='18', width='606', item_count=0, 
                                  sort_column=0, ):
                    gui.GridColumn(name='tributo_id', text=u'id', width=25, type='number', )
                    gui.GridColumn(name='impuesto', text=u'Impuesto', width=75, type='choice:nacional,provincial,municipal,interno,otro',)
                    gui.GridColumn(name='desc', text=u'Descripci\xf3n', width=200, type='text', )
                    gui.GridColumn(name='base_imp', text=u'Base Imp.', width=75, type='double:11,2',)
                    gui.GridColumn(name='alic', text=u'Al\xedcuota', width=75, type='double:3,2',)
                    gui.GridColumn(name='importe', text=u'Importe', width=125, type='double:15,2',)
                gui.Button(label=u'Agregar', name='button_36_161', left='6', 
                           top='127', width='85px', )
                gui.Button(id=493, label=u'Borrar', name='button_588_157_493', 
                           left='94', top='127', width='85px', )
                gui.Button(label=u'Modificar', name='button_588_157', left='183', 
                           top='128', width='85px', )
            with gui.TabPanel(name='tabpanel_638', selected=False, 
                              text=u'Observaciones', ):
                gui.Label(name='label_1324', left='15', top='87', 
                          text=u'Obs. Comerciales:', )
                gui.Label(id=1938, name='label_1324_1938', height='17', left='14', 
                          top='18', width='106', text=u'Obs. Generales:', )
                gui.TextBox(name='textbox_715', multiline=True, 
                            height='65', left='147', top='87', width='468', 
                            )
                gui.TextBox(name='textbox_715_1534', multiline=True, 
                            height='65', left='147', top='18', width='467', 
                            )
        gui.TextBox(mask='#####.##', name=u'total_1052', 
                    alignment='right', left='520', top='485', width='115', 
                    value=1000.0, )
        gui.TextBox(mask='#####.##', name=u'total_1052_1438', 
                    alignment='right', left='520', top='455', width='115', 
                    value=1000.0, )
        gui.Label(id=1892, name='label_469_345_1892', alignment='right', 
                  height='17', left='466', top='488', width='41', 
                  text=u'IVA:', )
        gui.Label(name='label_469_345_226', alignment='right', 
                  height='17', left='468', top='519', width='41', 
                  text=u'Total:', )
        gui.Label(name='label_469_345', alignment='right', height='17', 
                  left='406', top='461', width='110', 
                  text=u'Otros Tributos:', )
        with gui.Panel(label=u'Autorizaci\xf3n AFIP:', name='panel_3072', 
                       height='121', left='15', top='449', width='320', 
                       image='', ):
            gui.Label(name='label_26_372_2499_2861', height='17', 
                      left='13', top='28', width='39', text=u'CAE:', )
            gui.TextBox(name='textbox_81_362', left='78', top='23', width='133', 
                        value=u'123456789012345', )
            gui.Label(name='label_26_372', left='11', top='90', width='39', 
                      text=u'Resultado:', )
            gui.TextBox(mask='date', name=u'fecha_cbte_2201', 
                        alignment='center', left='94', top='54', 
                        
                        value=datetime.date(2014, 2, 11), )
            gui.Button(label=u'Obtener', name=u'imprimir', left='224', 
                       top='21', width='75', )
            gui.Label(name='label_26_372_217', height='17', left='11', 
                      top='60', width='71', text=u'Venc. CAE:', )
            gui.RadioButton(label=u'Aceptado', name='radiobutton_188_241', 
                            left='95', top='88', width='75', 
                            value=True, )
            gui.RadioButton(label=u'Rechazado', name='radiobutton_188', 
                            left='199', top='88', width='100', 
                            )
            gui.Button(label=u'Imprimir', name=u'imprimir_472', 
                       left='224', top='53', width='75', )
        with gui.Panel(label=u'Conceptos a incluir', name='panel_403', 
                       height='89', left='8', top='157', width='265', 
                       image='', ):
            gui.CheckBox(label=u'Productos', name='checkbox_32_32', left='13', 
                         top='24', width='99', 
                         )
            gui.CheckBox(label=u'Servicios', name='checkbox_180_32', left='12', 
                         top='49', width='110', 
                         )
        with gui.Panel(label=u'Per\xedodo Facturado', name='panel_404', 
                       height='89', left='276', top='158', width='363', 
                       image='', ):
            gui.Label(name='label_272_30', left='192', top='25', width='49', 
                      text=u'Hasta:', )
            gui.TextBox(mask='date', name='textbox_306_31', left='240', top='20', 
                        width='113', 
                        value=datetime.date(2014, 5, 28), )
            gui.TextBox(mask='date', name='textbox_306_31_486', 
                        left='241', top='51', width='113', 
                        value=datetime.date(2014, 5, 28), )
            gui.TextBox(id=998, mask='date', name='textbox_306_31_486_998', 
                        left='72', top='20', width='113', 
                        value=datetime.date(2014, 5, 28), )
            gui.Label(name='label_272_30_1442', height='17', left='113', 
                      top='59', width='49', text=u'Vto. para el Pago:', )
            gui.Label(name='label_272_30_1442_1458', height='17', 
                      left='17', top='25', width='49', text=u'Desde:', )
        gui.TextBox(mask='#####.##', name=u'total', alignment='right', left='520', 
                    top='515', width='115', 
                    value=1000.0, )
        gui.Image(name='image_507_571', height='36', left='394', top='546', 
                  width='238', filename='sistemas-agiles.png', )
        gui.Image(name='image_33_540', height='50', left='350', top='495', 
                  width='100', filename='logo-pyafipws.png', )

# --- gui2py designer generated code ends ---


# obtener referencia a la ventana principal:
mywin = gui.get("mywin")
panel = mywin['panel']

# agrego item de ejemplo:
new_key = 'my_key_%s' % time.time()
panel['notebook']['tab_art']['items'].items.append({'qty': '1', 'codigo': '1111', 
    'ds': u"Honorarios  p/administración  de alquileres", 'precio': 1000., 'iva_id': 21, 
    'subtotal': 1210.})

if __name__ == "__main__":
    mywin.show()
    gui.main_loop()
