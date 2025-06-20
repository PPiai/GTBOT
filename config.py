"""
Configurações centralizadas para Meta Ads Manager
Todas as listas e mapeamentos estão aqui para facilitar manutenção
"""

# ============================================================================
# CONFIGURAÇÕES PRINCIPAIS - EDITE AQUI PARA ALTERAR TUDO
# ============================================================================

class MetaAdsConfig:
    """Configuração centralizada para Meta Ads Manager"""
    
    # OBJETIVOS DE CAMPANHA (ODAX prioritários)
    CAMPAIGN_OBJECTIVES = [
        # ODAX - Prioritários
        "AWARENESS",      # Novo padrão Meta (substitui OUTCOME_AWARENESS)
        "TRAFFIC",        # Novo padrão Meta (substitui OUTCOME_TRAFFIC) 
        "ENGAGEMENT",     # Novo padrão Meta (substitui OUTCOME_ENGAGEMENT)
        "LEADS",          # Novo padrão Meta (substitui OUTCOME_LEADS)
        "REACH",          # Alcance máximo
        # Legados mantidos para compatibilidade
        "BRAND_AWARENESS",
        "VIDEO_VIEWS",
        "LINK_CLICKS", 
        "CONVERSIONS",
        "MESSAGES",
        "POST_ENGAGEMENT",
        "PAGE_LIKES",
        "EVENT_RESPONSES"
    ]
    
    # TIPOS DE OTIMIZAÇÃO por categoria
    OPTIMIZATION_GOALS = [
        # Consciência/Alcance
        "REACH", "IMPRESSIONS", "THRUPLAY", "PROFILE_VISIT",
        # Tráfego
        "LINK_CLICKS", "LANDING_PAGE_VIEWS",
        # Engajamento
        "POST_ENGAGEMENT", "PAGE_LIKES", "EVENT_RESPONSES", 
        "ENGAGED_USERS", "PROFILE_AND_PAGE_ENGAGEMENT",
        # Leads/Conversões
        "LEAD_GENERATION", "QUALITY_LEAD", "CONVERSATIONS", 
        "REMINDERS_SET", "MESSAGING_APPOINTMENT_CONVERSION",
        # Genéricos
        "AD_RECALL_LIFT", "VIDEO_VIEWS", "SOCIAL_IMPRESSIONS"
    ]
    
    # EVENTOS DE COBRANÇA
    BILLING_EVENTS = [
        "IMPRESSIONS",
        "LINK_CLICKS", 
        "CLICKS",
        "PAGE_LIKES",
        "POST_ENGAGEMENT",
        "VIDEO_VIEWS",
        "THRUPLAY"
    ]
    
    # ESTRATÉGIAS DE LANCE
    BID_STRATEGIES = [
        "LOWEST_COST_WITHOUT_CAP",
        "COST_CAP", 
        "LOWEST_COST_WITH_MIN_ROAS",
        "LOWEST_COST_WITH_BID_CAP"
    ]
    
    # CALL TO ACTION
    CTA_OPTIONS = [
        # E-commerce
        "BUY_NOW", "SHOP_NOW", "ADD_TO_CART", "VIEW_CART", "ORDER_NOW",
        # Engajamento
        "LEARN_MORE", "CONTACT_US", "GET_OFFER", "SIGN_UP", "GET_STARTED",
        # Mensagens
        "WHATSAPP_MESSAGE", "MESSAGE_PAGE", "CHAT_WITH_US", "WHATSAPP",
        # Agendamento
        "BOOK_NOW", "BOOK_A_CONSULTATION", "MAKE_APPOINTMENT",
        # Outros populares
        "CONTACT", "DONATE", "SUBSCRIBE", "WATCH_MORE", "FOLLOW_PAGE",
        "GET_DIRECTIONS", "PLAY_GAME", "SEND_A_GIFT", "SHARE"
    ]
    
    # TIPOS DE DESTINO
    DESTINATION_TYPES = [
        # Padrão/Website
        "WEBSITE", "FACEBOOK", "INSTAGRAM_PROFILE",
        # Mensagens
        "MESSENGER", "WHATSAPP", "INSTAGRAM_DIRECT",
        # Outros
        "SHOP_AUTOMATIC", "UNDEFINED"
    ]
    
    # ========================================================================
    # MAPEAMENTOS DE COMPATIBILIDADE - BASEADO NA DOCUMENTAÇÃO META
    # ========================================================================
    
    # Mapeamento Objetivo → Otimizações Válidas
    OBJECTIVE_OPTIMIZATION_MAP = {
        "AWARENESS": ["REACH", "IMPRESSIONS", "THRUPLAY", "PROFILE_VISIT"],
        "TRAFFIC": ["LINK_CLICKS", "LANDING_PAGE_VIEWS"],
        "ENGAGEMENT": ["POST_ENGAGEMENT", "PAGE_LIKES", "EVENT_RESPONSES", 
                      "ENGAGED_USERS", "PROFILE_AND_PAGE_ENGAGEMENT"],
        "LEADS": ["LEAD_GENERATION", "QUALITY_LEAD", "CONVERSATIONS", 
                 "REMINDERS_SET", "MESSAGING_APPOINTMENT_CONVERSION"],
        "REACH": ["REACH", "IMPRESSIONS"],
        # Legados
        "BRAND_AWARENESS": ["AD_RECALL_LIFT", "REACH", "IMPRESSIONS"],
        "VIDEO_VIEWS": ["VIDEO_VIEWS", "THRUPLAY", "IMPRESSIONS"],
        "LINK_CLICKS": ["LINK_CLICKS", "LANDING_PAGE_VIEWS"],
        "CONVERSIONS": ["LINK_CLICKS", "LANDING_PAGE_VIEWS", "IMPRESSIONS"],
        "MESSAGES": ["CONVERSATIONS", "IMPRESSIONS", "REACH"],
        "POST_ENGAGEMENT": ["POST_ENGAGEMENT", "IMPRESSIONS"],
        "PAGE_LIKES": ["PAGE_LIKES", "IMPRESSIONS"],
        "EVENT_RESPONSES": ["EVENT_RESPONSES", "IMPRESSIONS"]
    }
    
    # Mapeamento Otimização → Cobrança Recomendada
    OPTIMIZATION_BILLING_MAP = {
        "REACH": "IMPRESSIONS",
        "IMPRESSIONS": "IMPRESSIONS", 
        "THRUPLAY": "THRUPLAY",
        "LINK_CLICKS": "LINK_CLICKS",
        "LANDING_PAGE_VIEWS": "LINK_CLICKS",
        "POST_ENGAGEMENT": "POST_ENGAGEMENT",
        "PAGE_LIKES": "PAGE_LIKES",
        "VIDEO_VIEWS": "VIDEO_VIEWS",
        "CONVERSATIONS": "IMPRESSIONS",
        "LEAD_GENERATION": "IMPRESSIONS"
    }
    
    # Mapeamento Otimização → Promoted Object Requirements
    PROMOTED_OBJECT_REQUIREMENTS = {
        "REACH": {"required": False, "fields": []},
        "IMPRESSIONS": {"required": False, "fields": []},
        "THRUPLAY": {"required": False, "fields": [], "note": "Criativo deve ser vídeo"},
        "PROFILE_VISIT": {"required": True, "fields": ["page_id"], "note": "Para Instagram"},
        "LINK_CLICKS": {"required": True, "fields": ["object_story_id", "website_conversions"]},
        "LANDING_PAGE_VIEWS": {"required": True, "fields": ["website_conversions", "pixel_id"]},
        "POST_ENGAGEMENT": {"required": True, "fields": ["object_story_id"]},
        "PAGE_LIKES": {"required": True, "fields": ["page_id"]},
        "EVENT_RESPONSES": {"required": True, "fields": ["event_id"]},
        "LEAD_GENERATION": {"required": True, "fields": ["pixel_id", "custom_event_type"]},
        "CONVERSATIONS": {"required": True, "fields": ["page_id"]}
    }
    
    # Templates de campanha atualizados
    CAMPAIGN_TEMPLATES = {
        "Consciência de Marca": {
            "Tipo de Campanha": "ABO",
            "Objetivo da Campanha": "AWARENESS",
            "Status da Campanha": "PAUSED",
            "Tipo de Otimização": "REACH",
            "Cobrança do Adset": "IMPRESSIONS",
            "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
            "Tipo de Anúncio": "Imagem",
            "CTA": "LEARN_MORE",
            "Tipo de Destino": "WEBSITE"
        },
        "Tráfego para Site": {
            "Tipo de Campanha": "ABO", 
            "Objetivo da Campanha": "TRAFFIC",
            "Status da Campanha": "PAUSED",
            "Tipo de Otimização": "LINK_CLICKS",
            "Cobrança do Adset": "LINK_CLICKS",
            "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
            "Tipo de Anúncio": "Imagem",
            "CTA": "LEARN_MORE",
            "Tipo de Destino": "WEBSITE"
        },
        "Engajamento": {
            "Tipo de Campanha": "ABO",
            "Objetivo da Campanha": "ENGAGEMENT", 
            "Status da Campanha": "PAUSED",
            "Tipo de Otimização": "POST_ENGAGEMENT",
            "Cobrança do Adset": "POST_ENGAGEMENT",
            "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
            "Tipo de Anúncio": "Imagem",
            "CTA": "LEARN_MORE",
            "Tipo de Destino": "FACEBOOK"
        },
        "Geração de Leads": {
            "Tipo de Campanha": "ABO",
            "Objetivo da Campanha": "LEADS",
            "Status da Campanha": "PAUSED", 
            "Tipo de Otimização": "LEAD_GENERATION",
            "Cobrança do Adset": "IMPRESSIONS",
            "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
            "Tipo de Anúncio": "Imagem",
            "CTA": "SIGN_UP",
            "Tipo de Destino": "WEBSITE"
        },
        "Mensagem WhatsApp": {
            "Tipo de Campanha": "ABO",
            "Objetivo da Campanha": "LEADS",
            "Status da Campanha": "PAUSED",
            "Tipo de Otimização": "CONVERSATIONS", 
            "Cobrança do Adset": "IMPRESSIONS",
            "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
            "Tipo de Anúncio": "Imagem",
            "CTA": "WHATSAPP_MESSAGE",
            "Tipo de Destino": "WHATSAPP"
        }
    }
    
    # Categorias para documentação
    OBJECTIVE_CATEGORIES = {
        "ODAX Modernos": ["AWARENESS", "TRAFFIC", "ENGAGEMENT", "LEADS", "REACH"],
        "Legados": ["BRAND_AWARENESS", "VIDEO_VIEWS", "LINK_CLICKS", "CONVERSIONS", 
                   "MESSAGES", "POST_ENGAGEMENT", "PAGE_LIKES", "EVENT_RESPONSES"]
    }
    
    OPTIMIZATION_CATEGORIES = {
        "Consciência": ["REACH", "IMPRESSIONS", "THRUPLAY", "PROFILE_VISIT", "AD_RECALL_LIFT"],
        "Tráfego": ["LINK_CLICKS", "LANDING_PAGE_VIEWS"],
        "Engajamento": ["POST_ENGAGEMENT", "PAGE_LIKES", "EVENT_RESPONSES", 
                       "ENGAGED_USERS", "PROFILE_AND_PAGE_ENGAGEMENT"],
        "Leads/Conversões": ["LEAD_GENERATION", "QUALITY_LEAD", "CONVERSATIONS", 
                            "REMINDERS_SET", "MESSAGING_APPOINTMENT_CONVERSION"],
        "Outros": ["VIDEO_VIEWS", "SOCIAL_IMPRESSIONS"]
    }
    
    CTA_CATEGORIES = {
        "E-commerce": ["BUY_NOW", "SHOP_NOW", "ADD_TO_CART", "VIEW_CART", "ORDER_NOW"],
        "Engajamento": ["LEARN_MORE", "CONTACT_US", "GET_OFFER", "SIGN_UP", "GET_STARTED"],
        "Mensagens": ["WHATSAPP_MESSAGE", "MESSAGE_PAGE", "CHAT_WITH_US", "WHATSAPP"],
        "Agendamento": ["BOOK_NOW", "BOOK_A_CONSULTATION", "MAKE_APPOINTMENT"],
        "Social": ["FOLLOW_PAGE", "SHARE", "WATCH_MORE", "PLAY_GAME"]
    }

    # ========================================================================
    # MÉTODOS UTILITÁRIOS
    # ========================================================================
    
    @classmethod
    def get_valid_optimizations(cls, objective):
        """Retorna otimizações válidas para um objetivo"""
        return cls.OBJECTIVE_OPTIMIZATION_MAP.get(objective, [])
    
    @classmethod
    def get_recommended_billing(cls, optimization):
        """Retorna cobrança recomendada para uma otimização"""
        return cls.OPTIMIZATION_BILLING_MAP.get(optimization, "IMPRESSIONS")
    
    @classmethod
    def requires_promoted_object(cls, optimization):
        """Verifica se otimização requer promoted_object"""
        req = cls.PROMOTED_OBJECT_REQUIREMENTS.get(optimization, {})
        return req.get("required", False)
    
    @classmethod
    def get_promoted_object_fields(cls, optimization):
        """Retorna campos necessários para promoted_object"""
        req = cls.PROMOTED_OBJECT_REQUIREMENTS.get(optimization, {})
        return req.get("fields", [])
    
    @classmethod
    def validate_objective_optimization(cls, objective, optimization):
        """Valida se combinação objetivo-otimização é válida"""
        valid_opts = cls.get_valid_optimizations(objective)
        return optimization in valid_opts
    
    @classmethod
    def get_template_data(cls, template_name):
        """Retorna dados de um template"""
        return cls.CAMPAIGN_TEMPLATES.get(template_name, {})
    
    @classmethod
    def get_all_templates(cls):
        """Retorna lista de todos os templates"""
        return list(cls.CAMPAIGN_TEMPLATES.keys())

# Instância global para uso fácil
config = MetaAdsConfig()
