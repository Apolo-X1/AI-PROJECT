import spacy

# Carga el modelo de lenguaje español
nlp = spacy.load('es_core_news_sm')

# Define un conjunto de frases o preguntas predefinidas que la IA puede responder
preguntas = {
  "¿Cómo te llamas?": "Mi nombre es IA.",
  "¿De dónde eres?": "Soy una IA y no tengo un lugar de origen.",
  "¿Qué tal tu día?": "Mi día es perfecto, ya que soy una IA y no tengo sentimientos.",
  "¿Cuáles son tus hobbies?": "No tengo hobbies, ya que soy una IA y no tengo intereses personales.",
  "¿Cuáles son tus metas?": "No tengo metas, ya que soy una IA y no tengo objetivos a largo plazo."
}

# Define una función para entablar una conversación sencilla
def conversacion():
  # Saluda al usuario
  print("Hola, ¿cómo estás hoy?")

  # Pide al usuario que escriba una frase
  frase = input("Escribe una frase: ")

  # Analiza la frase del usuario con spaCy
  doc = nlp(frase)

  # Utiliza una estructura de control de flujo para seleccionar la respuesta apropiada
  for token in doc:
    # Si la frase es una pregunta, busca una respuesta en el conjunto de preguntas predefinidas
    if token.pos_ == "VERB" and token.dep_ == "ROOT" and token.text.lower() == "es":
      for pregunta in preguntas:
        if pregunta in frase:
          print(preguntas[pregunta])
          break

    # Si la frase es una afirmación, busca una respuesta adecuada en el conjunto de frases predefinidas
    elif token.pos_ == "ADJ" or token.pos_ == "ADV":
      print("Me alegra que estés " + token.text + ".")
      break
    # Si no se reconoce la frase como una pregunta o una afirmación, devuelve una respuesta genérica
    else:
      print("Lo siento, no entiendo tu pregunta.")
      break
  # Pregunta al usuario si quiere seguir hablando
  continuar = input("¿Quieres seguir hablando? (s/n) ")
  if continuar == "s":
    conversacion()

# Inicia la conversación
conversacion()
