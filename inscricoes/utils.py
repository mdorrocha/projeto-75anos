import xlwt
from datetime import datetime, date


def export_xlwt(model, values_list, fields):

    modelname = model._meta.verbose_name_plural.lower()
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet(modelname, cell_overwrite_ok=True)
    data = '{:%d-%m-%Y}'.format(date.today())
    nome_arquivo = 'inscrições-' + str(data)

    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

    for j, f in enumerate(fields):
        if fields[j] == 'id':
            fields[j] = 'Inscrição'
        else:
            fields[j] = fields[j].capitalize()
        sheet.write(0, j, fields[j])
    for row, rowdata in enumerate(values_list):
        for col, val in enumerate(rowdata):
            if isinstance(val, datetime):
                style = datetime_style
            elif isinstance(val, date):
                style = date_style
            else:
                style = default_style
            if col == 5:
                val = 'Sim' if val else 'Não'
            sheet.write(row + 1, col, val, style=style)

    return book, nome_arquivo

