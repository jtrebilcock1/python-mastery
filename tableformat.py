from abc import ABC, abstractmethod

class ColumnFormatMixin:
	#to be used with classes that have a row method
	formats = []
	def row(self, rowdata):
		rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
		super().row(rowdata)
		
class UpperHeadersMixin:
	#extend functionality of class that have headings method
	def headings(self, headers):
		super().headings([h.upper() for h in headers])		
		
class TableFormatter(ABC):
	'''this iz an abstract base class'''
	@abstractmethod
	def headings(self, headers):
		raise NotImplementedError()

	@abstractmethod
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
	if isinstance(formatter, TableFormatter):
		formatter.headings(fields)
		for r in records:
				rowdata = [getattr(r, fieldname) for fieldname in fields]
				formatter.row(rowdata)
	else:
		raise TypeError('object is not a member of TableFormatter')
		
def create_formatter(name, column_formats=None, upper_headers=False):
		
	if name == 'text':
		formatter_cls = TextTableFormatter
	elif name == 'csv':
		formatter_cls = CSVTableFormatter
	elif name == 'html':
		formatter_cls = HTMLTableFormatter	
	else:
		raise RuntimeError('Unknown format %s' % name)
	
	if column_formats:
		#column_formats input should be like ['"%s"','%d','%0.2f']
		class formatter_cls(ColumnFormatMixin, formatter_cls):
			formats = column_formats

	if upper_headers:
		class formatter_cls(UpperHeadersMixin, formatter_cls):
			pass	
	return formatter_cls()	
		
	