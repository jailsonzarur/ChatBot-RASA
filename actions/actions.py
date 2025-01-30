from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionValidarEspecialidade(Action):

    def name(self) -> Text:
        return "action_validar_especialidade"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        especialidade = tracker.get_slot("especialidade_medico")
        periodo = tracker.get_slot("periodo_consulta")
        data_hora = tracker.get_slot("data_hora_consulta")

        especialidades_validas = ["endocrinologista", "nutricionista", "cardiologista"]

        if especialidade.lower() in especialidades_validas:
            dispatcher.utter_message(text=f"Especialidades confirmadas para atendimento. Certo, Seus dados ({especialidade} - {data_hora} - \
                                     {periodo}) foram encaminhados para a central de atendimento, logo logo \
                                     eles entrarão em contato com você! Posso ajudar com mais alguma coisa?")
            return []
        else:
            dispatcher.utter_message(text=f"Desculpe, essa especialidade não está disponível. As especialidades \
                                     disponíveis são Endocrinologista, Nutricionista e Cardiologista. Favor, digite: quero agendar uma nova consulta, \
                                     para reiniciar o diálogo.")
            return [SlotSet("especialidade_medico", None)]

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
