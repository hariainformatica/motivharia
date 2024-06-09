from motivharia.proveedorfrases import ProveedorFrases

proveedor = ProveedorFrases('csv', autosave=False)
print(0, str(proveedor.getFrases()))
print(1, proveedor.getFrase('La vida es bella', 'Anónimo3'))
print(2, proveedor.getFrasePorId(2))

print(3, proveedor.createFrase('La vida es bella2', 'Anónim2o'))

print(4, proveedor.updateFrase('La vida es bella', 'Anónimo', 'La vida es maravillosa', 'Anónimo'))

print(5, str(proveedor.getFrases()))

#proveedor.deleteFrase('La vida es maravillosa', 'Anónimo')

print(6, str(proveedor.getFrases()))

proveedor.close()

'''


proveedor = ProveedorFrases('sql', autosave=True)
print(str(proveedor.getFrases()))
print(proveedor.createFrase('La vida es bella2', 'Anónimo2'))
print(proveedor.updateFrase('La vida es bella', 'Anónimo', 'La vida es maravillosa3', 'Anónimo'))
proveedor.deleteFrase('La vida es maravillosa', 'Anónimo')
print(str(proveedor.getFrases()))

'''