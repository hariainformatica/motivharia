# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(?<=\().*(?=\))"

test_str = ("Podrás amenazarme, encadenarme, encerrarme o exiliarme. Pero yo te recuerdo que ni Zeus podría quitarme el poder de decidir mi actitud. (Epicteto)\n"
	"El hombre conquista el mundo al conquistarse a sí mismo. (Zenón de Citio)\n"
	"¿Por qué deberíamos prestar tanta atención a lo que piensa la mayoría?. (Sócrates)\n"
	"Algunas cosas dependen de nosotros y otras no dependen de nosotros. (Epicteto)\n"
	"Nada, a mi modo de ver, es una mejor prueba de una mente bien ordenada que la capacidad de un hombre de detenerse justo donde está y pasar algún tiempo en su propia compañía. (Seneca)\n"
	"La tranquilidad que viene cuando dejas de preocuparte por lo que dicen. (Marco Aurelio)\n"
	"Nadie tiene el poder de tener todo lo que desea pero está en sus manos no querer lo que no tiene y, utilizar con entusiasmo de la mejor manera lo que si tiene. (Séneca)\n"
	"Cuando por la mañana salga el sol, recordaré que: tropezaré con algún inoportuno, con alguien ingrato, con algún insolente, un mentiroso, un envidioso, un egoísta. Todos estos vicios les sobrevinieron por ignorancia de lo que es bueno y lo que es malo. Pero yo, habiendo observado que la naturaleza del bien es lo bello, y que la del mal es lo mezquino y, que la condición misma del que comete un error es tal que no deja de ser de los míos, compartiendo el potencial de la razón y siendo una parte divina del todo en el orden natural y que además, nada de lo que haga puede afectarme, porque nadie puede mancharme con su bajeza. Entonces, tampoco podría enojarme contra mi prójimo ni aborrecerle, porque hemos nacido para trabajar en conjunto; como lo hacen los pies, las manos, los párpados, y las dos filas de dientes— la inferior y la superior. Actuar, pues, como adversarios los unos con los otros es ir en contra del orden natural. Y, ¿no son acaso el enojo y el rechazo una forma de mezquindad?. (Marco Aurelio)\n"
	"Quien le tenga miedo a la muerte no hará cosas dignas de quien está vivo. (Séneca)\n"
	"Es hora de que te des cuenta de que tienes algo más poderoso y milagroso que las cosas que te afectan y no te hacen bailar como un títere. (Marco Aurelio)\n"
	"No es el hombre que tiene muy poco, sino el hombre que anhela más, que es pobre. (Seneca)\n"
	"Las apariencias en la mente son de cuatro tipos. Las cosas son lo que parecen ser; o no lo son, ni lo parecen ser; o lo son, y no parecen ser; o no lo son, y sin embargo parecen serlo. Con razón apuntar en todos estos casos es la tarea del sabio. (Epicteto)\n"
	"Eres un alma pequeña que lleva un cadáver. (Epicteto)\n"
	"Los hombres no tienen miedo de las cosas, sino de cómo las ven. (Epicteto)\n"
	"Filosofar es esto: examinar y afinar los criterios. (Epicteto)\n"
	"Cuando hayas de sentenciar, procura olvidar a los litigantes y acordarte sólo de la causa.(Epicteto)\n"
	"Si quieres mejorar, conténtate con que te consideren tonto y estúpido. (Epicteto)\n"
	"¿Y cómo pretendes amar si no sabes que está bien y qué está mal?. (Epicteto)\n"
	"Primero aprende el significado de lo que dices y luego habla. (Epicteto)\n"
	"Únete a lo que es espiritualmente superior, independientemente de lo que otras personas piensan o hacen. Mantén tus verdaderas aspiraciones sin importar lo que esté sucediendo a tu alrededor. (Epicteto)\n"
	"Así como el Sol no espera que las oraciones y conjuros se levanten, sino que resplandece y es bien recibido por todos: así que tú tampoco esperes aplaudir y gritar y alabar para cumplir con tu deber; no, haz el bien por tu propia voluntad, y serás amado como el Sol. (Epicteto)\n"
	"La verdad triunfa por sí misma, la mentira necesita siempre complicidad. (Epicteto)\n"
	"La naturaleza ha dado a los hombres una lengua y dos oídos, para que podamos oír de los demás el doble de lo que hablamos. (Epicteto)\n"
	"La prudencia es el más excelso de todos los bienes. (Epicteto)\n"
	"Si logras algo con trabajo puede que el resultado no dure mucho, pero el bien perdura. Si hacés algo vergonzoso con el objetivo de obtener placer, el placer pasa rápidamente, pero la vergüenza se queda. (Musonio Rufo)\n"
	"Todo lo que escuchamos es solo una opinión, no un hecho. Lo que vemos es una perspectiva, no la realidad. (Marco Aurelio)\n"
	"Tienes poder sobre tu mente, no en eventos externos. Date cuenta de esto y encontrarás fuerza. (Marco Aurelio)\n"
	"Donde hay un ser humano, hay una oportunidad para la amabilidad. (Seneca)\n"
	"A menudo tenemos más miedo que dolor; y sufrimos más en la imaginación que en la realidad. (Seneca)\n"
	"No es que tengamos poco tiempo, sino que perdemos mucho. (Séneca)\n"
	"Toma este momento. Sumérgete en sus detalles. Responde a esta persona, este desafío, esta acción. Deja las evasiones. (Epicteto)\n"
	"Si no está bien, no lo hagas, si no es verdad, no lo digas. (Marco Aurelio)")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.