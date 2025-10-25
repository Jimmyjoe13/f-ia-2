# ai_integration.py
import openai
import requests
import json
from ai_config import AIConfig
from errors import RuntimeError

class AIIntegration:
    """Module d'intégration des plateformes d'IA pour le langage F-IA"""
    
    def __init__(self):
        self.config = AIConfig()
        self._setup_openai()
    
    def _setup_openai(self):
        """Configuration d'OpenAI"""
        if self.config.is_openai_configured():
            openai.api_key = self.config.OPENAI_API_KEY
    
    def appeler_ia(self, plateforme, modele, message, temperature=None, max_tokens=None):
        """
        Fonction principale pour appeler une IA depuis F-IA
        
        Args:
            plateforme (str): 'openai' ou 'deepseek'
            modele (str): nom du modèle à utiliser
            message (str): message à envoyer à l'IA
            temperature (float): créativité (0.0 à 1.0)
            max_tokens (int): nombre maximum de tokens
        
        Returns:
            str: réponse de l'IA
        """
        try:
            # Paramètres par défaut
            temperature = temperature or self.config.DEFAULT_TEMPERATURE
            max_tokens = max_tokens or self.config.DEFAULT_MAX_TOKENS
            
            if plateforme.lower() == 'openai':
                return self._call_openai(modele, message, temperature, max_tokens)
            elif plateforme.lower() == 'deepseek':
                return self._call_deepseek(modele, message, temperature, max_tokens)
            else:
                raise RuntimeError(f"Plateforme IA non supportée: {plateforme}")
                
        except Exception as e:
            raise RuntimeError(f"Erreur lors de l'appel IA: {str(e)}")
    
    def _call_openai(self, modele, message, temperature, max_tokens):
        """Appel vers OpenAI"""
        if not self.config.is_openai_configured():
            raise RuntimeError("OpenAI non configuré. Vérifiez votre clé API dans .env")
        
        try:
            # Utilisation de la nouvelle API OpenAI v1.0+
            client = openai.OpenAI(api_key=self.config.OPENAI_API_KEY)
            
            response = client.chat.completions.create(
                model=modele,
                messages=[
                    {"role": "user", "content": message}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            raise RuntimeError(f"Erreur OpenAI: {str(e)}")
    
    def _call_deepseek(self, modele, message, temperature, max_tokens):
        """Appel vers DeepSeek"""
        if not self.config.is_deepseek_configured():
            raise RuntimeError("DeepSeek non configuré. Vérifiez votre clé API dans .env")
        
        try:
            headers = {
                "Authorization": f"Bearer {self.config.DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": modele,
                "messages": [
                    {"role": "user", "content": message}
                ],
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            response = requests.post(
                f"{self.config.DEEPSEEK_BASE_URL}/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code != 200:
                raise RuntimeError(f"Erreur HTTP {response.status_code}: {response.text}")
            
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
            
        except requests.RequestException as e:
            raise RuntimeError(f"Erreur réseau DeepSeek: {str(e)}")
        except (KeyError, IndexError) as e:
            raise RuntimeError(f"Réponse DeepSeek invalide: {str(e)}")
    
    def lister_plateformes(self):
        """Liste les plateformes IA disponibles"""
        return self.config.get_available_providers()
    
    def lister_modeles(self, plateforme):
        """Liste les modèles disponibles pour une plateforme"""
        if plateforme.lower() == 'openai':
            return list(self.config.OPENAI_MODELS.keys())
        elif plateforme.lower() == 'deepseek':
            return list(self.config.DEEPSEEK_MODELS.keys())
        else:
            raise RuntimeError(f"Plateforme inconnue: {plateforme}")
    
    def generer_reponse_conversationnelle(self, plateforme, modele, message_utilisateur, contexte_bot=""):
        """
        Génère une réponse conversationnelle optimisée pour les chatbots
        
        Args:
            plateforme (str): plateforme IA
            modele (str): modèle à utiliser
            message_utilisateur (str): message de l'utilisateur
            contexte_bot (str): contexte/personnalité du bot
        
        Returns:
            str: réponse du bot
        """
        prompt = f"""Tu es un assistant conversationnel intelligent.
{contexte_bot}

Réponds de manière naturelle, amicale et utile au message suivant:
"{message_utilisateur}"

Réponse:"""
        
        return self.appeler_ia(plateforme, modele, prompt, temperature=0.8, max_tokens=200)

# Instance globale pour F-IA
_ai_integration = AIIntegration()

# Fonctions exposées au langage F-IA
def _appeler_ia(plateforme, modele, message, temperature=0.7, max_tokens=1000):
    """Fonction F-IA pour appeler une IA"""
    return _ai_integration.appeler_ia(plateforme, modele, message, temperature, max_tokens)

def _lister_plateformes_ia():
    """Fonction F-IA pour lister les plateformes IA disponibles"""
    return _ai_integration.lister_plateformes()

def _lister_modeles_ia(plateforme):
    """Fonction F-IA pour lister les modèles d'une plateforme"""
    return _ai_integration.lister_modeles(plateforme)

def _generer_reponse_bot(plateforme, modele, message_utilisateur, contexte=""):
    """Fonction F-IA pour générer des réponses de chatbot"""
    return _ai_integration.generer_reponse_conversationnelle(
        plateforme, modele, message_utilisateur, contexte
    )

def _verifier_config_ia():
    """Fonction F-IA pour vérifier la configuration IA"""
    config_status = {
        "openai": _ai_integration.config.is_openai_configured(),
        "deepseek": _ai_integration.config.is_deepseek_configured()
    }
    return config_status
