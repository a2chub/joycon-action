import streamlit as st
from components.hello_world import hello_world_component

# ページ設定
st.set_page_config(
    page_title="Joycon Action",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .welcome-message {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # メインヘッダー
    st.markdown('<h1 class="main-header">🎮 Joycon Action</h1>', unsafe_allow_html=True)
    
    # サイドバー
    with st.sidebar:
        st.title("ナビゲーション")
        page = st.selectbox(
            "ページを選択",
            ["ホーム", "設定", "ヘルプ"]
        )
    
    # ページルーティング
    if page == "ホーム":
        show_home_page()
    elif page == "設定":
        show_settings_page()
    elif page == "ヘルプ":
        show_help_page()

def show_home_page():
    """ホームページの表示"""
    st.header("ホームページ")
    
    # Hello Worldコンポーネントの表示
    hello_world_component()
    
    # 追加情報
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("プロジェクト情報")
        st.info("""
        このアプリケーションはStreamlitを使用して構築されています。
        
        **技術スタック:**
        - Python
        - Streamlit
        - JavaScript (ブラウザ内)
        """)
    
    with col2:
        st.subheader("機能")
        st.success("""
        **現在の機能:**
        - Hello World表示
        - ナビゲーションシステム
        - レスポンシブデザイン
        
        **今後の予定:**
        - ユーザー認証
        - データ管理
        - API連携
        """)

def show_settings_page():
    """設定ページの表示"""
    st.header("設定")
    st.write("設定機能は今後実装予定です。")
    
    # プレースホルダーとして基本的な設定項目を表示
    st.subheader("基本設定")
    
    theme = st.selectbox("テーマ", ["ライト", "ダーク", "自動"])
    language = st.selectbox("言語", ["日本語", "English"])
    
    if st.button("設定を保存"):
        st.success("設定が保存されました！")

def show_help_page():
    """ヘルプページの表示"""
    st.header("ヘルプ")
    
    st.markdown("""
    ## 使い方
    
    ### 基本操作
    1. 左のサイドバーからページを選択してください
    2. 各ページで利用可能な機能をご使用ください
    
    ### トラブルシューティング
    
    **Q: ページが正しく表示されない**
    A: ブラウザをリフレッシュしてください
    
    **Q: エラーが発生した**
    A: 管理者にお問い合わせください
    
    ### サポート
    技術的な問題や質問については、開発チームまでお問い合わせください。
    """)

if __name__ == "__main__":
    main()