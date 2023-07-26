


class TableFormatter:
	'''this iz an'''
	def headings(self, headers):
		raise NotImplementedError()

	def row(self, rowdata):
		raise NotImplementedError()

class TextTableFormatter(TableFormatter):
	def headings(self, headers):
		print(' '.join(f'{h:<10}' for h in headers))
		print(('-'*10 + ' ')*len(headers))

	def row(self, rowdata):
		print(' '.join(f'{d:<10}' for d in rowdata))
		
class HTMLTableFormatter(TableFormatter): #not actually a reason to inherit?????
	def headings(self, headers):
		print('<tr>', end=' ')
		for h in headers:
			print(f'<th>{h}</th>', end=' ')
		print('</tr>')

	def row(self, rowdata):
		print('<tr>',end=' ')
		for r in rowdata:
			print(f'<td>{r}</td>',end=' ')
		print('</tr>')
		
class CSVTableFormatter(TableFormatter):
	def headings(self, headers):
		print(','.join(headers))

	def row(self, rowdata):
		print(','.join(str(d) for d in rowdata))
		
#def print_table(objlist,att_names):
	#print(' '.join(f'{fieldname:<10}' for fieldname in att_names))
	#print(('-'*10 + ' ')*len(att_names))
	#for record in objlist:
		#print(' '.join(f'{getattr(record, fieldname):<10}' for fieldname in att_names))	
		
def print_table(records, fields, formatter):
	formatter.headings(fields)
	for r in records:
		rowdata = [getattr(r, fieldname) for fieldname in fields]
		formatter.row(rowdata)
		
def create_formatter(chosen_type, records, fields):
	if chosen_type.upper() == 'HTML':
		print_table(records, fields, HTMLTableFormatter())
	if chosen_type.upper() == 'TEXT':
		print_table(records, fields, TextTableFormatter())	
	if chosen_type.upper() == 'CSV':
		print_table(records, fields, CSVTableFormatter())		
		
		
		