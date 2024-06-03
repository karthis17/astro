tools=[
    {
        "type": "function",
        "function": {
            "name": "astro_details",
            "description": "Provides comprehensive astrological insights based on an individual's birth details. The response includes information about the ascendant, Varna, Vashya, Yoni, Gan, Nadi, SignLord, sign, Nakshatra, NakshatraLord, Charan, Yog, Karan, Tithi, Yunja, Tatva, name_alphabet, and Paya. These insights are crucial for understanding various aspects of a person's life, personality, and future prospects according to Vedic astrology.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude, eg: 25.2056"
                    }
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "fallback_response",
            "description": "Function to handle and respond to errors during API calls or processing failures. It returns a structured error message, indicating that an error has occurred and providing details to assist the user in understanding or resolving the issue.",
            "parameters": {
               "type": "object",
               "properties": {
                  "error_message": {
                      "type": "string",
                      "description": "Error message detailing what went wrong during the API call or processing."
                    }
                },
            "required": ["error_message"]
           }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "planets",
            "description": "Provides astrological information about the positions and characteristics of planets at the time of birth. The response includes details about each planet's name, position in the zodiac sign, speed, sign lord, associated nakshatra and its lord, house placement, and retrograde status.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "ayanamsha",
            "description": "Provides the value of ayanamsha for a given date, time, and location. Ayanamsha is the angular difference between the tropical and sidereal zodiacs, crucial for sidereal astrological calculations. The response includes the ayanamsha value in degrees and its formatted representation in hours, minutes, and seconds.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "ghat_chakra",
            "description": "Returns the Panchang details (Hindu calendar) for a given date and location, including the month, tithi (lunar day), day of the week, nakshatra (lunar mansion), yog (auspicious time), karan (half of a tithi), pahar (day division), and moon phase. These elements are essential for determining auspicious times and understanding lunar influences in Vedic astrology.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude, eg: 25.2056"
                    }
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "general_house_report",
            "description": "Provides a horoscope report for a specific planet in a person's natal chart. The response includes insights into the individual's personality traits, physical characteristics, and potential challenges related to that planet's influence on their chart. Available planets include sun, moon, mars, mercury, jupiter, venus, and saturn.",
            "parameters": {
                "type": "object",
                "properties": {
                    "planet_name": {
                        "type": "string",
                        "description": "Name of the planet (sun, moon, mars, mercury, jupiter, venus, saturn)"
                    },
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["planet_name", "day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "general_rashi_report",
            "description": "Provides a two-line report on a person's nature based on their astrological sun sign or 'rashi'. The report offers insights into their personality traits, tendencies, and potential areas of strength or weakness. It also includes advice on how to channel energies and overcome any negative tendencies. Available planets include moon, mars, mercury, jupiter, venus, and saturn.",
            "parameters": {
                "type": "object",
                "properties": {
                    "planet_name": {
                        "type": "string",
                        "description": "Name of the planet (moon, mars, mercury, jupiter, venus, saturn)"
                    },
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["planet_name", "day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "general_ascendant_report",
            "description": "Provides a report on a person's Ascendant or Rising sign. The report includes a detailed description of the individual's personality traits, tendencies, strengths, and weaknesses based on their Ascendant sign. It also offers insights into the spiritual lessons that the individual needs to learn based on their Ascendant sign, helping them understand their life's purpose and direction.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "lalkitab_remedies",
            "description": "Provides Lal Kitab remedies for a given planet name. The response contains the planet name, house placement, Lal Kitab descriptions, and remedies for that planet. The remedies include suggestions such as avoiding certain clothing colors, performing certain actions for a certain duration, and abstaining from certain food and drink, to mitigate the negative effects of the planet's placement.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "lalkitab_debts",
            "description": "Provides information about various types of karmic debts according to Lalkitab astrology. The response includes the debt name, indications of the debt in a person's horoscope, and the events or consequences that may arise from not addressing the debt. This insight helps individuals understand and mitigate the impact of these debts on their life.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "kalsarpa_details",
            "description": "Provides information about the presence and type of KalSarpa Dosha in a horoscope and its effects. The response includes details such as the type of KalSarpa Dosha present, the house in which it is located, and its effects on various aspects of the native's life such as belief in religion, hurdles in life, career, foreign travel, health, family, and legal matters. Understanding KalSarpa Dosha is crucial for mitigating its negative effects through appropriate remedies.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "manglik",
            "description": "Calculates the presence of Manglik Dosha in a person's horoscope. Manglik Dosha, also known as Kuja Dosha, is an astrological condition that is believed to have adverse effects on marriage and relationships. The response indicates whether Manglik Dosha is present or not, based on the position of Mars in the birth chart.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "sadhesati_current_status",
            "description": "Checks the current status of Sadhe Sati based on the consideration date. Sadhe Sati is a period of approximately 7.5 years during which Saturn transits through the 12th, 1st, and 2nd houses from the natal Moon. The response determines whether the user is currently undergoing Sadhe Sati and provides a brief explanation of its effects on different stages of life.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "sadhesati_life_details",
            "description": "Provides details about Sadhe Sati, a period of seven and a half years during which Saturn moves through three signs, and its effect on a person's life. The response includes a summary of Sadhe Sati, and a report that contains the dates, phases, and effects of Sadhe Sati based on the user's birth moon sign and Saturn's position. This information helps individuals understand the impact of this significant astrological period on their life.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "pitra_dosha_report",
            "description": "Provides a report on the presence of Pitri Dosha in a horoscope, including a description of what Pitri Dosha is, whether it is present or not, the rules matched, remedies, and effects. The response includes information such as the rules that cause Pitri Dosha, remedies to overcome it, and its potential negative effects, such as delays in marriage and education or inherited diseases. Understanding and addressing Pitri Dosha can help mitigate its impact on various aspects of life.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "horo_chart",
            "description": "Provides data for various divisional charts (D-charts) based on the chart type specified by the chart_id. The data points include various planetary positions along with the ascendant and their respective house positions, which are essential for drawing and analyzing astrological charts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "chart_id": {
                        "type": "string",
                        "description": "The type of chart for which you want data (e.g., 'D1' for Rasi chart, 'D9' for Navamsa chart)"
                    },
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["chart_id", "day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "major_yogini_dasha",
            "description": "Provides information on the timing and duration of different yoginis or periods of time in Vedic astrology. The response includes details such as the dasha name, start and end dates, duration, and start and end times in milliseconds for each period. This information is crucial for understanding the influence of various yoginis on different aspects of life during their respective periods.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "sub_yogini_dasha",
            "description": "Provides a list of sub-dashas for a given major dasha in Vedic astrology. The response includes dasha IDs, names, start and end dates, and their respective timestamps. This information is crucial for understanding the timing and influence of various sub-dashas during the major dasha period.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "current_yogini_dasha",
            "description": "Returns the current major, sub, and sub-sub period of a yogini dasha with their respective start and end dates. This information is crucial for understanding the ongoing influences and trends in a person's life according to Vedic astrology.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "major_vdasha",
            "description": "Provides information on the major periods or 'Maha Dasha' in Vimshottari Dasha system of Vedic astrology. The response includes details such as the dasha name, start and end dates, and duration for each major period. This information is essential for understanding the long-term trends and influences in a person's life according to their birth chart.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "current_vdasha",
            "description": "Provides information about the current Vimshottari Dasha periods according to Vedic astrology. It includes the start and end dates, as well as the ruling planet, for the major, minor, sub-minor, sub-sub-minor, and sub-sub-sub-minor periods. This information is essential for understanding the ongoing astrological influences and their potential impact on various aspects of an individual's life.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "current_vdasha_all",
            "description": "Provides information on all five levels of the Vimshottari Dasha system according to Vedic astrology. The response includes the current major (Maha Dasha), minor (Antar Dasha), sub-minor (Pratyantar Dasha), sub-sub-minor (Sookshma Dasha), and sub-sub-sub-minor (Praana Dasha) periods, along with their start and end dates and ruling planets. This comprehensive insight is crucial for understanding the nuanced astrological influences on an individual's life.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
      "type": "function",
      "function": {
           "name": "varshaphal_month_chart",
           "description": "API Endpoint for Varshaphal Month Chart",
           "parameters": {
              "type": "object",
              "properties": {
                  "day": {
                     "type": "integer",
                     "description": "Day of birth, eg: 10"
                },
                  "month": {
                      "type": "integer",
                      "description": "Month of birth, eg: 5"
                },
                   "year": {
                       "type": "integer",
                       "description": "Year of birth, eg: 1990"
                },
                   "varshaphal_year": {
                       "type": "integer",
                       "description": "Varshaphal year for the chart, eg: 2021"
                 
                },
                   "hour": {
                        "type": "integer",
                        "description": "Hour, eg: 19"
                },
                   "min": {
                        "type": "integer",
                        "description": "Minute, eg: 55"
                },
                  "lat": {
                        "type": "number",
                        "description": "Latitude, eg: 19.2056"
                },
                  "lon": {
                        "type": "number",
                        "description": "Longitude, eg: 25.2056"
                }
            },
           "required": ["day", "month", "year", "varshaphal_year", "hour", "min", "lat", "lon"]
           }
        }
    },
    {
      "type": "function",
      "function": {
           "name": "varshaphal_details",
           "description": "The varshaphal_details API provides information about a person's yearly horoscope based on their birth date. The response includes details such as the year, age of the person, birth date, and details about different planetary positions and lords.",
           "parameters": {
              "type": "object",
              "properties": {
                  "day": {
                     "type": "integer",
                     "description": "Day of birth, eg: 10"
                },
                  "month": {
                      "type": "integer",
                      "description": "Month of birth, eg: 5"
                },
                   "year": {
                       "type": "integer",
                       "description": "Year of birth, eg: 1990"
                },
                   "varshaphal_year": {
                       "type": "integer",
                       "description": "Varshaphal year for the chart, eg: 2021"
                 
                },
                   "hour": {
                        "type": "integer",
                        "description": "Hour, eg: 19"
                },
                   "min": {
                        "type": "integer",
                        "description": "Minute, eg: 55"
                },
                  "lat": {
                        "type": "number",
                        "description": "Latitude, eg: 19.2056"
                },
                  "lon": {
                        "type": "number",
                        "description": "Longitude, eg: 25.2056"
                }
            },
           "required": ["day", "month", "year", "varshaphal_year", "hour", "min", "lat", "lon"]
           }
        }
    },
    {
      "type": "function",
      "function": {
           "name": "varshaphal_year_chart",
           "description": "This API endpoint provides the Varshaphal Yearly Chart, which is an annual horoscope chart based on the solar return. It calculates and provides detailed insights into the astrological predictions for the year, based on the specific birth date, time, and location of an individual. The chart includes detailed planetary positions and significant astrological aspects for the year.",
           "parameters": {
              "type": "object",
              "properties": {
                  "day": {
                     "type": "integer",
                     "description": "Day of birth, eg: 10"
                },
                  "month": {
                      "type": "integer",
                      "description": "Month of birth, eg: 5"
                },
                   "year": {
                       "type": "integer",
                       "description": "Year of birth, eg: 1990"
                },
                   "varshaphal_year": {
                       "type": "integer",
                       "description": "Varshaphal year for the chart, eg: 2021"
                 
                },
                   "hour": {
                        "type": "integer",
                        "description": "Hour, eg: 19"
                },
                   "min": {
                        "type": "integer",
                        "description": "Minute, eg: 55"
                },
                  "lat": {
                        "type": "number",
                        "description": "Latitude, eg: 19.2056"
                },
                  "lon": {
                        "type": "number",
                        "description": "Longitude, eg: 25.2056"
                }
            },
           "required": ["day", "month", "year", "varshaphal_year", "hour", "min", "lat", "lon"]
           }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "daily_nakshatra_prediction",
            "description": "Provides daily astrological predictions based on a person's birth moon sign and nakshatra, including aspects of health, emotions, profession, luck, personal life, and travel.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "basic_gem_suggestion",
            "description": "Provides gemstone suggestions based on different aspects of a person's life, including details like the gemstone name, semi-gemstone, finger to wear it on, weight in carats, metal to wear it with, day to wear it, and the deity associated.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "rudraksha_suggestion",
            "description": "Provides a recommendation for which combination of rudraksha beads to wear based on the user's horoscope, including the name, image URL, and benefits of the recommended beads.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "integer",
                        "description": "Date of birth, eg: 10"
                    },
                    "month": {
                        "type": "integer",
                        "description": "Month of birth, eg: 5"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Year of birth, eg: 1990"
                    },
                    "hour": {
                        "type": "integer",
                        "description": "Hour of birth, eg: 19"
                    },
                    "min": {
                        "type": "integer",
                        "description": "Minute of birth, eg: 55"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude of birthplace, eg: 19.2056"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude of birthplace, eg: 25.2056"
                    }
                    
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "advanced_panchang",
            "description": "Provides an in-depth analysis of Hindu Panchang elements such as tithi (lunar day), nakshatra (lunar mansion), yog (auspicious timing), and karan (half-day period), detailing their astrological significance and daily impact",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {"type": "integer", "description": "Panchang day, eg: 10"},
                    "month": {"type": "integer", "description": "Panchang month, eg: 7"},
                    "year": {"type": "integer", "description": "Panchang year, eg: 2014"},
                    "hour": {"type": "integer", "description": "Hour of birth, eg: 19"},
                    "min": {"type": "integer", "description": "Minute of birth, eg: 55"},
                    "lat": {"type": "number", "description": "Panchang place latitude, eg: 18.7250"},
                    "lon": {"type": "number", "description": "Panchang place longitude, eg: 72.250"}
                    
                },
                "required": ["day", "month", "year", "hour","min","lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "chaughadiya_muhurta",
            "description": "Provides a list of muhurta (auspicious time) categories and their time intervals based on Vedic astrology.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {"type": "integer", "description": "Panchang day, eg: 10"},
                    "month": {"type": "integer", "description": "Panchang month, eg: 7"},
                    "year": {"type": "integer", "description": "Panchang year, eg: 2014"},
                    "hour": {"type": "integer", "description": "Hour of birth, eg: 19"},
                    "min": {"type": "integer", "description": "Minute of birth, eg: 55"},
                    "lat": {"type": "number", "description": "Panchang place latitude, eg: 18.7250"},
                    "lon": {"type": "number", "description": "Panchang place longitude, eg: 72.250"}
                
                },
                "required": ["day", "month", "year", "hour","min","lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "hora_muhurta",
            "description": "Provides information on the planetary hours for a given day based on Vedic astrology.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {"type": "integer", "description": "Panchang day, eg: 10"},
                    "month": {"type": "integer", "description": "Panchang month, eg: 7"},
                    "year": {"type": "integer", "description": "Panchang year, eg: 2014"},
                    "hour": {"type": "integer", "description": "Hour of birth, eg: 19"},
                    "min": {"type": "integer", "description": "Minute of birth, eg: 55"},
                    "lat": {"type": "number", "description": "Panchang place latitude, eg: 18.7250"},
                    "lon": {"type": "number", "description": "Panchang place longitude, eg: 72.250"}
                    
                },
                "required": ["day", "month", "year","hour","min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "planet_ashtak",
            "description": "Returns the Ashtak Varga table for a specified planet, including points in each zodiac sign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "planet_name": {"type": "string", "description": "Planet name, e.g., sun, moon, mars, mercury, jupiter, venus, saturn, ascendant"},
                    "day": {"type": "integer", "description": "Date of birth, eg: 10"},
                    "month": {"type": "integer", "description": "Month of birth, eg: 5"},
                    "year": {"type": "integer", "description": "Year of birth, eg: 1990"},
                    "hour": {"type": "integer", "description": "Hour of birth, eg: 19"},
                    "min": {"type": "integer", "description": "Minute of birth, eg: 55"},
                    "lat": {"type": "number", "description": "Latitude of birthplace, eg: 19.2056"},
                    "lon": {"type": "number", "description": "Longitude of birthplace, eg: 25.2056"}
                },
                "required": ["planet_name", "day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "sarvashtak",
            "description": "Provides Ashtak Varga points for all significant planets and the ascendant in a horoscope.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {"type": "integer", "description": "Date of birth, eg: 10"},
                    "month": {"type": "integer", "description": "Month of birth, eg: 5"},
                    "year": {"type": "integer", "description": "Year of birth, eg: 1990"},
                    "hour": {"type": "integer", "description": "Hour of birth, eg: 19"},
                    "min": {"type": "integer", "description": "Minute of birth, eg: 55"},
                    "lat": {"type": "number", "description": "Latitude of birthplace, eg: 19.2056"},
                    "lon": {"type": "number", "description": "Longitude of birthplace, eg: 25.2056"}
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon"]
            }
        }
    },
    {
     "type": "function",
     "function": {
       "name": "match_making_detailed_report",
       "description": "Provides a comprehensive match-making analysis, including Ashtakoota and Manglik dosha, between a male and a female.",
       "parameters": {
        "type": "object",
        "properties": {
          "m_day": {"type": "integer", "description": "Male's day of birth"},
          "m_month": {"type": "integer", "description": "Male's month of birth"},
          "m_year": {"type": "integer", "description": "Male's year of birth"},
          "m_hour": {"type": "integer", "description": "Male's hour of birth"},
          "m_min": {"type": "integer", "description": "Male's minute of birth"},
          "m_lat": {"type": "number", "description": "Male's latitude of birthplace"},
          "m_lon": {"type": "number", "description": "Male's longitude of birthplace"},
          "f_day": {"type": "integer", "description": "Female's day of birth"},
          "f_month": {"type": "integer", "description": "Female's month of birth"},
          "f_year": {"type": "integer", "description": "Female's year of birth"},
          "f_hour": {"type": "integer", "description": "Female's hour of birth"},
          "f_min": {"type": "integer", "description": "Female's minute of birth"},
          "f_lat": {"type": "number", "description": "Female's latitude of birthplace"},
          "f_lon": {"type": "number", "description": "Female's longitude of birthplace"},
        
        },
          "required": [
           "m_day", "m_month", "m_year", "m_hour", "m_min", "m_lat", "m_lon",
           "f_day", "f_month", "f_year", "f_hour", "f_min", "f_lat", "f_lon"
        ]
      }
     }
    },
    {
        "type": "function",
        "function": {
            "name": "match_planet_details",
            "description": "Returns details of all nine planets and lagna for both male and female for compatibility analysis.",
            "parameters": {
                "type": "object",
                "properties": {
                    "m_day": {"type": "integer", "description": "Male's day of birth"},
                    "m_month": {"type": "integer", "description": "Male's month of birth"},
                    "m_year": {"type": "integer", "description": "Male's year of birth"},
                    "m_hour": {"type": "integer", "description": "Male's hour of birth"},
                    "m_min": {"type": "integer", "description": "Male's minute of birth"},
                    "m_lat": {"type": "number", "description": "Male's latitude of birthplace"},
                    "m_lon": {"type": "number", "description": "Male's longitude of birthplace"},
                    "f_day": {"type": "integer", "description": "Female's day of birth"},
                    "f_month": {"type": "integer", "description": "Female's month of birth"},
                    "f_year": {"type": "integer", "description": "Female's year of birth"},
                    "f_hour": {"type": "integer", "description": "Female's hour of birth"},
                    "f_min": {"type": "integer", "description": "Female's minute of birth"},
                    "f_lat": {"type": "number", "description": "Female's latitude of birthplace"},
                    "f_lon": {"type": "number", "description": "Female's longitude of birthplace"}
                    
                },
                "required": [
                    "m_day", "m_month", "m_year", "m_hour", "m_min", "m_lat", "m_lon",
                    "f_day", "f_month", "f_year", "f_hour", "f_min", "f_lat", "f_lon"
                ]
            }
        }
    }, 
    {
        "type": "function",
        "function": {
            "name": "match_ashtakoot_points",
            "description": "Provides the Ashtakoota matching score between a male and a female, detailing the points scored in each koot.",
            "parameters": {
                "type": "object",
                "properties": {
                    "m_day": {"type": "integer", "description": "Male's day of birth"},
                    "m_month": {"type": "integer", "description": "Male's month of birth"},
                    "m_year": {"type": "integer", "description": "Male's year of birth"},
                    "m_hour": {"type": "integer", "description": "Male's hour of birth"},
                    "m_min": {"type": "integer", "description": "Male's minute of birth"},
                    "m_lat": {"type": "number", "description": "Male's latitude of birthplace"},
                    "m_lon": {"type": "number", "description": "Male's longitude of birthplace"},            
                    "f_day": {"type": "integer", "description": "Female's day of birth"},
                    "f_month": {"type": "integer", "description": "Female's month of birth"},
                    "f_year": {"type": "integer", "description": "Female's year of birth"},
                    "f_hour": {"type": "integer", "description": "Female's hour of birth"},
                    "f_min": {"type": "integer", "description": "Female's minute of birth"},
                    "f_lat": {"type": "number", "description": "Female's latitude of birthplace"},
                    "f_lon": {"type": "number", "description": "Female's longitude of birthplace"}
                    
                },
                "required": [
                    "m_day", "m_month", "m_year", "m_hour", "m_min", "m_lat", "m_lon",
                    "f_day", "f_month", "f_year", "f_hour", "f_min", "f_lat", "f_lon"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "match_manglik_report",
            "description": "Provides information about mangal dosha for both individuals, including impact, cancellation rules, and remedies.",
            "parameters": {
                "type": "object",
                "properties": {
                    "m_day": {"type": "integer", "description": "Male's day of birth"},
                    "m_month": {"type": "integer", "description": "Male's month of birth"},
                    "m_year": {"type": "integer", "description": "Male's year of birth"},
                    "m_hour": {"type": "integer", "description": "Male's hour of birth"},
                    "m_min": {"type": "integer", "description": "Male's minute of birth"},
                    "m_lat": {"type": "number", "description": "Male's latitude of birthplace"},
                    "m_lon": {"type": "number", "description": "Male's longitude of birthplace"},    
                    "f_day": {"type": "integer", "description": "Female's day of birth"},
                    "f_month": {"type": "integer", "description": "Female's month of birth"},
                    "f_year": {"type": "integer", "description": "Female's year of birth"},
                    "f_hour": {"type": "integer", "description": "Female's hour of birth"},
                    "f_min": {"type": "integer", "description": "Female's minute of birth"},
                    "f_lat": {"type": "number", "description": "Female's latitude of birthplace"},
                    "f_lon": {"type": "number", "description": "Female's longitude of birthplace"}
                    
                },
                "required": [
                    "m_day", "m_month", "m_year", "m_hour", "m_min", "m_lat", "m_lon",
                    "f_day", "f_month", "f_year", "f_hour", "f_min", "f_lat", "f_lon"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "match_obstructions",
            "description": "Analyzes potential obstructions in the match between two individuals, providing detailed insights into astrological hindrances.",
            "parameters": {
                "type": "object",
                "properties": {
                    "m_day": {"type": "integer", "description": "Male's day of birth"},
                    "m_month": {"type": "integer", "description": "Male's month of birth"},
                    "m_year": {"type": "integer", "description": "Male's year of birth"},
                    "m_hour": {"type": "integer", "description": "Male's hour of birth"},
                    "m_min": {"type": "integer", "description": "Male's minute of birth"},
                    "m_lat": {"type": "number", "description": "Male's latitude of birthplace"},
                    "m_lon": {"type": "number", "description": "Male's longitude of birthplace"},                 
                    "f_day": {"type": "integer", "description": "Female's day of birth"},
                    "f_month": {"type": "integer", "description": "Female's month of birth"},
                    "f_year": {"type": "integer", "description": "Female's year of birth"},
                    "f_hour": {"type": "integer", "description": "Female's hour of birth"},
                    "f_min": {"type": "integer", "description": "Female's minute of birth"},
                    "f_lat": {"type": "number", "description": "Female's latitude of birthplace"},
                    "f_lon": {"type": "number", "description": "Female's longitude of birthplace"}
                },
                "required": [
                    "m_day", "m_month", "m_year", "m_hour", "m_min", "m_lat", "m_lon",
                    "f_day", "f_month", "f_year", "f_hour", "f_min", "f_lat", "f_lon"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "match_dashakoot_points",
            "description": "Provides the dashakoot points for matching the compatibility between male and female, analyzing ten different aspects.",
            "parameters": {
                "type": "object",
                "properties": {
                    "m_day": {"type": "integer", "description": "Male's day of birth"},
                    "m_month": {"type": "integer", "description": "Male's month of birth"},
                    "m_year": {"type": "integer", "description": "Male's year of birth"},
                    "m_hour": {"type": "integer", "description": "Male's hour of birth"},
                    "m_min": {"type": "integer", "description": "Male's minute of birth"},
                    "m_lat": {"type": "number", "description": "Male's latitude of birthplace"},
                    "m_lon": {"type": "number", "description": "Male's longitude of birthplace"},               
                    "f_day": {"type": "integer", "description": "Female's day of birth"},
                    "f_month": {"type": "integer", "description": "Female's month of birth"},
                    "f_year": {"type": "integer", "description": "Female's year of birth"},
                    "f_hour": {"type": "integer", "description": "Female's hour of birth"},
                    "f_min": {"type": "integer", "description": "Female's minute of birth"},
                    "f_lat": {"type": "number", "description": "Female's latitude of birthplace"},
                    "f_lon": {"type": "number", "description": "Female's longitude of birthplace"}
                },
                "required": [
                    "m_day", "m_month", "m_year", "m_hour", "m_min", "m_lat", "m_lon",
                    "f_day", "f_month", "f_year", "f_hour", "f_min", "f_lat", "f_lon"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "papasamyam_details",
            "description": "Analyzes the dosha points in the horoscope of an individual, providing details on the impact of planets and remedial measures.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {"type": "integer", "description": "Date of birth"},
                    "month": {"type": "integer", "description": "Month of birth"},
                    "year": {"type": "integer", "description": "Year of birth"},
                    "hour": {"type": "integer", "description": "Hour of birth"},
                    "min": {"type": "integer", "description": "Minute of birth"},
                    "lat": {"type": "number", "description": "Latitude of birthplace"},
                    "lon": {"type": "number", "description": "Longitude of birthplace"},
                    "gender": {"type": "string", "description": "Gender, e.g., male or female"}
                },
                "required": ["day", "month", "year", "hour", "min", "lat", "lon", "gender"]
            }
        }
    },
    {
      "type": "function",
      "function": {
           "name": "get_current_time_india",
           "description": "Fetches the current date and time for the Indian Standard Time (IST) timezone using the timeapi.io service. The response includes the full date and time in IST, along with details like the year, month, day, hour, minute, seconds, and timezone.",
           "parameters": {
              "type": "object",
              "properties": {
                 "timeZone": { "type": "string","description": "Timezone for which current time is needed, eg: Asia/Kolkata"}
                },
               "required": ["timeZone"]
            }
        }
    }
]
