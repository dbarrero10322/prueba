class NewModule(models.Model):
    _name = 'new_module.new_module'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()
