# ai_config.py
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class AIConfig:
    """Configuration pour les plateformes d'IA"""
    
    # Clés API
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    
    # URLs de base
    OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    DEEPSEEK_BASE_URL = os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com/v1')
    
    # Modèles disponibles
    OPENAI_MODELS = {
        'gpt-4.1-nano': 'gpt-4.1-nano',
        'gpt-4-turbo': 'gpt-4-turbo-preview',
        'gpt-3.5': 'gpt-3.5-turbo'
    }
    
    DEEPSEEK_MODELS = {
        'deepseek-chat': 'deepseek-chat',
        'deepseek-coder': 'deepseek-coder'
    }
    
    # Configuration par défaut
    DEFAULT_MODEL = os.getenv('DEFAULT_AI_MODEL', 'gpt-3.5-turbo')
    DEFAULT_MAX_TOKENS = 1000
    DEFAULT_TEMPERATURE = 0.7
    
    @classmethod
    def is_openai_configured(cls):
        """Vérifie si OpenAI est configuré"""
        return bool(cls.OPENAI_API_KEY and cls.OPENAI_API_KEY != 'votre_cle_openai_ici')
    
    @classmethod
    def is_deepseek_configured(cls):
        """Vérifie si DeepSeek est configuré"""
        return bool(cls.DEEPSEEK_API_KEY and cls.DEEPSEEK_API_KEY != 'votre_cle_deepseek_ici')
    
    @classmethod
    def get_available_providers(cls):
        """Retourne la liste des plateformes configurées"""
        providers = []
        if cls.is_openai_configured():
            providers.append('openai')
        if cls.is_deepseek_configured():
            providers.append('deepseek')
        return providers
