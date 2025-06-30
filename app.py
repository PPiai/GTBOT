import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime
import re
from time import sleep
import config

# Set page config
st.set_page_config(
    page_title="Meta Ads Campaign Manager",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS global para forçar tema claro e corrigir todos os elementos
st.markdown("""
<style>
    html, body, .stApp {
        background-color: #fff !important;
    }
    .st-emotion-cache-seewz2 {
        color: black !important;
    }
    /* Força tema claro em todos os elementos */
    body[data-theme="dark"], .stApp[data-theme="dark"] {
        background-color: #fff !important;
        color: #111 !important;
    }
    [data-testid="stSidebar"] {
        background-color: #e5e5e5 !important;
    }
    [data-testid="stSidebar"] * {
        color: #111 !important;
    }
    [data-testid="stHeader"] {
        background-color: #fff !important;
        border-bottom: 1px solid #e0e0e0;
    }
    [data-testid="stHeader"] * {
        color: #111 !important;
        fill: #111 !important;
    }
    /* Botões */
    .stButton > button, button[data-baseweb="button"] {
        background-color: #FF4B4B !important;
        color: #fff !important;
        font-color: #fff !important;
        border: 1px solid #FF4B4B !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
    }
    .stButton > button:hover, button[data-baseweb="button"]:hover {
        background-color: #fff !important;
        color: #FF4B4B !important;
        font-color: #FF4B4B !important;
        border: 1px solid #FF4B4B !important;
    }
    button[data-baseweb="button"] svg {
        fill: #111 !important;
    }
    /* Selectbox, Dropdowns, Radio, Checkbox */
    [data-testid="stSelectbox"] > div, [data-baseweb="select"] > div, .stRadio, .stCheckbox, .stRadio label, .stCheckbox label {
        background-color: #fff !important;
        color: #111 !important;
        border: 1px solid #cccccc !important;
        border-radius: 8px !important;
    }
    [data-testid="stSelectbox"] svg {
        fill: #111 !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"] {
        background-color: #fff !important;
        border: 1px solid #e0e0e0 !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"] li {
        color: #111 !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"] li:hover {
        background-color: #f0f2f6 !important;
    }
    /* Inputs de texto */
    [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input, textarea, [data-testid="stTextArea"] textarea {
        background-color: #fff !important;
        color: #111 !important;
        border: 1px solid #cccccc !important;
        border-radius: 8px !important;
    }
    /* Tabelas */
    [data-testid="stDataGrid"], .stTable, table, th, td {
        background-color: #fff !important;
        color: #111 !important;
        border-color: #e0e0e0 !important;
    }
    [data-testid="stDataGrid"] .glide-header-wrapper {
        background-color: #f0f2f6 !important;
    }
    [data-testid="stDataGrid"] .glide-cell {
        color: #111 !important;
        background-color: #fff !important;
    }
    /* Abas (Tabs) */
    div[data-baseweb="tab"] {
        color: #111 !important;
        font-weight: 500 !important;
        background: #fff !important;
        border: none !important;
    }
    div[data-baseweb="tab"][aria-selected="true"] {
        color: #111 !important;
        border-bottom: 2px solid #FF4B4B !important;
        background: #fff !important;
    }
    /* Blocos de código */
    code {
        background-color: #e9ecef !important;
        color: #495057 !important;
        padding: 0.2rem 0.4rem !important;
        border-radius: 4px !important;
        border: 1px solid #ced4da !important;
    }
    /* Headers e textos customizados */
    .main-header {
        font-size: 2.5rem !important;
        font-weight: bold !important;
        margin-bottom: 1rem !important;
        color: #111 !important;
    }
    .sub-header {
        font-size: 1.5rem !important;
        margin-bottom: 1rem !important;
        color: #111 !important;
    }
    h1, h2, h3, h4, h5, h6, strong, b {
        color: #111 !important;
    }
    .success-message {
        background-color: #e6f7e6 !important;
        color: #2e7d32 !important;
        padding: 1rem !important;
        border-radius: 4px !important;
        margin-bottom: 1rem !important;
    }
    .error-message {
        background-color: #ffebee !important;
        color: #c62828 !important;
        padding: 1rem !important;
        border-radius: 4px !important;
        margin-bottom: 1rem !important;
    }
    /* Sidebar título e divisores */
    
    .st-emotion-cache-1v0mbdj, .st-emotion-cache-1avcm0n {
        color: #111 !important;
    }
    /* Expander e outros detalhes */
    .stExpander, .stExpanderHeader, .stExpanderContent {
        background: #fff !important;
        color: #111 !important;
    }
    /* Corrige slider */
    .stSlider, .stSlider > div {
        background: #fff !important;
        color: #111 !important;
    }
    .st-emotion-cache-qoz3f2 {
        color: black !important;
    }
    /* Corrige alertas e avisos */
    .stAlert, .stAlert > div {
        background: #fffbe6 !important;
        color: #111 !important;
    }
    /* Corrige tooltips */
    .stTooltipContent, .stTooltipContent * {
        background: #fff !important;
        color: #111 !important;
    }
    /* Corrige placeholder de campos desabilitados */
    input:disabled, textarea:disabled, select:disabled {
        background: #f5f5f5 !important;
        color: #bbb !important;
    }
    /* Corrige abas desabilitadas */
    div[data-baseweb="tab"][aria-disabled="true"] {
        color: #bbb !important;
        background: #f5f5f5 !important;
    }
    .st-emotion-cache-1weic72 {
        color: black !important;
    }
    .stButton {
        font-color: black !important;
    }
</style>
""", unsafe_allow_html=True)

# Client accounts data with page_id included
contas = pd.DataFrame([
    {'nome_cliente': 'AJL', 'conta_id': '5557603504330426', 'page_id': ""},
    {'nome_cliente': 'Absoluta Incorporação', 'conta_id': '743422994203639', 'page_id': 109493203959221},
    {'nome_cliente': 'Adapter Sistemas', 'conta_id': '413912314603205', 'page_id': ""},
    {'nome_cliente': 'Agromann', 'conta_id': '764715671633746', 'page_id': ""},
    {'nome_cliente': 'Aguia de Ouro', 'conta_id': '930138122661830', 'page_id': ""},
    {'nome_cliente': 'Alcance', 'conta_id': '2904536849786560', 'page_id': 1271577962865774},
    {'nome_cliente': 'Alcance B2B', 'conta_id': '2904536849786560', 'page_id': 1271577962865774},
    {'nome_cliente': 'Amalog', 'conta_id': '1557368498476976', 'page_id': 477028982164537},
    {'nome_cliente': 'Aquifero', 'conta_id': '1038346274756810', 'page_id': 199445826903776},
    {'nome_cliente': 'Auto Credcard', 'conta_id': '131715405272596', 'page_id': 100630558707028},
    {'nome_cliente': 'Bahls Odontologia', 'conta_id': '341929899811752', 'page_id': 134184147276805},
    {'nome_cliente': 'Bawer Motores', 'conta_id': '346860261810268', 'page_id': 103665665224727},
    {'nome_cliente': 'Biovit', 'conta_id': '3896030874057266', 'page_id': ""},
    {'nome_cliente': 'CSS Log', 'conta_id': '220492102569024', 'page_id': 199624250106007},
    {'nome_cliente': 'CTC', 'conta_id': '860506788095972', 'page_id': 1795514953860843},
    {'nome_cliente': 'Café com Leite', 'conta_id': '733072060715959', 'page_id': 1647716382217687},
    {'nome_cliente': 'Calvin Klein', 'conta_id': '535788031261479', 'page_id': 525738414202280},
    {'nome_cliente': 'Casa dos Motores', 'conta_id': '556908113899805', 'page_id': 191606210935953},
    {'nome_cliente': 'Clero Brasil', 'conta_id': '838288521687758', 'page_id': 307228162647992},
    {'nome_cliente': 'Comam', 'conta_id': '394120044591493', 'page_id': 105239014171312},
    {'nome_cliente': 'Condor', 'conta_id': '203537889759095', 'page_id': ""},
    {'nome_cliente': 'Day Hospital', 'conta_id': '1663531577433280', 'page_id': 249248981611874},
    {'nome_cliente': 'Dziabas', 'conta_id': '2281392792260986', 'page_id': 481551325036520},
    {'nome_cliente': 'Enmed', 'conta_id': '1775072306366660', 'page_id': ""},
    {'nome_cliente': 'Evolution Signs', 'conta_id': '218764335949405', 'page_id': 418238448245945},
    {'nome_cliente': 'Exohair', 'conta_id': '922812376352170', 'page_id': ""},
    {'nome_cliente': 'Extinseto', 'conta_id': '3461207023864', 'page_id': 270989276256375},
    {'nome_cliente': 'FOR-TY STORE', 'conta_id': '7767604866623167', 'page_id': 278960501975649},
    {'nome_cliente': 'Ferragens Floresta', 'conta_id': '199516851165071', 'page_id': ""},
    {'nome_cliente': 'GTL', 'conta_id': '602220500784998', 'page_id': ""},
    {'nome_cliente': 'Gloria Rabello', 'conta_id': '1503339850472458', 'page_id': ""},
    {'nome_cliente': 'HS Gold', 'conta_id': '905719624940336', 'page_id': 363168754077448},
    {'nome_cliente': 'Hidraucambio', 'conta_id': '859616951882800', 'page_id': ""},
    {'nome_cliente': 'Highaus', 'conta_id': '420443957644515', 'page_id': ""},
    {'nome_cliente': 'Intact Estojos', 'conta_id': '1836117320469996', 'page_id': ""},
    {'nome_cliente': 'Italian Gastronomia', 'conta_id': '814045333572501', 'page_id': ""},
    {'nome_cliente': 'JTP Solution', 'conta_id': '1209571203593781', 'page_id': 394943953704805},
    {'nome_cliente': 'Kalatec', 'conta_id': '1604948507066510', 'page_id': ""},
    {'nome_cliente': 'Lefer', 'conta_id': '617886166202496', 'page_id': 112383597266845},
    {'nome_cliente': 'Logline', 'conta_id': '2786386548206132', 'page_id': ""},
    {'nome_cliente': 'MF Peças', 'conta_id': '531544614131498', 'page_id': 101577442722677},
    {'nome_cliente': 'Mactoot', 'conta_id': '155886204959659', 'page_id': 1492102647765264},
    {'nome_cliente': 'Makebetter', 'conta_id': '3236627973136982', 'page_id': 326703403865126},
    {'nome_cliente': 'MaqCenter', 'conta_id': '470618307419362', 'page_id': ""},
    {'nome_cliente': 'Marlin Autos', 'conta_id': '432026079386037', 'page_id': 166142323248808},
    {'nome_cliente': 'Marluvas', 'conta_id': '937586130079158', 'page_id': ""},
    {'nome_cliente': 'Mega Coffee', 'conta_id': '282434177103318', 'page_id': 100318242539661},
    {'nome_cliente': 'Metalsider', 'conta_id': '1625896747769654', 'page_id': ""},
    {'nome_cliente': 'Monnaie', 'conta_id': '1328655617999318', 'page_id': 111771584713208},
    {'nome_cliente': 'Moretti Odontologia', 'conta_id': '1641829612969953', 'page_id': ""},
    {'nome_cliente': 'Nila Photography', 'conta_id': '5837453393018571', 'page_id': ""},
    {'nome_cliente': 'Nutriquality', 'conta_id': '439991594112145', 'page_id': ""},
    {'nome_cliente': 'Oftalmoclínica Américas', 'conta_id': '1749225102281713', 'page_id': ""},
    {'nome_cliente': 'Ornare Semijóias', 'conta_id': '841878016587031', 'page_id': ""},
    {'nome_cliente': 'Panorama', 'conta_id': '1915942465406802', 'page_id': 114033321589862},
    {'nome_cliente': 'Pluralquimica', 'conta_id': '2488064127938269', 'page_id': 539152259281388},
    {'nome_cliente': 'Poligarbo', 'conta_id': '914691500545820', 'page_id': 467109606484475},
    {'nome_cliente': 'Polpa & Congelados', 'conta_id': '1259525575587947', 'page_id': ""},
    {'nome_cliente': 'Proinfo - FIA', 'conta_id': '3577843515771052', 'page_id': 598758560151058},
    {'nome_cliente': 'RTT', 'conta_id': '231030318338724', 'page_id': 102617528870447},
    {'nome_cliente': 'Recoplast', 'conta_id': '623122470618153', 'page_id': 100441515940974},
    {'nome_cliente': 'Remo Fenut', 'conta_id': '898336111347971', 'page_id': ""},
    {'nome_cliente': 'Repsol', 'conta_id': '2232590890444963', 'page_id': 496660016854038},
    {'nome_cliente': 'Resimaq', 'conta_id': '995978674482822', 'page_id': 408769009266365},
    {'nome_cliente': 'SRT Transportes', 'conta_id': '913549057234070', 'page_id': ""},
    {'nome_cliente': 'Sartori Auto Peças', 'conta_id': '616436801130224', 'page_id': ""},
    {'nome_cliente': 'SmartX', 'conta_id': '679012503781785', 'page_id': 119999527860630},
    {'nome_cliente': 'Stone Mall', 'conta_id': '531409504089794', 'page_id': 417879178590331},
    {'nome_cliente': 'Supranet', 'conta_id': '422110711745409', 'page_id': 2660230607327771},
    {'nome_cliente': 'Suruka', 'conta_id': '694252122331708', 'page_id': ""},
    {'nome_cliente': 'Sérgio Calçados', 'conta_id': '1145544443248370', 'page_id': 113881887194677},
    {'nome_cliente': 'Trisul', 'conta_id': '496159270236236', 'page_id': ""},
    {'nome_cliente': 'Trisul (JL)', 'conta_id': '496159270236236', 'page_id': ""},
    {'nome_cliente': 'Tutto Casa', 'conta_id': '1158215392516029', 'page_id': ""},
    {'nome_cliente': 'UV Line', 'conta_id': '513209639246301', 'page_id': 160017340733143},
    {'nome_cliente': 'Vieira Rossi', 'conta_id': '2149206938558605', 'page_id': 150393168472406},
    {'nome_cliente': 'Vivacril', 'conta_id': '330431722463892', 'page_id': 104811258703874},
    {'nome_cliente': 'Vogel', 'conta_id': '921923696764459', 'page_id': 107335274129706},
    {'nome_cliente': 'Wave Solutions', 'conta_id': '1051202479011920', 'page_id': 102622741998288},
    {'nome_cliente': 'Zatta', 'conta_id': '656032961789593', 'page_id': 265063026905654},
    {'nome_cliente': 'Agro Appec', 'conta_id': '1934432050708596', 'page_id': 725785810608279}
])

# Initialize session state variables if they don't exist
if 'page' not in st.session_state:
    st.session_state.page = 'Create Ads'

# Function to validate URL
def is_valid_url(url):
    if not url:
        return False
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

def is_valid_driveurl(url):
    if not url:
        return False
    url_pattern_drive = re.compile(
        r'^https?://'               # começa com http:// ou https://
        r'(?:www\.)?'               # opcional www
        r'drive\.google\.com'       # domínio esperado
        r'(?:/[\w\-./?=&%]*)?$',    # caminhos válidos
        re.IGNORECASE
    )
    return url_pattern_drive.match(url)

# Function to send data to webhook
def send_to_webhook(data, endpoint_url):
    try:
        response = requests.post(
            endpoint_url,
            json=data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            return True, "Dados enviados com sucesso!"
        else:
            return False, f"Erro: {response.status_code} - {response.text}"
    except Exception as e:
        return False, f"Erro: {str(e)}"

# Function to get client data
def get_client_data(cliente_nome):
    client_row = contas[contas['nome_cliente'] == cliente_nome]
    if not client_row.empty:
        return {
            'conta_id': client_row.iloc[0]['conta_id'],
            'page_id': client_row.iloc[0]['page_id']
        }
    return {'conta_id': None, 'page_id': None}

# Function for Create Ads page
def show_create_ads_page():
    st.markdown('<h1 class="main-header">🧩 Criar Anúncios</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Crie anúncios baseados em conjuntos de anúncios existentes</p>', unsafe_allow_html=True)
    
    # Initialize session state for ads data if it doesn't exist
    if 'ads_df' not in st.session_state:
        st.session_state.ads_df = pd.DataFrame(columns=[
            "ID Adset", "Nome Anúncio", "Tipo de Anúncio",
            "Status do Anúncio", "Link de Destino", "Texto do Anúncio", 
            "Call to Action (CTA)", "Imagem / Vídeo", "Thumbnail", "BM Conectada"
        ])
        
    # Create the data editor
    edited_df = st.data_editor(
        st.session_state.ads_df,
        column_config={
            "ID Adset": st.column_config.TextColumn("ID Adset", required=True),
            "Nome Anúncio": st.column_config.TextColumn("Nome Anúncio", required=True),
            "Tipo de Anúncio": st.column_config.SelectboxColumn(
                "Tipo de Anúncio", 
                options=["Imagem", "Video"], 
                required=True
            ),
            "Status do Anúncio": st.column_config.SelectboxColumn(
                "Status do Anúncio", 
                options=["ACTIVE", "PAUSED"], 
                required=True
            ),
            "Link de Destino": st.column_config.TextColumn("Link de Destino", required=True),
            "Texto do Anúncio": st.column_config.TextColumn("Texto do Anúncio", required=True),
            "Call to Action (CTA)": st.column_config.SelectboxColumn(
                "Call to Action (CTA)", 
                options=config.CTA_OPTIONS, 
                required=True
            ),
            "Imagem / Vídeo": st.column_config.TextColumn("Imagem / Vídeo", required=True),
            "Thumbnail": st.column_config.TextColumn("Thumbnail"),
            "BM Conectada": st.column_config.SelectboxColumn(
                "BM Conectada", 
                options=["Piai & Associados", "V4 Ferraz & Co"], 
                required=True
            )
        },
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True
    )
    # Função para buscar adsets do Meta com tratamento de erro e fallback de token
    def fetch_adsets(account_id):
        if not account_id or not str(account_id).strip():
            return None

        tokens = [
            "EAGge1iO10QgBO2kV2C9ZCOPvjF1BUkZAd22dxTJMgwvXCJSNsf0pGP7maW4gznObxU51pjnpB4sSq4AgAxULs8YTJKdNzwJMWDhxQoOzVBdsOEzZCXUgkmjpICZARZCLEB53ZB9DnjKYI8kMhLk72w0MZCI2F8Vw6GPlO3Aklb18G5hbZAGv4TZCGUwZBfeLPWLuP42AZDZD",
            "EAAII0Wm9NVMBO6O08bTsl6xZBVcI2IBOOrUy7b72Jd1pb7ufuAoXzMSp9DIFON9549idhsRaZAZCQZCfClPOxWDJajrE9tyYeSF3lXAvZBKFWBfnmNX7sIbhbSZBSjrzgbNLUdZCCwAa2kYOzW5F4TLEAcDJkLpHl0cNOnbSRMVXVQyBzF6tGuvZBqQZCij1noBw4LwZDZD"
        ]
        url_base = "https://graph.facebook.com/v19.0/act_{}/adsets?fields=id,name,effective_status&statuses=['ACTIVE']&access_token={}"
        for token in tokens:
            url = url_base.format(account_id, token)
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if "data" in data and data["data"]:
                        return data["data"]
                # Se não for 200 ou não houver adsets, tenta próximo token
            except Exception:
                continue
        return None

    # Buscar adsets apenas se houver conta selecionada e conta_id válido
    adsets_data = None
    adsets_table = None  # Inicializa a tabela como None

    if isinstance(contas, pd.DataFrame) and "conta_id" in contas.columns and not contas.empty:
        cliente_selecionado = st.session_state.get("selected_cliente", None)
        if cliente_selecionado:
            linha_cliente = contas[contas["nome_cliente"] == cliente_selecionado]
            if not linha_cliente.empty:
                account_id = linha_cliente.iloc[0]["conta_id"]
                if account_id:
                    adsets_data = fetch_adsets(account_id)
                    if adsets_data is not None and len(adsets_data) > 0:
                        adsets_table = pd.DataFrame([
                            {"Nome do Adset": adset.get("name", ""), "ID do Adset": adset.get("id", "")}
                            for adset in adsets_data
                        ])
                    # Se não houver adsets, adsets_table permanece None

    # Exibe a tabela na página apenas se houver adsets
    if adsets_table is not None and not adsets_table.empty:
        st.markdown("### Adsets Ativos da Conta")
        st.table(adsets_table)
    else:
        st.info("Selecione um cliente para visualizar os adsets ativos da conta.")
    st.session_state.ads_df = edited_df
    
    validation_messages = []
    
    # Validate DataFrame
    if not st.session_state.ads_df.empty:
        for index, row in st.session_state.ads_df.iterrows():
            # Validar Link de Destino
            if not pd.isna(row["Link de Destino"]) and row["Link de Destino"]:
                if not is_valid_url(row["Link de Destino"]):
                    validation_messages.append(f"❌ Linha {index+1}: Link de Destino deve ser uma URL válida")

            # Validar Imagem / Vídeo (pode ter múltiplos links separados por \n)
            image_links = row.get("Imagem / Vídeo", "")
            if pd.notna(image_links) and image_links:
                for line_num, link in enumerate(image_links.strip().split('\n'), 1):
                    if link.strip() and not is_valid_driveurl(link.strip()):
                        validation_messages.append(
                            f"❌ Linha {index+1}: Link de Imagem (linha {line_num}) inválido || Verifique se é do Google Drive"
                        )

            # Validação "Thumbnail"
            thumbnail_link = row.get("Thumbnail", "")
            if pd.notna(thumbnail_link) and thumbnail_link:
                if not is_valid_driveurl(thumbnail_link.strip()):
                    validation_messages.append(
                        f"❌ Linha {index+1}: Link de Thumbnail inválido || Faça upload da imagem no Google Drive"
                    )

        if validation_messages:
            for msg in validation_messages:
                st.markdown(msg)
        else:
            st.markdown("✅ Todos os campos estão válidos!")
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Submit button
    st.divider()
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        submit_button = st.button("🚀 Enviar Anúncios", type="primary", use_container_width=True)
    
    # Process form submission
    if submit_button:
        if st.session_state.ads_df.empty:
            st.error("Por favor, adicione pelo menos um anúncio antes de enviar.")
        elif validation_messages:
            st.error("Por favor, corrija os erros de validação antes de enviar.")
        else:
            # Get client data from sidebar
            client_data = get_client_data(st.session_state.selected_cliente)
            
            # Prepare data for submission
            ads_data = st.session_state.ads_df.to_dict('records')
            
            # Add image and thumbnail links
            for index, row in st.session_state.ads_df.iterrows():
                image_links = row.get("Imagem / Vídeo", "")
                thumbnail_link = row.get("Thumbnail", "")
                
                # Lista de links de imagem por linha
                image_urls = [link.strip() for link in image_links.split('\n') if link.strip()] if image_links else []
                
                # Link único de thumbnail
                thumbnail_url = thumbnail_link.strip() if thumbnail_link else ""
                
                ads_data[index]["Imagens"] = image_urls
                ads_data[index]["Thumbnail (Video)"] = thumbnail_url
                ads_data[index]["SubmissionTime"] = str(datetime.now())
                ads_data[index]["Cliente"] = st.session_state.selected_cliente
                ads_data[index]["ID da Conta de Anúncios"] = client_data['conta_id']
                ads_data[index]["ID da Página"] = client_data['page_id']
            
            # Prepare final payload
            payload = {
                "tipo_requisicao": "criar_anuncio",
                "dados": ads_data,
                "timestamp": str(datetime.now())
            }
            
            # Send to webhook
            webhook_url = "https://ferrazpiai-n8n-webhook.uyk8ty.easypanel.host/webhook/e78ecade-5474-4877-93a6-f91980088282"
            success, message = send_to_webhook(payload, webhook_url)
            
            if success:
                st.markdown("✅ Envio feito com sucesso!")
                st.markdown(f'<div class="success-message">{message}</div>', unsafe_allow_html=True)
                # Clear form after successful submission
                st.session_state.ads_df = pd.DataFrame(columns=[
                    "ID Adset", "Nome Anúncio", "Tipo de Anúncio",
                    "Status do Anúncio", "Link de Destino", "Texto do Anúncio", 
                    "Call to Action (CTA)", "Imagem / Vídeo", "Thumbnail", "BM Conectada"
                ])
                sleep(5)
                st.rerun()
            else:
                st.markdown(f'<div class="error-message">{message}</div>', unsafe_allow_html=True)
            
            st.subheader("📋 Preview JSON")
            st.json(payload, expanded=False)

# Function for Create Campaigns page
def show_create_campaigns_page():
    st.markdown('<h1 class="main-header">🚀 Criar Campanhas</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Crie campanhas completas com entrada manual ou templates</p>', unsafe_allow_html=True)
    
    # Get client data from sidebar
    client_data = get_client_data(st.session_state.selected_cliente)
    
    # Show client info
    st.markdown(f"""
    <div class="client-info">
        <strong>📊 Cliente Selecionado:</strong> {st.session_state.selected_cliente}<br>
        <strong>🏢 Conta ID:</strong> {client_data['conta_id']}<br>
        <strong>📄 Page ID:</strong> {client_data['page_id'] if client_data['page_id'] else 'Não disponível'}
    </div>
    """, unsafe_allow_html=True)
    
    # Template selection usando configuração centralizada
    st.subheader("📋 Template de Campanha (Opcional)")
    template_options = ["Criar do zero"] + config.get_all_templates()
    selected_template = st.selectbox(
        "Selecione um template ou crie do zero",
        template_options
    )
    
    # Initialize form values based on template
    if selected_template != "Criar do zero":
        template_data = config.get_template_data(selected_template)
    else:
        template_data = {}
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Info Geral da Campanha", "⚙️ Configurações do Ad Set", "🎨 Info Criativa", "🎯 Segmentação de Audiência"])
    
    with tab1:
        st.subheader("Informações Gerais da Campanha")
        
        col1, col2 = st.columns(2)
        with col1:
            campaign_type = st.selectbox(
                "Tipo de Campanha",
                ["ABO", "CBO", "ADV+"],
                help="Caso o tipo seja CBO, o valor maximo de lance deve ser maior que R$ 300,00",
                index=["ABO", "CBO", "ADV+"].index(template_data.get("Tipo de Campanha", "ABO"))
            )
        
        with col2:
            campaign_objective = st.selectbox(
                "Objetivo da Campanha",
                config.CAMPAIGN_OBJECTIVES,
                index=config.CAMPAIGN_OBJECTIVES.index(template_data.get("Objetivo da Campanha", config.CAMPAIGN_OBJECTIVES[0]))
            )
        
        campaign_name = st.text_input("Nome da Campanha", placeholder="Digite o Nome da Campanha")

    with tab2:
        st.subheader("Configurações do Ad Set")
        
        col1, col2 = st.columns(2)
        with col1:
            campaign_status = st.selectbox(
                "Status da Campanha",
                ["ACTIVE", "PAUSED"],
                index=["ACTIVE", "PAUSED"].index(template_data.get("Status da Campanha", "PAUSED"))
            )
            
            ad_set_name = st.text_input("Nome do Ad Set", placeholder="Digite o Nome do Ad Set")
        
        with col2:
            # Filtrar otimizações válidas baseado no objetivo selecionado
            valid_optimizations = config.get_valid_optimizations(campaign_objective)
            if valid_optimizations:
                optimization_options = valid_optimizations
            else:
                optimization_options = config.OPTIMIZATION_GOALS
                
            optimization_type = st.selectbox(
                "Tipo de Otimização",
                optimization_options,
                index=optimization_options.index(template_data.get("Tipo de Otimização", optimization_options[0])) if template_data.get("Tipo de Otimização") in optimization_options else 0
            )
        
        # Mostrar cobrança recomendada baseada na otimização
        recommended_billing = config.get_recommended_billing(optimization_type)
        
        col1, col2 = st.columns(2)
        with col1:
            billing_event = st.selectbox(
                "Cobrança do Adset",
                config.BILLING_EVENTS,
                index=config.BILLING_EVENTS.index(recommended_billing) if recommended_billing in config.BILLING_EVENTS else 0
            )
        
        with col2:
            bid_strategy = st.selectbox(
                "Estratégia de Lance",
                config.BID_STRATEGIES,
                index=config.BID_STRATEGIES.index(template_data.get("Estratégia de Lance", config.BID_STRATEGIES[0]))
            )
        
        col1, col2 = st.columns(2)
        with col1:
            daily_budget = st.number_input("Orçamento Diário", min_value=1.0, step=0.5, format="%.2f")
        
        with col2:
            bid_cap = st.number_input("Valor Máximo de Lance (Opcional)", min_value=1.0, step=1.0, format="%.2f", value=None)
    
    with tab3:
        st.subheader("Informações Criativas")

        ad_quantity = st.number_input("Quantidade de Anúncios", min_value=1, value=1, placeholder="Digite a Quantidade")
        ad_type = st.selectbox(
                "Tipo de Anúncio",
                ["Imagem", "Video", "Carrossel"],
                index=["Imagem", "Video", "Carrossel"].index(template_data.get("Tipo de Anúncio", "Imagem"))
            )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:          
            ad_names = []
            ctas = []
            for i in range(ad_quantity):
                ad_name = st.text_input(
                    f"Nome do Anúncio {i+1}", 
                    placeholder="Digite o Nome do Anúncio", 
                    key=f"ad_name_{i}"
                )
                
                ad_names.append(ad_name)

                cta = st.selectbox(
                f"Call to Action {i+1}",
                config.CTA_OPTIONS,
                index=config.CTA_OPTIONS.index(template_data.get("CTA", config.CTA_OPTIONS[0]))
            )
                ctas.append(cta)

        with col2:
            ad_texts = []
            for i in range(ad_quantity):
                ad_text = st.text_input(
                   f"Texto do Anúncio {i+1}", 
                   placeholder="Digite o texto do seu anúncio aqui...", 
                   key=f"ad_text_{i}"
                )
                ad_texts.append(ad_text)

                destination_types = []
                destination_type = st.selectbox(
                f"Tipo de Destino {i+1}",
                config.DESTINATION_TYPES,
                index=config.DESTINATION_TYPES.index(template_data.get("Tipo de Destino", config.DESTINATION_TYPES[0]))
            )   
                destination_types.append(destination_type)

        with col3:
            destination_links = []
            for i in range(ad_quantity):
                destination_link = st.text_input(f"Link de Destino {i+1}", placeholder="https://exemplo.com",key=f"destination_link_{i}")
                destination_links.append(destination_link)                    
                

        
        # Upload sections for campaigns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("📷 **Link da Imagem ou Vídeo**")
            st.markdown("Link do Drive da Imagem")
            campaign_image_links = st.text_area(
                "Adicione a URL do drive de sua Imagem / Vídeo Aqui",
                placeholder="https://drive.google.com/file/d/...",
                value="http://drive.google.com/open?id=COLE_O_ID_AQUI",
                height=100,
                label_visibility="collapsed",
                key="campaign_images"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("🎬 **Link da Thumbnail de Vídeo**")
            st.markdown("Link do Drive da Thumbnail (Caso o Tipo do Anúncio seja Vídeo)")
            campaign_thumbnail_link = st.text_area(
                "Adicione a URL do drive de sua Thumbnail Aqui",
                placeholder="https://drive.google.com/file/d/...",
                value="http://drive.google.com/open?id=COLE_O_ID_AQUI",
                height=100,
                label_visibility="collapsed",
                key="campaign_thumbnail"
            )
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.subheader("Segmentação de Audiência")
        
        col1, col2 = st.columns(2)
        with col1:
            connected_bm = st.selectbox(
                "Conta em Qual BM?",
                ["Piai & Associados", "V4 Ferraz & Co"]
            )
        
        col1, col2 = st.columns(2)
        with col1:
            min_age = st.number_input("Idade Mínima", min_value=13, max_value=65, value=18)
        
        with col2:
            max_age = st.number_input("Idade Máxima", min_value=13, max_value=65, value=65)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            city = st.text_input("Cidade", placeholder="ex: São Paulo")
        
        with col2:
            state = st.text_input("Estado (SP, AL, MT...)", placeholder="ex: SP, RJ")
        
        with col3:
            country = st.text_input("País (BR, US...)", placeholder="ex: BR, US")
        
        radius = st.slider("Raio de Distância (Milhas)", min_value=1, max_value=18, value=9)
    
    # Validation warnings usando configuração centralizada
    st.subheader("⚠️ Validação Inteligente")
    
    # Validação de compatibilidade objetivo-otimização
    if campaign_objective and optimization_type:
        is_valid = config.validate_objective_optimization(campaign_objective, optimization_type)
        if not is_valid:
            st.markdown(f"""
            <div class="compatibility-info">
                ⚠️ <strong>Incompatibilidade Detectada:</strong><br>
                O tipo de otimização '<strong>{optimization_type}</strong>' pode não ser compatível com o objetivo '<strong>{campaign_objective}</strong>'.<br>
                <strong>Otimizações válidas:</strong> {', '.join(config.get_valid_optimizations(campaign_objective))}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("✅ Combinação objetivo-otimização válida!")
    
    # Validação de promoted_object
    if optimization_type:
        requires_promoted = config.requires_promoted_object(optimization_type)
        required_fields = config.get_promoted_object_fields(optimization_type)
        
        if requires_promoted:
            if not client_data['page_id'] and 'page_id' in required_fields:
                st.markdown(f"""
                <div class="compatibility-info">
                    ⚠️ <strong>Page ID Necessário:</strong><br>
                    A otimização '<strong>{optimization_type}</strong>' requer Page ID cadastrado.<br>
                    Cliente atual não possui Page ID. Cadastre antes de prosseguir.
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="compatibility-info">
                ℹ️ <strong>Campos Necessários para '{optimization_type}':</strong><br>
                {', '.join(required_fields) if required_fields else 'Configuração automática'}
            </div>
            """, unsafe_allow_html=True)
    
    # Check for missing page_id
    if not client_data['page_id']:
        st.error(f"⚠️ O cliente '{st.session_state.selected_cliente}' não possui Page ID cadastrado. Isso não é possível para a criação da campanha.")
        st.stop()
    
    # Submit button
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        submit_button = st.button("🚀 Enviar Campanha", type="primary", use_container_width=True)
    
    # Process form submission
    if submit_button:
        # Validate required fields
        required_fields = {
            "Nome da Campanha": campaign_name,
            "Nome do Ad Set": ad_set_name,
            "Link de Destino": destination_link
        }
        
        missing_fields = [field for field, value in required_fields.items() if not value]
        
        # Validate URL format for Destination Link
        invalid_url = False
        if destination_link and not is_valid_url(destination_link):
            invalid_url = True
        
        # Validação especial para otimizações que requerem Page ID
        if config.requires_promoted_object(optimization_type):
            required_fields_opt = config.get_promoted_object_fields(optimization_type)
            if 'page_id' in required_fields_opt and not client_data['page_id']:
                st.error(f"A otimização '{optimization_type}' requer Page ID cadastrado. Por favor, cadastre o Page ID do cliente.")
                st.stop()
        
        if missing_fields:
            st.error(f"Por favor, preencha todos os campos obrigatórios: {', '.join(missing_fields)}")
        elif invalid_url:
            st.error("Link de Destino deve ser uma URL válida começando com http:// ou https://")
        else:
            # Prepare image and thumbnail links
            image_urls = [link.strip() for link in campaign_image_links.split('\n') if link.strip()] if campaign_image_links else []
            thumbnail_url = campaign_thumbnail_link.strip() if campaign_thumbnail_link else ""
            
            # Prepare data for submission
            campaign_data = {
                "ID da Página": client_data['page_id'],
                "ID da Conta de Anúncios": client_data['conta_id'],
                "Tipo de Campanha": campaign_type,
                "Nome da Campanha": campaign_name,
                "Objetivo da Campanha": campaign_objective,
                "Status da Campanha": campaign_status,
                "Nome do Ad Set": ad_set_name,
                "Tipo de Otimização": optimization_type,
                "Cobrança do Adset": billing_event,
                "Estratégia de Lance": bid_strategy,
                "Orçamento Diário": daily_budget,
                "Valor Máximo de Lance": bid_cap,
                "Tipo de Anúncio": ad_type,
                "Nome do Anúncio": ad_names,
                "Texto do Anúncio": ad_texts,
                "Link de Destino": destination_link,
                "CTA": cta,
                "Tipo de Destino": destination_type,
                "Imagens": image_urls,
                "Thumbnail (Video)": thumbnail_url,
                "Conta em Qual BM?": connected_bm,
                "Idade Mínima": min_age,
                "Idade Máxima": max_age,
                "Cidade": city,
                "Estado (SP, AL, MT...)": state,
                "País (BR, EUA...)": country,
                "Raio de Distância": radius,
                "SubmissionTime": str(datetime.now()),
                "Cliente": st.session_state.selected_cliente,
                # Metadados de validação
                "Promoted_Object_Required": config.requires_promoted_object(optimization_type),
                "Required_Fields": config.get_promoted_object_fields(optimization_type)
            }
            
            # Prepare final payload
            payload = {
                "tipo_requisicao": "criar_campanha",
                "dados": campaign_data,
                "timestamp": str(datetime.now())
            }
            
            # Send to webhook
            webhook_url = "https://ferrazpiai-n8n-webhook.uyk8ty.easypanel.host/webhook/e78ecade-5474-4877-93a6-f91980088282"
            success, message = send_to_webhook(payload, webhook_url)
            
            if success:
                st.markdown(f'<div class="success-message">{message}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="error-message">{message}</div>', unsafe_allow_html=True)

            # Display JSON preview
            st.subheader("📋 Preview JSON")
            st.json(payload, expanded=False)

# Function for Documentation page
def show_documentation_page():
    st.markdown('<h1 class="main-header">📚 Documentação Interativa</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Aprenda sobre componentes do Meta Ads e melhores práticas</p>', unsafe_allow_html=True)
    
    # Create tabs for different documentation sections
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🎯 Objetivos de Campanha", 
        "⚙️ Tipos de Otimização", 
        "💰 Eventos de Cobrança", 
        "📊 Estratégias de Lance", 
        "🔘 CTAs", 
        "🌐 Tipos de Destino"
    ])
    
    with tab1:
        st.header("Objetivos de Campanha")
        st.markdown("""
        Os objetivos de campanha definem a meta principal da sua campanha publicitária. 
        **Objetivos modernos** são priorizados pelo Meta para melhor performance.
        """)
        
        # Mostrar objetivos por categoria usando configuração
        for category, objectives in {
            "ODAX Modernos": config.CAMPAIGN_OBJECTIVES,
            "Legados": getattr(config, 'LEGACY_OBJECTIVES', [])
        }.items():
            st.subheader(f"📋 {category}")
            objectives_data = []
            for obj in objectives:
                valid_opts = config.get_valid_optimizations(obj)
                objectives_data.append({
                    "Objetivo": obj,
                    "Otimizações Válidas": len(valid_opts),
                    "Principais": ", ".join(valid_opts[:3]) + ("..." if len(valid_opts) > 3 else "")
                })
            st.table(pd.DataFrame(objectives_data))
        
        with st.expander("🔍 Mapeamento Completo Objetivo → Otimização"):
            for obj, opts in config.OBJECTIVE_OPTIMIZATION_MAP.items():
                st.write(f"**{obj}**: {', '.join(opts)}")
    
    with tab2:
        st.header("Tipos de Otimização")
        st.markdown("""
        Os tipos de otimização informam ao algoritmo do Meta qual ação específica você quer que os usuários realizem.
        """)
        
        # Mostrar otimizações por categoria
        optimization_categories = {
            "Consciência": ["REACH", "IMPRESSIONS", "AD_RECALL_LIFT", "THRUPLAY"],
            "Tráfego": ["LINK_CLICKS", "LANDING_PAGE_VIEWS"],
            "Engajamento": ["POST_ENGAGEMENT", "PAGE_LIKES", "EVENT_RESPONSES", "ENGAGED_USERS"],
            "Leads/Conversões": ["LEAD_GENERATION", "QUALITY_LEAD", "CONVERSATIONS", "CONVERSIONS", "CONVERSION_LEADS"],
            "Outros": [opt for opt in config.OPTIMIZATION_GOALS if opt not in [
                "REACH", "IMPRESSIONS", "AD_RECALL_LIFT", "THRUPLAY",
                "LINK_CLICKS", "LANDING_PAGE_VIEWS",
                "POST_ENGAGEMENT", "PAGE_LIKES", "EVENT_RESPONSES", "ENGAGED_USERS",
                "LEAD_GENERATION", "QUALITY_LEAD", "CONVERSATIONS", "CONVERSIONS", "CONVERSION_LEADS"
            ]]
        }
        for category, optimizations in optimization_categories.items():
            st.subheader(f"🎯 {category}")
            opt_data = []
            for opt in optimizations:
                recommended_billing = config.get_recommended_billing(opt)
                # Não há mais requires_promoted_object, sempre False
                requires_promoted = config.requires_promoted_object(opt)
                opt_data.append({
                    "Otimização": opt,
                    "Cobrança Recomendada": recommended_billing,
                    "Requer Promoted Object": "✅" if requires_promoted else "❌"
                })
            st.table(pd.DataFrame(opt_data))
        
        with st.expander("🔍 Detalhes de Promoted Object"):
            st.info("Não há requisitos de Promoted Object definidos na configuração atual.")
    
    with tab3:
        st.header("Eventos de Cobrança")
        st.markdown("""
        Os eventos de cobrança determinam como o Meta cobra pelos seus anúncios.
        """)
        
        billing_descriptions = {
            "IMPRESSIONS": "Você paga por cada 1.000 impressões",
            "LINK_CLICKS": "Você paga quando alguém clica no link",
            "CLICKS": "Você paga por cliques gerais",
            "PAGE_LIKES": "Você paga por curtidas na página",
            "POST_ENGAGEMENT": "Você paga por interações com posts",
            "VIDEO_VIEWS": "Você paga por visualizações de vídeo",
            "THRUPLAY": "Você paga por reproduções completas de vídeo"
        }
        
        billing_data = []
        for billing in config.BILLING_EVENTS:
            # Contar quantas otimizações recomendam este billing
            recommended_count = sum(1 for opt in config.OPTIMIZATION_GOALS 
                                  if config.get_recommended_billing(opt) == billing)
            
            billing_data.append({
                "Evento de Cobrança": billing,
                "Descrição": billing_descriptions.get(billing, "Descrição não disponível"),
                "Otimizações que Recomendam": recommended_count
            })
        
        st.table(pd.DataFrame(billing_data))
    
    with tab4:
        st.header("Estratégias de Lance")
        st.markdown("""
        As estratégias de lance determinam como o Meta gerencia seus lances no leilão de anúncios.
        """)
        
        bid_descriptions = {
            "LOWEST_COST_WITHOUT_CAP": "Meta automaticamente faz lances para obter o máximo de resultados",
            "COST_CAP": "Meta tenta manter seu custo médio por resultado em ou abaixo do alvo",
            "LOWEST_COST_WITH_MIN_ROAS": "Meta otimiza para valor mínimo de ROAS",
            "LOWEST_COST_WITH_BID_CAP": "Define um valor máximo que você pagará por resultado"
        }
        
        bid_control = {
            "LOWEST_COST_WITHOUT_CAP": "Baixo controle, alta automação",
            "COST_CAP": "Controle médio, automação média",
            "LOWEST_COST_WITH_MIN_ROAS": "Controle médio, focado em valor",
            "LOWEST_COST_WITH_BID_CAP": "Alto controle, baixa automação"
        }
        
        bid_data = []
        for strategy in config.BID_STRATEGIES:
            bid_data.append({
                "Estratégia de Lance": strategy,
                "Descrição": bid_descriptions.get(strategy, ""),
                "Nível de Controle": bid_control.get(strategy, "")
            })
        
        st.table(pd.DataFrame(bid_data))
    
    with tab5:
        st.header("Call to Action (CTA) Buttons")
        st.markdown("""
        Os botões de Call to Action orientam os usuários sobre qual ação tomar após ver seu anúncio.
        """)
        
        # Mostrar CTAs por categorias
        cta_categories = {
            "E-commerce": ["BUY_NOW", "SHOP_NOW", "ADD_TO_CART", "ORDER_NOW"],
            "Engajamento": ["LEARN_MORE", "CONTACT_US", "GET_OFFER", "SIGN_UP", "LIKE_PAGE"],
            "Mensagens": ["WHATSAPP_MESSAGE", "MESSAGE_PAGE"],
            "Outros": [cta for cta in config.CTA_OPTIONS if cta not in [
                "BUY_NOW", "SHOP_NOW", "ADD_TO_CART", "ORDER_NOW",
                "LEARN_MORE", "CONTACT_US", "GET_OFFER", "SIGN_UP", "LIKE_PAGE",
                "WHATSAPP_MESSAGE", "MESSAGE_PAGE"
            ]]
        }
        for category, ctas in cta_categories.items():
            st.subheader(f"🔘 {category}")
            cols = st.columns(3)
            for i, cta in enumerate(ctas):
                with cols[i % 3]:
                    st.write(f"• {cta}")
        
        with st.expander("📋 Lista Completa de CTAs"):
            st.write(f"Total de {len(config.CTA_OPTIONS)} CTAs disponíveis:")
            cols = st.columns(4)
            for i, cta in enumerate(config.CTA_OPTIONS):
                with cols[i % 4]:
                    st.write(f"• {cta}")
    
    with tab6:
        st.header("Tipos de Destino")
        st.markdown("""
        O tipo de destino determina para onde os usuários irão após clicar no seu anúncio.
        """)
        
        destination_descriptions = {
            "WEBSITE": "Direciona para uma página web externa",
            "FACEBOOK": "Mantém usuário no Facebook",
            "INSTAGRAM_PROFILE": "Direciona para perfil do Instagram",
            "MESSENGER": "Abre conversa no Messenger",
            "WHATSAPP": "Abre conversa no WhatsApp",
            "INSTAGRAM_DIRECT": "Mensagem direta no Instagram",
            "SHOP_AUTOMATIC": "Loja automática do Meta",
            "UNDEFINED": "Destino não definido"
        }
        
        destination_data = []
        for dest in config.DESTINATION_TYPES:
            destination_data.append({
                "Tipo de Destino": dest,
                "Descrição": destination_descriptions.get(dest, "Descrição não disponível"),
                "Categoria": "Mensagem" if dest in ["MESSENGER", "WHATSAPP", "INSTAGRAM_DIRECT"] else "Padrão"
            })
        
        st.table(pd.DataFrame(destination_data))

# Sidebar navigation
with st.sidebar:
    st.image("https://i.postimg.cc/FzmbTq38/111254a8-8cf2-4ad7-b2da-9e0f0d44798c.png", width=300)
    st.title("Meta Ads Manager")

    # Client selection with automatic ID population
    cliente = st.selectbox(
        "Selecione o Cliente",
        options=contas['nome_cliente'].tolist(),
        placeholder=None
    )
    
    # Store selected client in session state
    st.session_state.selected_cliente = cliente
    
    # Get client data
    client_data = get_client_data(cliente)
    
    # Display client information
    st.markdown("---")
    st.markdown("**📊 Informações do Cliente:**")
    st.markdown(f"**Cliente:** {cliente}")
    st.markdown(f"**Conta ID:** `{client_data['conta_id']}`")
    if client_data['page_id'] == "":
        st.markdown("**Page ID:** `Não disponível`")
        st.error('⚠️ Page ID não cadastrado\n\nPor favor, pegue o page id e encaminhe para o grupo "Suporte GTBOT" seguindo essa formatação: /page_id: NOME CLIENTE <PAGE ID DO CLIENTE>.')
        chat_url = "https://chat.google.com/room/AAQAOzlyvJU?cls=1" 
        st.markdown(
        f"""
        <a href="{chat_url}" target="_blank" style="
            display: Button;
            background-color: #FF4B4B;
            color: #fff;
            padding: 10px 24px;
            border-radius: 8px;
            font-color: #fff !important; 
            text-decoration: none;
            font-weight: itallic;
            font-size: 16px;
            margin: 8px;
        " onmouseover="this.style.backgroundColor='#fff';this.style.color='#FF4B4B';this.style.border='1px solid #FF4B4B';" onmouseout="this.style.backgroundColor='#FF4B4B';this.style.color='#fff';this.style.border='none';">
            🆘 Suporte
        </a>
        """,
        unsafe_allow_html=True
    )
        st.stop()
    else:
        st.markdown(f"**Page ID:** `{client_data['page_id']}`")
        
    # Navigation buttons
    st.markdown("---")
    if st.button("🧩 Criar Anúncios", key="nav_create_ads", use_container_width=True):
        st.session_state.page = 'Create Ads'
    
    if st.button("🚀 Criar Campanhas", key="nav_create_campaigns", use_container_width=True):
        st.session_state.page = 'Create Campaigns'
    
    if st.button("📚 Documentação", key="nav_documentation", use_container_width=True):
        st.session_state.page = 'Documentation'

    chat_url = "https://chat.google.com/room/AAQAOzlyvJU?cls=1"  

    st.divider()
    st.caption("© 2025 GTBOT")
    st.markdown(
        f"""
        <a href="{chat_url}" target="_blank" style="
            display: Button;
            background-color: #FF4B4B;
            color: #fff;
            padding: 10px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: itallic;
            font-size: 16px;
            margin-top: 8px;
            transition: background 0.2s, color 0.2s;
        " onmouseover="this.style.backgroundColor='#fff';this.style.color='#FF4B4B';this.style.border='1px solid #FF4B4B';" onmouseout="this.style.backgroundColor='#FF4B4B';this.style.color='#fff';this.style.border='none';">
            🆘 Suporte
        </a>
        """,
        unsafe_allow_html=True
    )

# Main content based on selected page
if st.session_state.page == 'Create Ads':
    show_create_ads_page()
elif st.session_state.page == 'Create Campaigns':
    show_create_campaigns_page()
elif st.session_state.page == 'Documentation':
    show_documentation_page()

print("✅ Meta Ads Manager com configuração centralizada!")
print(f"📊 Total de objetivos: {len(config.CAMPAIGN_OBJECTIVES)}")
print(f"⚙️ Total de otimizações: {len(config.OPTIMIZATION_GOALS)}")
print(f"🔘 Total de CTAs: {len(config.CTA_OPTIONS)}")
print(f"🌐 Total de destinos: {len(config.DESTINATION_TYPES)}")
