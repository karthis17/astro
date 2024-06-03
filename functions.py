import requests
import json
import base64

user_id='629800'
astro_api_key='5904c37117950e8f719422a9b19a9925d8962145'



def fallback_response(error_message):
    return {
        "error": True,
        "message": f"An error occurred: {error_message}. Please try again later or contact support."
    }


def get_current_time_india(time_zone='Asia/Kolkata'):
    url = 'https://timeapi.io/api/Time/current/zone'
    params = {'timeZone': time_zone}
    headers = {'accept': 'application/json'}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response status is 4xx or 5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))


    
def varshaphal_month_chart(day, month, year, hour, min,lat,lon,varshaphal_year):
    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5,
        "varshaphal_year":varshaphal_year
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/current_vdasha_date"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))


def varshaphal_details(day, month, year, hour, min,lat,lon,varshaphal_year):
    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5,
        "varshaphal_year":varshaphal_year
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/varshaphal_details"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
    

def varshaphal_year_chart(day, month, year, hour, min,lat,lon,varshaphal_year):
    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5,
        "varshaphal_year":varshaphal_year
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/varshaphal_year_chart"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
    
    

def base(type,day, month, year, hour, min,lat,lon):

    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/{type}"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))

def astro_details(day, month, year, hour, min,lat,lon):
    return base('astro_details',day, month, year, hour, min,lat,lon)
def planets(day, month, year, hour, min,lat,lon):
    return base('planets',day, month, year, hour, min,lat,lon)
def ayanamsha(day, month, year, hour, min,lat,lon):
    return base('ayanamsha',day, month, year, hour, min,lat,lon)
#print(ayanamsha(17,12,2001,11,28,18,81))
def ghat_chakra(day, month, year, hour, min,lat,lon):
    return base('ghat_chakra',day, month, year, hour, min,lat,lon)

def general_house_report(planet_name,day, month, year, hour, min,lat,lon):
    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/general_house_report/{planet_name}"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
#print(general_house_report('sun',17,12,2001,11,28,18,81))
    
def general_rashi_report(planet_name,day, month, year, hour, min,lat,lon):
    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/general_rashi_report/{planet_name}"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
#print(general_rashi_report('sun',17,12,2001,11,28,18,81))



def general_ascendant_report(day, month, year, hour, min,lat,lon):
    return base('general_ascendant_report',day, month, year, hour, min,lat,lon)
#print(general_ascendant_report(17,12,2001,11,28,18,88))



def lalkitab_debts(day, month, year, hour, min,lat,lon):
    return base('lalkitab_debts',day, month, year, hour, min,lat,lon)
#print(lalkitab_debts(17,12,2001,11,28,18,88))

def lalkitab_remedies(day, month, year, hour, min,lat,lon):
    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/lalkitab_remedies/moon"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
  
#print(lalkitab_planets(17,12,2001,11,28,18,88))
def kalsarpa_details(day, month, year, hour, min,lat,lon):
    return base('kalsarpa_details',day, month, year, hour, min,lat,lon)
#print(kalsarpa_details(17,12,2001,11,28,18,88))

def manglik(day, month, year, hour, min,lat,lon):
    return base('manglik',day, month, year, hour, min,lat,lon)

#print(manglik(17,12,2001,11,28,18,88))

def sadhesati_current_status(day, month, year, hour, min,lat,lon):
    return base('sadhesati_current_status',day, month, year, hour, min,lat,lon)

def sadhesati_life_details(day, month, year, hour, min,lat,lon):
    return base('sadhesati_life_details',day, month, year, hour, min,lat,lon)

def pitra_dosha_report(day, month, year, hour, min,lat,lon):
    return base('pitra_dosha_report',day, month, year, hour, min,lat,lon)


def horo_chart(chart_id,day, month, year, hour, min,lat,lon):


    data = {
        "chart_id":chart_id,
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/horo_chart/:chart_id"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
    
def major_yogini_dasha(day, month, year, hour, min,lat,lon):
    return base('major_yogini_dasha',day, month, year, hour, min,lat,lon)



def sub_yogini_dasha(day, month, year, hour, min,lat,lon):
    return base('sub_yogini_dasha',day, month, year, hour, min,lat,lon)

def current_yogini_dasha(day, month, year, hour, min,lat,lon):
    return base('current_yogini_dasha',day, month, year, hour, min,lat,lon)



def major_vdasha(day, month, year, hour, min,lat,lon):
    return base('major_vdasha',day, month, year, hour, min,lat,lon)


def current_vdasha(day, month, year, hour, min,lat,lon):
    return base('current_vdasha',day, month, year, hour, min,lat,lon)

def current_vdasha_all(day, month, year, hour, min,lat,lon):
    return base('current_vdasha_all',day, month, year, hour, min,lat,lon)

def daily_nakshatra_prediction(day, month, year, hour, min,lat,lon):
    return base('daily_nakshatra_prediction',day, month, year, hour, min,lat,lon)



def basic_gem_suggestion(day, month, year, hour, min,lat,lon):
    return base('basic_gem_suggestion',day, month, year, hour, min,lat,lon)



def rudraksha_suggestion(day, month, year, hour, min,lat,lon):
    return base('rudraksha_suggestion',day, month, year, hour, min,lat,lon)

def advanced_panchang(day, month, year, hour, min,lat,lon):
    return base('advanced_panchang',day, month, year, hour, min,lat,lon)


def hora_muhurta(day, month, year, hour, min,lat,lon):
    return base('hora_muhurta',day, month, year, hour, min,lat,lon)


def chaughadiya_muhurta(day, month, year, hour, min,lat,lon):
    return base('chaughadiya_muhurta',day, month, year, hour, min,lat,lon)


def planet_ashtak(day, month, year, hour, min,lat,lon):


    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/planet_ashtak/:planet_name"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
    
def sarvashtak(day, month, year, hour, min,lat,lon):
    return base('sarvashtak',day, month, year, hour, min,lat,lon)


def base_match(type,m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon):


    data = {
        "m_day": m_day,
        "m_month": m_month,
        "m_year": m_year,
        "m_hour": m_hour,
        "m_min": m_min,
        "m_lat": m_lat,
        "m_lon": m_lon,
        "m_tzone":5.5,
        "f_day": f_day,
        "f_month": f_month,
        "f_year": f_year,
        "f_hour": f_hour,
        "f_min": f_min,
        "f_lat": f_lat,
        "f_lon": f_lon,
        "f_tzone":5.5
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/{type}"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
    


   
def match_ashtakoot_points(m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon):
    return base_match('match_ashtakoot_points',m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon)

   
def match_obstructions(m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon):
    return base_match('match_obstructions',m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon)

   
def match_astro_details(m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon):
    return base_match('match_astro_details',m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon)

 
def match_planet_details(m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon):
    return base_match('match_planet_details',m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon)

def match_making_detailed_report (m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon):
    return base_match('match_making_detailed_report',m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon)

def match_manglik_report(m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon):
    return base_match('match_manglik_report',m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon)


 
def match_dashakoot_points(m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon):
    return base_match('match_dashakoot_points',m_day,m_month,m_year,m_hour,m_min,m_lat,m_lon,f_day,f_month,f_year,f_hour,f_min,f_lat,f_lon)


def papasamyam_details(day,month,year,hour,min,lat,lon,gender):
    
    data = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone":5.5,
        "gender": gender
    }
    auth_string = f"{user_id}:{astro_api_key}"
    auth = "Basic " + base64.b64encode(auth_string.encode()).decode()
    headers = {"Authorization": auth, "Content-Type": 'application/json'}
    url = f"https://json.astrologyapi.com/v1/papasamyam_details"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return fallback_response(str(e))
    


