from motivharia.proveedorfrases import ProveedorFrases

proveedor = ProveedorFrases('csv', autosave=True)
print(str(proveedor.getFrases()))
print(proveedor.getFrase('La vida es bella', 'Anónimo'))
print(proveedor.getFrasePorId(2))

print(proveedor.createFrase('La vida es bella', 'Anónimo'))

print(proveedor.updateFrase('La vida es bella', 'Anónimo', 'La vida es maravillosa', 'Anónimo'))

print(str(proveedor.getFrases()))

proveedor.deleteFrase('La vida es maravillosa', 'Anónimo')

print(str(proveedor.getFrases()))

proveedor.close()

proveedor = ProveedorFrases('sql', autosave=True)
print(str(proveedor.getFrases()))
print(proveedor.createFrase('La vida es bella', 'Anónimo'))
print(proveedor.updateFrase('La vida es bella', 'Anónimo', 'La vida es maravillosa', 'Anónimo'))
proveedor.deleteFrase('La vida es maravillosa', 'Anónimo')
print(str(proveedor.getFrases()))