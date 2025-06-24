"""
Configurações centralizadas para Meta Ads Manager
Todas as listas e mapeamentos estão aqui para facilitar manutenção
"""

# ========================================================================
# CONFIGURAÇÃO SIMPLIFICADA E FOCADA PARA META ADS API (Q2 2025)
# Foco em padrões de campanha para Site, Facebook e WhatsApp.
# ========================================================================

# OBJETIVOS DE CAMPANHA (Padrão ODAX Focado)
CAMPAIGN_OBJECTIVES = [
    "OUTCOME_AWARENESS",       # Reconhecimento
    "OUTCOME_TRAFFIC",         # Tráfego
    "OUTCOME_ENGAGEMENT",      # Engajamento
    "OUTCOME_LEADS",           # Leads (Cadastros)
    "OUTCOME_SALES"            # Vendas (para site)
]

# Objetivos legados mais comuns.
LEGACY_OBJECTIVES = [
    "BRAND_AWARENESS", "REACH", "TRAFFIC", "ENGAGEMENT",
    "VIDEO_VIEWS", "LEAD_GENERATION", "MESSAGES", "CONVERSIONS",
    "POST_ENGAGEMENT", "PAGE_LIKES", "EVENT_RESPONSES"
]

# METAS DE OTIMIZAÇÃO (Focadas no Padrão Web)
OPTIMIZATION_GOALS = [
    "AD_RECALL_LIFT",
    "CONVERSATIONS",
    "CONVERSION_LEADS",
    "CONVERSIONS",
    "ENGAGED_USERS",
    "EVENT_RESPONSES",
    "IMPRESSIONS",
    "LANDING_PAGE_VIEWS",
    "LEAD_GENERATION",
    "LINK_CLICKS",
    "OFFSITE_CONVERSIONS",
    "PAGE_LIKES",
    "POST_ENGAGEMENT",
    "QUALITY_LEAD",
    "REACH",
    "REMINDERS_SET",
    "THRUPLAY",
    "VALUE"
]

# EVENTOS DE COBRANÇA (Ad Set Level)
BILLING_EVENTS = [
    "IMPRESSIONS",
    "LINK_CLICKS",
    "THRUPLAY"
]

# ESTRATÉGIAS DE LANCE (Ad Set Level)
BID_STRATEGIES = [
    "LOWEST_COST_WITHOUT_CAP",  # Custo mais baixo (Padrão)
    "COST_CAP",                 # Limite de Custo
    "LOWEST_COST_WITH_BID_CAP", # Limite de Lance
    "LOWEST_COST_WITH_MIN_ROAS" # ROAS Mínimo
]

# OPÇÕES DE CALL TO ACTION (Focadas no Padrão Web e Facebook)
CTA_OPTIONS = [
    "ADD_TO_CART", "APPLY_NOW", "BOOK_TRAVEL", "BUY_NOW", "CONTACT_US",
    "DONATE_NOW", "DOWNLOAD", "EVENT_RSVP", "GET_DIRECTIONS", "GET_OFFER",
    "GET_OFFER_VIEW", "GET_QUOTE", "GET_SHOWTIMES", "LEARN_MORE", "LIKE_PAGE",
    "LISTEN_MUSIC", "LISTEN_NOW", "MESSAGE_PAGE", "OPEN_LINK",
    "ORDER_NOW", "PLAY_GAME", "REQUEST_TIME", "SAVE", "SEE_MENU",
    "SEND_A_GIFT", "SEND_UPDATES", "SHOP_NOW", "SIGN_UP",
    "SUBSCRIBE", "VOTE_NOW", "WATCH_MORE", "WATCH_VIDEO", "WHATSAPP_MESSAGE"
]

# TIPOS DE DESTINO (Focados no Padrão Web e Facebook)
DESTINATION_TYPES = [
    "WEBSITE",
    "MESSENGER",
    "WHATSAPP",
    "FACEBOOK",
    "ON_AD", # Para Formulários Instantâneos
    "MESSAGING_MESSENGER",
    "MESSAGING_WHATSAPP"
]

# ========================================================================
# MAPEAMENTOS DE COMPATIBILIDADE (VERSÃO SIMPLIFICADA)
# ========================================================================

# Mapeamento Objetivo ODAX → Otimizações Válidas
OBJECTIVE_OPTIMIZATION_MAP = {
    "OUTCOME_AWARENESS": ["REACH", "IMPRESSIONS", "AD_RECALL_LIFT", "THRUPLAY"],
    "OUTCOME_TRAFFIC": ["LINK_CLICKS", "LANDING_PAGE_VIEWS", "IMPRESSIONS", "REACH"],
    "OUTCOME_ENGAGEMENT": [
        "POST_ENGAGEMENT", "PAGE_LIKES", "EVENT_RESPONSES", "CONVERSATIONS",
        "THRUPLAY", "REACH", "IMPRESSIONS"
    ],
    "OUTCOME_LEADS": ["LEAD_GENERATION", "CONVERSIONS", "CONVERSATION_LEADS", "QUALITY_LEAD", "IMPRESSIONS"],
    "OUTCOME_SALES": ["CONVERSIONS", "LINK_CLICKS", "LANDING_PAGE_VIEWS", "VALUE", "IMPRESSIONS"]
}

# Mapeamento Otimização → Cobrança Válida (Recomendada)
OPTIMIZATION_BILLING_MAP = {
    "REACH": "IMPRESSIONS",
    "IMPRESSIONS": "IMPRESSIONS",
    "THRUPLAY": "THRUPLAY",
    "LINK_CLICKS": "LINK_CLICKS",
    "LANDING_PAGE_VIEWS": "IMPRESSIONS",
    "POST_ENGAGEMENT": "IMPRESSIONS",
    "PAGE_LIKES": "IMPRESSIONS",
    "CONVERSIONS": "IMPRESSIONS",
    "VALUE": "IMPRESSIONS",
    "LEAD_GENERATION": "IMPRESSIONS",
    "QUALITY_LEAD": "IMPRESSIONS"
}

# NOVO MAPA: Mapeamento Objetivo ODAX → Destinos Válidos
OBJECTIVE_DESTINATION_MAP = {
    "OUTCOME_AWARENESS": ["WEBSITE", "FACEBOOK"],
    "OUTCOME_TRAFFIC": ["WEBSITE", "MESSENGER", "WHATSAPP", "MESSAGING_MESSENGER", "MESSAGING_WHATSAPP"],
    "OUTCOME_ENGAGEMENT": ["FACEBOOK", "WEBSITE", "MESSENGER", "MESSAGING_MESSENGER"],
    "OUTCOME_LEADS": ["WEBSITE", "ON_AD", "MESSENGER", "MESSAGING_MESSENGER"],
    "OUTCOME_SALES": ["WEBSITE"]
}

# ========================================================================
# TEMPLATES DE CAMPANHA (FOCO EM E-COMMERCE E INSIDE SALES)
# ========================================================================

CAMPAIGN_TEMPLATES = {
    "Vendas para E-commerce (Conversão)": {
        "Tipo de Campanha": "CBO",
        "Objetivo da Campanha": "OUTCOME_SALES",
        "Status da Campanha": "PAUSED",
        "Tipo de Otimização": "CONVERSIONS",
        "Cobrança do Adset": "IMPRESSIONS",
        "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
        "Tipo de Anúncio": "Imagem",
        "CTA": "SHOP_NOW",
        "Tipo de Destino": "WEBSITE",
        "Nota": "Requer Pixel da Meta configurado com eventos de conversão (ex: Purchase)."
    },
    "Leads Qualificados (Inside Sales)": {
        "Tipo de Campanha": "ABO",
        "Objetivo da Campanha": "OUTCOME_LEADS",
        "Status da Campanha": "PAUSED",
        "Tipo de Otimização": "QUALITY_LEAD",
        "Cobrança do Adset": "IMPRESSIONS",
        "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
        "Tipo de Anúncio": "Video",
        "CTA": "GET_QUOTE",
        "Tipo de Destino": "ON_AD", # Usa o Formulário Instantâneo
        "Nota": "Utiliza Formulário Instantâneo da Meta. Para máxima qualidade, integre seu CRM."
    },
    "Tráfego para Site": {
        "Tipo de Campanha": "ABO",
        "Objetivo da Campanha": "OUTCOME_TRAFFIC",
        "Status da Campanha": "PAUSED",
        "Tipo de Otimização": "LANDING_PAGE_VIEWS",
        "Cobrança do Adset": "IMPRESSIONS",
        "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
        "Tipo de Anúncio": "Imagem",
        "CTA": "LEARN_MORE",
        "Tipo de Destino": "WEBSITE"
    },
    "Mensagem WhatsApp": {
        "Tipo de Campanha": "ABO",
        "Objetivo da Campanha": "OUTCOME_TRAFFIC",
        "Status da Campanha": "PAUSED",
        "Tipo de Otimização": "CONVERSATIONS",
        "Cobrança do Adset": "IMPRESSIONS",
        "Estratégia de Lance": "LOWEST_COST_WITHOUT_CAP",
        "Tipo de Anúncio": "Imagem",
        "CTA": "WHATSAPP_MESSAGE",
        "Tipo de Destino": "MESSAGING_WHATSAPP"
    }
}

# ========================================================================
# MÉTODOS UTILITÁRIOS E VALIDAÇÃO
# ========================================================================

def get_valid_optimizations(objective):
    """Retorna otimizações válidas para um objetivo"""
    return OBJECTIVE_OPTIMIZATION_MAP.get(objective, [])

def get_recommended_billing(optimization):
    """Retorna cobrança recomendada para uma otimização"""
    return OPTIMIZATION_BILLING_MAP.get(optimization, BILLING_EVENTS[0])

def get_all_templates():
    """Retorna lista de todos os templates"""
    return list(CAMPAIGN_TEMPLATES.keys())

def get_template_data(template_name):
    """Retorna dados de um template"""
    return CAMPAIGN_TEMPLATES.get(template_name, {})

def validate_objective_optimization(objective, optimization):
    """Valida se combinação objetivo-otimização é válida"""
    valid_opts = get_valid_optimizations(objective)
    return optimization in valid_opts

# ========================================================================
# FUNÇÃO DE VALIDAÇÃO DE COMBINAÇÕES
# ========================================================================

def validate_campaign_combination(objective, optimization, billing, bid_strategy, destination, cta):
    """
    Valida uma combinação de parâmetros de campanha com base nas regras da API da Meta.

    Retorna:
        tuple: (bool, str) onde bool é True se a combinação for válida, e str é a mensagem de status.
    """
    # 1. Validação de existência básica
    if objective not in CAMPAIGN_OBJECTIVES: return (False, f"ERRO: Objetivo '{objective}' é inválido.")
    if optimization not in OPTIMIZATION_GOALS: return (False, f"ERRO: Otimização '{optimization}' é inválida.")
    if billing not in BILLING_EVENTS: return (False, f"ERRO: Cobrança '{billing}' é inválida.")
    if bid_strategy not in BID_STRATEGIES: return (False, f"ERRO: Estratégia de lance '{bid_strategy}' é inválida.")
    if destination not in DESTINATION_TYPES: return (False, f"ERRO: Destino '{destination}' é inválido.")
    if cta not in CTA_OPTIONS: return (False, f"ERRO: CTA '{cta}' é inválido.")

    # 2. Validação: Objetivo -> Otimização
    valid_optimizations = OBJECTIVE_OPTIMIZATION_MAP.get(objective, [])
    if optimization not in valid_optimizations:
        return (False, f"FALHA DE COMBINAÇÃO: Otimização '{optimization}' não é válida para o objetivo '{objective}'. Válidas são: {valid_optimizations}")

    # 3. Validação: Objetivo -> Destino
    valid_destinations = OBJECTIVE_DESTINATION_MAP.get(objective, [])
    if destination not in valid_destinations:
        return (False, f"FALHA DE COMBINAÇÃO: Destino '{destination}' não é válido para o objetivo '{objective}'. Válidos são: {valid_destinations}")

    # 4. Validação: Otimização -> Cobrança
    expected_billing = OPTIMIZATION_BILLING_MAP.get(optimization)
    if expected_billing and billing != expected_billing:
        return (False, f"FALHA DE COMBINAÇÃO: Para a otimização '{optimization}', o evento de cobrança esperado é '{expected_billing}', mas foi fornecido '{billing}'.")

    # 5. Validação de Lógica (Avançada)
    # 5a. ROAS Mínimo requer otimização por valor ou conversões
    if bid_strategy == "LOWEST_COST_WITH_MIN_ROAS" and optimization not in ["VALUE", "CONVERSIONS"]:
        return (False, f"FALHA DE LÓGICA: A estratégia de lance 'LOWEST_COST_WITH_MIN_ROAS' requer otimização por 'VALUE' ou 'CONVERSIONS'.")

    # 5b. CTA de WhatsApp deve ter um destino de WhatsApp
    if cta == "WHATSAPP_MESSAGE" and destination not in ["WHATSAPP", "MESSAGING_WHATSAPP"]:
        return (False, f"FALHA DE LÓGICA: O CTA 'WHATSAPP_MESSAGE' deve ser usado com um destino de WhatsApp.")

    # Se todas as checagens passarem
    return (True, "SUCESSO: Combinação válida.")

def requires_promoted_object(optimization):
    """Compatibilidade: sempre retorna False (não há promoted_object obrigatório)"""
    return False

def get_promoted_object_fields(optimization):
    """Compatibilidade: sempre retorna lista vazia (sem campos obrigatórios)"""
    return []
