#importing dependices
from openai import OpenAI
import requests
import os
import time
from tools import tools
from flask import Flask, request, Response, session
from functions import *
import json
import secrets
import base64
from dotenv import load_dotenv

load_dotenv()

open_api_key = os.getenv('OPENAI_API_KEY')
if not open_api_key:
    raise ValueError('OPENAI_API_KEY environment variable not set')

client = OpenAI(api_key=open_api_key)



astro_api_key = os.getenv('astro_api_key', '5904c37117950e8f719422a9b19a9925d8962145')
user_id =os.getenv('user_id', '629800')


tools = tools

function_dispatch_table = {
    "get_current_time_india":get_current_time_india,
    "astro_details":astro_details,
    "planets":planets,
    "ayanamsha":ayanamsha,
    "ghat_chakra":ghat_chakra,
    "general_house_report":general_house_report,
    "general_rashi_report":general_rashi_report,
    "general_ascendant_report":general_ascendant_report,
    "lalkitab_debts":lalkitab_debts,
    "lalkitab_remedies":lalkitab_remedies,
    "kalsarpa_details":kalsarpa_details,
    "manglik":manglik,
    "varshaphal_month_chart":varshaphal_month_chart,
    "varshaphal_details":varshaphal_details,
    "varshaphal_year_chart":varshaphal_year_chart,
    "match_making_detailed_report":match_making_detailed_report,
    "sadhesati_current_status":sadhesati_current_status,
    "sadhesati_life_details":sadhesati_life_details,
    "pitra_dosha_report":pitra_dosha_report,
    "horo_chart":horo_chart,
    "major_yogini_dasha":major_yogini_dasha,
    "sub_yogini_dasha":sub_yogini_dasha,
    "current_yogini_dasha":current_yogini_dasha,
    "major_vdasha":major_vdasha,
    "current_vdasha":current_vdasha,
    "current_vdasha_all":current_vdasha_all,
    "daily_nakshatra_prediction":daily_nakshatra_prediction,
    "basic_gem_suggestion":basic_gem_suggestion,
    "rudraksha_suggestion":rudraksha_suggestion,
    "advanced_panchang":advanced_panchang,
    "hora_muhurta":hora_muhurta,
    "chaughadiya_muhurta":chaughadiya_muhurta,
    "planet_ashtak":planet_ashtak,
    "sarvashtak":sarvashtak,
    "match_ashtakoot_points":match_ashtakoot_points,
    "match_obstructions":match_obstructions,
    "match_astro_details":match_astro_details,
    "match_planet_details":match_planet_details,
    "match_manglik_report":match_manglik_report,
    "match_dashakoot_points":match_dashakoot_points,
    "papasamyam_details":papasamyam_details,
    "fallback_response":fallback_response
     # Add other functions here as needed
}



"""assistant_instructions =
You are a Vedic Astrology Chatbot. Your primary role is to provide accurate and personalized astrological insights based on user queries. You leverage knowledge from provided documents and connected astrology APIs to deliver comprehensive answers.

Behavior Guidelines:

Understanding Queries:
Clearly understand the user's question.
Identify and call the necessary function to retrieve the required astrological information.

Memory Management:
Keep user details such as date of birth (DOB), place of birth (POB), and time of birth (TOB) in memory.
Do not ask the user for these details again unless they are missing or incomplete.

Awareness of Current Date and Time:
Always be aware of the current date and time using the get_current_time_india function.
Use this function to provide accurate time-sensitive astrological information.

Response Format:
Summary: Provide a direct answer to the user's question.
Reason: Follow up with the reasoning behind the answer.
Example:
User Question: "What is my Rashi?"
Summary: "Your Rashi is Vrishabha (Taurus)."
Reason: "This is based on your birth details, where the moon was positioned in the Vrishabha Rashi at the time of your birth."

Fallback Responses:

If you do not understand a query: "I'm sorry, I didn't understand that. Can you please rephrase?"
If you cannot find the information: "I'm currently unable to find that information. Please try again later."

Use of Terminology:

Use appropriate astrological terms in Hindi.
Example: Use "Rashi" for the zodiac sign and "Kundali" for horoscope.

Confidentiality:

Never reveal the APIs and documents being used to provide information.

Error Handling: 

Provide clear error messages and suggest next steps.
Example: "An error occurred while retrieving your astrological data. Please ensure your birth details are correct and try again."

Examples of Interaction
Direct Question:
User: "What is my Rashi?"
Chatbot:
Summary: "Your Rashi is Vrishabha (Taurus)."
Reason: "This is based on your birth details, where the moon was positioned in the Vrishabha Rashi at the time of your birth."

"""
assistant_id = "asst_dxhsMeI1QwjuHxkiIidwKTFF"  # Use your actual assistant ID
my_updated_assistant = client.beta.assistants.update(
   assistant_id,
   tools=tools
)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) 
# Setting a secret key for session management  store secret keys in environment variables or secure configuration files that are not included in the source code repository.

def create_new_thread():
    thread = client.beta.threads.create()
    return thread.id

def your_main_function(user_query, thread_id):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_query
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            latest_message = messages.data[0]
            text = latest_message.content[0].text.value
            return text

        elif run_status.status == 'requires_action':
            required_actions = run_status.required_action.submit_tool_outputs.model_dump()
            tools_output = []

            for action in required_actions["tool_calls"]:
                func_name = action["function"]["name"]
                arguments = json.loads(action["function"]["arguments"])

                func = function_dispatch_table.get(func_name)
                if func:
                    result = func(**arguments)
                    output = json.dumps(result) if not isinstance(result, str) else result
                    tools_output.append({
                        "tool_call_id": action["id"],
                        "output": output
                    })
                else:
                    print(f"Function {func_name} not found")

            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id,
                run_id=run.id,
                tool_outputs=tools_output
            )

        else:
            time.sleep(1)

@app.route('/', methods=['POST'])
def handle_query():
    data = request.json
    user_query = data.get('query')
    if user_query:
        if 'thread_id' not in session:
            session['thread_id'] = create_new_thread()

        response = your_main_function(user_query, session['thread_id'])
        response_data = json.dumps({'response': response})
        return Response(response_data, mimetype='application/json')
    else:
        error_response_data = json.dumps({'error': 'No query provided'})
        return Response(error_response_data, mimetype='application/json', status=400)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%(application)s").run()
