"""
AI Powered English/French Translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(version='2018-05-01', authenticator=auth)
translator.set_service_url(url)


def english_to_french(en_text):
    """
    Translates text from English to French using Watson service.
    """
    if isinstance(en_text, str) and en_text:
        translation = translator.translate(text=en_text, model_id='en-fr').get_result()
        fr_text = translation.get('translations')[0].get('translation')
    else:
        fr_text = en_text
    return fr_text


def french_to_english(fr_text):
    """
    Translates text from English to French using Watson service.
    """
    if isinstance(fr_text, str) and fr_text:
        translation = translator.translate(text=fr_text, model_id='fr-en').get_result()
        en_text = translation.get('translations')[0].get('translation')
    else:
        en_text = fr_text
    return en_text
