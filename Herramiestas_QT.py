def Centrar_Buttons_Cajas( Tam_Ventana , Tam_Ventana_Reducida , Tam_Buttons , Cant_Buttons ):
	#Tam_Ventana: Tamanio de la ventana total
	#Tam_Ventana_Reducida: Tamanio de la ventana donde se introducen los botones
	#Tam_Buttons: Tamanio de los Botones [ no debe pasar el Tam_Ventana_Reducida ]
	#Cant_Buttons: Cantidad de Botones que se quiere introducir
	# -->> [ Retorna Arreglo con posiciones Iniciales de los Botones ]
	
	if( Tam_Ventana >= Tam_Ventana_Reducida and Tam_Ventana_Reducida>=Tam_Buttons*Cant_Buttons and Cant_Buttons>0):
		Mitad_Ventana_Total = Tam_Ventana/2 
		Mitad_Ventana_Principal = Tam_Ventana_Reducida/2

		Comienzo_Ventana_Principal = Mitad_Ventana_Total - Mitad_Ventana_Principal
		Comienzo_Sub_Ventana = Comienzo_Ventana_Principal #0

		Tam_Sub_Ventanas = Tam_Ventana_Reducida/Cant_Buttons
		Array_Posiciones_Button = []	

		for num_Ventana in range( Cant_Buttons ):

			Centro_posicion_Button = (Comienzo_Sub_Ventana + (Comienzo_Sub_Ventana+Tam_Sub_Ventanas))/2
			Array_Posiciones_Button.append( [Centro_posicion_Button-Tam_Buttons/2,Centro_posicion_Button-Tam_Buttons/2+Tam_Buttons ] )

			Comienzo_Sub_Ventana = Comienzo_Sub_Ventana+Tam_Sub_Ventanas
		
		return Array_Posiciones_Button #Retorna Arreglo
	
	#Error en Tam Ventanas o Buttons
	print("<<<---- Tamanio de Ventanas o Botton no Posible ---->>> [error func: Centrar_Buttons]")	

	

print( Centrar_Buttons_Cajas( 200, 100 , 30 , 1 ) )
