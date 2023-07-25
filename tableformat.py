

def print_table(objlist,att_names):
	print(' '.join(f'{fieldname:<10}' for fieldname in att_names))
	print(('-'*10 + ' ')*len(att_names))
	for record in objlist:
		print(' '.join(f'{getattr(record, fieldname):<10}' for fieldname in att_names))	