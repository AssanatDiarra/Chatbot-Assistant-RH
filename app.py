import streamlit as st
import random

#CHATBOT LOGIC 

class HRChatbot:
    def __init__(self):
        self.responses = {
            'greetings': {
                'keywords': ['bonjour', 'salut', 'hello', 'bonsoir'],
                'responses': [
                    "Bonjour 😊 Comment puis-je vous aider ?",
                    "Salut ! Je suis votre assistant RH."
                ]
            },
            'information': {
                'keywords': ['information', 'informations', 'info', 'Infornaton'],
                'responses': [
                    "Quelles genre d'information souhaitez vous avoir ?",
                    "Precisez nous ce que vous voulez."
                ]
            },
            'work_hours': {
                'keywords': ['horaires', 'heures de travail'],
                'responses': [
                    "Les horaires de travail sont de 8h à 17h, du lundi au vendredi."
                ]
            },
            'jours': {
                'keywords': ['jours ouvrables', 'ouvrables'],
                'responses': [
                    "Les jours ouvrables sont du lundi au vendredi."
                ]
            },
            'leave': {
                'keywords': ['jours de congés','congés', 'vacances'],
                'responses': [
                    "Les demandes de congé se font auprès du service RH."
                ]
            },
            'salary': {
                'keywords': ['salaire', 'paie'],
                'responses': [
                    "Le salaire est versé à la fin de chaque mois."
                ]
            },
            'contacts': {
                'keywords': ['contacter', 'contacts'],
                'responses': [
                    "Vous pouvez contacter les ressources humaines par email à rh@entreprise.com."
                ]
            },
            'securite': {
                'keywords': ['urgence', 'securité', "en cas d'urgence"],
                'responses': [
                    "En cas d’urgence, contactez immédiatement votre responsable ou le service de sécurité."
                ]
            }       
        }

    def classify_question(self, question):
        question = question.lower()
        for category, info in self.responses.items():
            for keyword in info['keywords']:
                if keyword in question:
                    return category
        return None

    def get_response(self, question):
        category = self.classify_question(question)
        if category:
            return random.choice(self.responses[category]['responses'])
        return "Désolé, je n'ai pas compris la question 🤔"


#STREAMLIT UI

st.set_page_config(page_title="Assistant RH", page_icon="🤖")
st.title("Assistant RH")

bot = HRChatbot()

# Initialisation de l'historique
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage de la conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Champ de saisie (style messagerie)
user_input = st.chat_input("Écrivez votre message...")

if user_input:
    # Message utilisateur
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Réponse du bot
    bot_response = bot.get_response(user_input)
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    # Rafraîchir pour afficher immédiatement
    st.rerun()
