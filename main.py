from motivharia.proveedorautores import ProveedorAutores

proveedor = ProveedorAutores('csv', autosave=True)
print(str(proveedor.getAutores()))
print(str(proveedor.getAutor('Séneca')))
print(proveedor.getAutorPorId(2))

print(proveedor.createAutor('Platón'))

print(proveedor.updateAutor('Platón', 'Platón de Atenas'))


print(str(proveedor.getAutores()))

#print(proveedor.deleteAutor('Platón de Atenas'))

proveedor.close()

proveedor = ProveedorAutores('sql', autosave=True)
print(str(proveedor.getAutores()))
print(proveedor.createAutor('Platón'))
print(proveedor.updateAutor('Platón', 'Platón de Atenas'))
#proveedor.deleteAutor('Platón de Atenas')
print(str(proveedor.getAutores()))