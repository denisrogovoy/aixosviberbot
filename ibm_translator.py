from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import secrets

authenticator = IAMAuthenticator(apikey=secrets.api_key)
language_translator = LanguageTranslatorV3(version="2018-05-01", authenticator=authenticator)
language_translator.set_service_url(secrets.url)


def recognize_language(viber_text):
    try:
        language = language_translator.identify(text=viber_text).get_result()
        #print(json.dumps(language, indent=2))
        return language["languages"][0]["language"]
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def translate(viber_text):
    print(viber_text)
    from_language=recognize_language(viber_text)
    print(from_language)
    if from_language!="uk":
        englishtext=viber_text
        if from_language!="en":
            translation = language_translator.translate(
                text=viber_text,
                model_id=(from_language+"-en")).get_result()
            print(json.dumps(translation, indent=2, ensure_ascii=False))
            englishtext=translation["translations"][0]["translation"]
        translatedText = language_translator.translate(
            text=englishtext,
            model_id="en-uk").get_result()
        print(json.dumps(translatedText, indent=2, ensure_ascii=False))
        return translatedText["translations"][0]["translation"]
    else:
        return viber_text
#models = language_translator.list_models().get_result()
#print(json.dumps(models, indent=2))
#print(translate("Добрый день"))


