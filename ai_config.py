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
    OPENAI_BASE_URL = "https://api.openai.com/v1"
    DEEPSEEK_BASE_URL = os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com/v1')
    
    # Modèles disponibles (OFFICIELS 2025)
    OPENAI_MODELS = {
        # Nouveaux modèles GPT-5 (octobre 2025)
        'gpt-5': 'gpt-5',
        'gpt-5-mini': 'gpt-5-mini', 
        'gpt-5-nano': 'gpt-5-nano',
        
        # Modèles GPT-4.1 (avril 2025)
        'gpt-4.1': 'gpt-4.1',
        'gpt-4.1-mini': 'gpt-4.1-mini',
        'gpt-4.1-nano': 'gpt-4.1-nano',
        
        # Modèles GPT-4o (encore supportés)
        'gpt-4o': 'gpt-4o',
        'gpt-4o-mini': 'gpt-4o-mini',
        
        # Modèles legacy
        'gpt-3.5-turbo': 'gpt-3.5-turbo',
        'gpt-4-turbo': 'gpt-4-turbo'
    }
    
    DEEPSEEK_MODELS = {
        'deepseek-chat': 'deepseek-chat',
        'deepseek-coder': 'deepseek-coder',
        'deepseek-v3': 'deepseek-v3'
    }
    
    # Configuration par défaut
    DEFAULT_MODEL = os.getenv('DEFAULT_AI_MODEL', 'gpt-4.1-nano')
    DEFAULT_MAX_TOKENS = 1000
    DEFAULT_TEMPERATURE = 0.7
    
    # Contexte window par modèle (en tokens)
    MODEL_CONTEXT_LIMITS = {
        'gpt-5': 1000000,
        'gpt-5-mini': 1000000,
        'gpt-5-nano': 1000000,
        'gpt-4.1': 1047576,  # ~1M tokens
        'gpt-4.1-mini': 1047576,
        'gpt-4.1-nano': 1047576,
        'gpt-4o': 128000,
        'gpt-4o-mini': 128000,
        'gpt-3.5-turbo': 16385,
        'gpt-4-turbo': 128000
    }
    
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
    
    @classmethod
    def get_model_context_limit(cls, model_name):
        """Retourne la limite de contexte pour un modèle"""
        return cls.MODEL_CONTEXT_LIMITS.get(model_name, 4096)
    
    @classmethod
    def get_recommended_models(cls):
        """Retourne les modèles recommandés par cas d'usage"""
        return {
            'speed': 'gpt-4.1-nano',      # Le plus rapide
            'balance': 'gpt-4.1-mini',    # Équilibre prix/performance
            'quality': 'gpt-5',           # Qualité maximale
            'coding': 'gpt-5',            # Meilleur pour le code
            'cheap': 'gpt-4.1-nano'       # Le moins cher
        }
