


class TableFormatter:
	'''this iz an abstract base class'''
	#i think it is pointless currently, if you remove the inheritance all the format classes work fine?
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

class redirect_stdout:
	def __init__(self, out_file):
		self.out_file = out_file
	def __enter__(self):
		self.stdout = sys.stdout
		sys.stdout = self.out_file
		return self.out_file
	def __exit__(self, ty, val, tb):
		sys.stdout = self.stdout
		
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
		
def create_formatter(name):
	if name == 'text':
		formatter_cls = TextTableFormatter
	elif name == 'csv':
		formatter_cls = CSVTableFormatter
	elif name == 'html':
		formatter_cls = HTMLTableFormatter	
	else:
		raise RuntimeError('Unknown format %s' % name)
	return formatter_cls()	
		
	