# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class garaje(models.Model):
#     _name = 'garaje.garaje'
#     _description = 'garaje.garaje'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date


class aparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir características de un aparcamiento'

    name = fields.Char('Dirección', required=True)
    plazas = fields.Integer(string='Plazas',required=True)

    #relaciones entre tablas
    coche_ids = fields.One2many('garaje.coche','aparcamiento_id',string='Coches')
    moto_ids = fields.One2many('garaje.moto','aparcamiento_idM',string='Motos')

class coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permite definir las características de un coche'
    _order = 'name'

    name = fields.Char(string='Matrícula', required=True, size=7)
    modelo = fields.Char(string='Modelo',required=True)
    construido = fields.Date(string = 'Fecha de construcción')
    consumo = fields.Float('Consumo', (4, 1), default=0.0, help='Consumo promedio cada 100 kms')
    averiado = fields.Boolean(string='Averiado', default=False)
    #store=True no lo pone porque al pasar los años no los suma
    annos = fields.Integer('Años', compute='_get_annos')
    descripcion = fields.Text('Descipcion')

    #relaciones entre tablas
    aparcamiento_id = fields.Many2one('garaje.aparcamiento',string='Aparcamiento')
    mantenimiento_ids= fields.Many2many('garaje.mantenimiento',string='Mantenimientos')


    @api.depends('construido')
    def _get_annos(self):
        for coche in self:
            hoy = date.today()
            coche.annos=relativedelta(hoy, coche.construido).years

    # restricciones, mismo formato que en la id
    _sql_constraints=[('name_uniq', 'unique(name)', 'La matricula ya existe')]

class moto(models.Model):
    _name = 'garaje.moto'
    _description = 'Permite definir las características de una moto'
    _order = 'nameM'

    nameM = fields.Char(string='Matrícula', required=True, size=7)
    modeloM = fields.Char(string='Modelo',required=True)
    construidoM = fields.Date(string = 'Fecha de construcción')
    consumoM = fields.Float('Consumo', (4, 1), default=0.0, help='Consumo promedio cada 100 kms')
    averiadoM = fields.Boolean(string='Averiado', default=False)
    annosM = fields.Integer('Años', compute='_get_annos')
    descripcionM = fields.Text('Descripcion')

    #relaciones entre tablas
    aparcamiento_idM = fields.Many2one('garaje.aparcamiento',string='Aparcamiento')
    mantenimiento_idsM= fields.Many2many('garaje.mantenimiento',string='Mantenimientos')


    @api.depends('construidoM')
    def _get_annos(self):
        for moto in self:
            hoy = date.today()
            moto.annosM=relativedelta(hoy, moto.construidoM).years

    # restricciones, mismo formato que en la id
    _sql_constraints=[('name_uniq', 'unique(nameM)', 'La matricula ya existe')]

class mantenimiento(models.Model):
    _name='garaje.mantenimiento'
    _description='Permite definir mantenimientos rutinarios sobre conjuntos de coches'
    _order='fecha'

    #name = fields.Char()
    fecha = fields.Date('Fecha',required=True, default=fields.date.today())
    tipo = fields.Selection(string='Tipo', selection=[('l','Lavar'),('r','Revisión'),('m','Mecánica'),('p','Pintura')], default='l')
    coste = fields.Float('Coste', (8,2), help='Coste total del mantenimiento')

    #relaciones entre tablas
    coche_ids= fields.Many2many('garaje.coche',string='Coches')
    moto_ids= fields.Many2many('garaje.moto',string='Motos')



    def name_get(self):
        resultados=[]
        for mantenimiento in self:
            descripcion = f'{len(mantenimiento.coche_ids)} coches -{mantenimiento.coste} €'
            resultados.append((mantenimiento.id, descripcion))
            return resultados


