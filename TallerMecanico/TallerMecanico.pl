% Hechos: síntomas observados en el vehículo
sintoma(falla_encendido).
sintoma(sobrecalentamiento).
sintoma(fuga_aceite).
sintoma(perdida_compresion).
sintoma(pastillas_desgastadas).
sintoma(pedal_freno_fondo).
sintoma(ruido_suspension).
sintoma(rebote_excesivo).

% Reglas de diagnóstico

% Fallas en el sistema de encendido
diagnostico(falla_encendido, 'Revisar bujias: verificar estado y limpieza.').
diagnostico(falla_encendido, 'Revisar bobinas de encendido: verificar funcionamiento.').
diagnostico(falla_encendido, 'Verificar cables de bujias: asegurar conexión y estado.').
diagnostico(falla_encendido, 'Considerar problema en la unidad de control electronico (ECU) si otros componentes estan bien.').

% Sobrecalentamiento
diagnostico(sobrecalentamiento, 'Verificar nivel de refrigerante y buscar fugas.').
diagnostico(sobrecalentamiento, 'Revisar el termostato: asegurar que abre correctamente.').
diagnostico(sobrecalentamiento, 'Verificar el funcionamiento del ventilador del radiador.').
diagnostico(sobrecalentamiento, 'Inspeccionar la bomba de agua: asegurar que circula el refrigerante.').
diagnostico(sobrecalentamiento, 'Considerar obstruccion en el radiador o mangueras.').

% Fugas de aceite
diagnostico(fuga_aceite, 'Identificar la fuente de la fuga (carter, retenes, juntas, etc.).').
diagnostico(fuga_aceite, 'Verificar el nivel de aceite regularmente.').
diagnostico(fuga_aceite, 'Reemplazar la junta o reten defectuoso.').
diagnostico(fuga_aceite, 'Asegurar que el tapón del cárter esté bien ajustado.').

% Pérdida de compresión
diagnostico(perdida_compresion, 'Realizar una prueba de compresion en los cilindros.').
diagnostico(perdida_compresion, 'Posibles causas: valvulas defectuosas, anillos de pistón desgastados, junta de culata dañada.').
diagnostico(perdida_compresion, 'Requiere reparacion interna del motor.').

% Problemas de Frenos
diagnostico(pastillas_desgastadas, 'Reemplazar las pastillas de freno.').
diagnostico(pastillas_desgastadas, 'Revisar el estado de los discos de freno.').
diagnostico(pedal_freno_fondo, 'Verificar el nivel de liquido de frenos y buscar fugas.').
diagnostico(pedal_freno_fondo, 'Purgar el sistema de frenos para eliminar aire.').
diagnostico(pedal_freno_fondo, 'Inspeccionar el cilindro maestro y las lineas de freno.').

% Suspensión del vehículo
diagnostico(ruido_suspension, 'Identificar la ubicacion del ruido (amortiguadores, bujes, rotulas, etc.).').
diagnostico(ruido_suspension, 'Inspeccionar visualmente los componentes de la suspension en busca de daños o desgaste.').
diagnostico(rebote_excesivo, 'Verificar el estado de los amortiguadores.').
diagnostico(rebote_excesivo, 'Considerar la posibilidad de resortes dañados o vencidos.').


% Ejemplo de consulta para un sintoma:
% ?- diagnosticar(sobrecalentamiento).

% Ejemplo de consulta para multiples sintomas:
% ?- diagnosticar_multiple([falla_encendido, fuga_aceite]).
